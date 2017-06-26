# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Windows系统下，psycopg2从http://www.stickpeople.com/projects/python/win-psycopg/下载
其余操作系统请按照http://initd.org/psycopg/docs/install.html中提及的Linux  系统与Mac OS X进行安装 。
'''
import psycopg2
import psycopg2.extras
import datetime
conn = psycopg2.connect(database="test", user="postgres", password="postgres", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS todo")
cur.execute('''CREATE TABLE todo
(
  id serial NOT NULL,
  title character varying(255) NOT NULL,
  posted_on date,
  status boolean DEFAULT false ,
  DateDue date,
  level integer,
  CONSTRAINT todo_pkey PRIMARY KEY (id)
    )''')
print "Table created successfully"



cur=conn.cursor()
cur.execute("INSERT INTO todo (id,title , DateDue ,level) \
      VALUES (1,  '第一个 ',   '2015-12-12', 1)");
cur.execute("INSERT INTO todo (id,title , DateDue ,level) \
      VALUES (2, '第二个',   '2015-12-12', 1)");
cur.execute("INSERT INTO todo (id,title , DateDue ,level) \
      VALUES (3, '第三个',   '2015-12-12', 1)");
# executemany
query = "INSERT INTO todo ( id, title, DateDue,level ) VALUES (%s,  %s, %s ,%s)"
todolist = (
    (  12,'第四个', datetime.date(2015, 11, 11) ,12 ),
    ( 13, '第五个', datetime.date(2015, 11, 18) ,132 )
)
cur.executemany(query, todolist)
##select
cur.execute("SELECT * from todo")
rows = cur.fetchall()
print"所有字段名 ", zip(*cur.description)[0]
columnname=zip(*cur.description)[0]
for row in rows:
    k=0
    while k <len(columnname):
        print columnname[k],":", row[k]
        k=k+1
# one by one
cur.execute("SELECT * FROM todo")
while True:
    row = cur.fetchone()
    if row == None:
        break
    print row[0], row[1], row[2]

#update
cur = conn.cursor()
print "update ";
cur.execute(("UPDATE todo set level =%s where ID=1")%13)
cur.execute(("SELECT * FROM todo where id=%s")%1)
row=cur.fetchone()
print row[0], row[1], row[2],row[3],row[4],row[5]

print "delete  ";
cur.execute("DELETE from todo where ID=1")
# one by one
cur.execute("SELECT * FROM todo")
while True:
    row = cur.fetchone()
    if row == None:
        break
    print row[0], row[1], row[2]
conn.close()

#dict conection

conn=psycopg2.connect(database="test", user="postgres", password="postgres", host="127.0.0.1", port="5432", connection_factory=psycopg2.extras.DictConnection )
dict_cur=conn.cursor( cursor_factory=psycopg2.extras.NamedTupleCursor)
dict_cur.execute("SELECT * FROM todo")
rows = dict_cur.fetchall()
for row in rows:
    print row['id'],row['title']
conn.close()


