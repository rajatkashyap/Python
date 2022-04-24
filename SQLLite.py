# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 07:43:01 2018

@author: U40MV02
"""

import sqlite3 as db
conn=db.connect('test.db')
print conn
c=conn.cursor()
print c
c.execute('Drop table  IF EXISTS Students' )
c.execute('CREATE TABLE Students (gtid INTEGER, name TEXT)' )
c.execute("insert into Students values (101,'Rajat')")

more_students = [(723, 'Rozga'),
                 (882, 'Zha'),
                 (401, 'Park'),
                 (377, 'Vetter'),
                 (904, 'Brown')]

c.executemany("insert into Students values (?,?)",more_students)

conn.commit()
c.execute('select * from Students')
results=c.fetchall()
for i in results:
    print i