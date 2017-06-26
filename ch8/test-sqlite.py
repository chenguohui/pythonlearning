#!/usr/bin/python
#encoding=utf-8

import sqlite3
conn=sqlite3.connect(":memory:")#conn = sqlite3.connect(r'd:\testdb.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE User  
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')  #可直接用conn.execute
       
cur.execute("INSERT INTO user (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, '中文', 32, '大连', 20000.00 )") #可直接用conn.execute
cur.execute("insert into user (ID,NAME,AGE)values(?,?,?)" ,(2,u"中文名 " ,23))       
conn.commit()
cur = cur.execute("SELECT id, name, address, salary  from User")
for row in cur.fetchall():
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"
conn.close()


