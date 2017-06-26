# -*- coding: utf-8 -*-
"""
Created on Sat Apr 04 12:41:38 2015

@author: lenovo
"""

from sqlalchemy import Column, Integer, String, ForeignKey  ,DateTime,Boolean
from sqlalchemy import create_engine  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import backref,  mapper, relation, sessionmaker
import datetime
Base = declarative_base()
########################################################################  
class Todo(Base):
    """"""  
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)  
    title = Column(String(255), nullable=False)
    posted_on = Column(DateTime,default=datetime.datetime.now()  )
    status = Column(Boolean, default=False)
    datedue=Column(DateTime )
    level= Column(Integer )
    def __init__(self, id,  title,level,datedue):
        """构造函数"""
        self.id = id
        self.title = title
        self.level=level
        self.datedue=datedue
    def __repr__(self):  
        return  "<todo  ('%s', '%s','%s', '%s','%s')>" % (self.id, self.title,self.level,self.datedue,self.posted_on)

#engine = create_engine("sqlite://", echo=True)
engine =create_engine( 'postgresql://postgres:postgres@localhost:5432/test' ,  echo = True )#echo 是否显示SQL语句
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
####
Session = sessionmaker(bind=engine)
session = Session()
session.bind.echo=False
todo1 = Todo(id=1,title="test1",level=1,datedue=datetime.datetime.now())
todo2 = Todo(id=2,title="test2",level=2,datedue=datetime.datetime.now())
todo3 = Todo(id=3,title="test3",level=12,datedue=datetime.datetime.now())
try:
    session.add(todo1)
    session.add_all([todo2,todo3])
    session.commit()
except:
    session.rollback()
alldata = session.query(Todo).all()
print " data "
for somedata in alldata:
    print somedata

try:
    session.delete(todo1)
    session.commit()
except:
    session.roolback()

alldata=session.query(Todo).all()
for _data in alldata:
    print _data
#update

todo2.title="test!"
session.commit()

#query
print "query "
alldata=session.query(Todo) .all()
for _data in alldata:
    print type(_data)
    print _data.id ,_data.title,_data

alldata=session.query(Todo) .filter(Todo.level>10 ).all()
print str(session.query(Todo) .filter(Todo.level>10 ))