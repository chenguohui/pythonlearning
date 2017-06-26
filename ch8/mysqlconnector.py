# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 21:03:06 2015

@author: lenovo
"""
 
from __future__ import print_function
import mysql.connector
from datetime import date, datetime, timedelta
from mysql.connector import errorcode
DB_NAME = 'todolist'
 
cnx =mysql.connector.connect ( user='root', password='123456',
                              host='127.0.0.1')
                              
cursor = cnx.cursor()
cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
TABLE  = ('''
        CREATE TABLE `todolist`.`todo` (
        `id` INT NOT NULL COMMENT '',
        `titile` TEXT NULL COMMENT '',
        `posted_on` DATE NULL COMMENT '',
        `datedue` DATE NULL COMMENT '',
        `level` INT NULL COMMENT '',
        PRIMARY KEY (`id`)  COMMENT '')
        '''
        )
    
cursor.execute(TABLE)

cursor.close()
cnx.close()
                              
cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1',
                              database=DB_NAME 
                               )

cursor = cnx.cursor()
 
insertsql = ("INSERT INTO todo "
               "(id, titile, posted_on, datedue, level) "
               "VALUES (%s, %s, %s, %s, %s)")
    
todo_data1 = (12, 'write','2012-09-08', '2012-09-09',1 )
todo_data2=(10,str(datetime.now().date()), str( datetime.now().date()+ timedelta(days=1)),2)

cursor.execute(insertsql, todo_data1)

todo_data2=(10,"read",str(datetime.now().date()), str( datetime.now().date()+ timedelta(days=1)),2)

  
 
cursor.execute(insertsql, todo_data2)
cnx.commit()
cursor.close()
cnx.close()

cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1',
                              database=DB_NAME 
                               )

cursor = cnx.cursor()

nghu query =  "SELECT * FROM todo " 
 
cursor.execute(query )
while True:
    row = cursor.fetchone()
    if row == None:
        break
    print (row[0], row[1], row[2] ,row[3]) 


cnx.commit()
cursor.close()
cnx.close()


 

