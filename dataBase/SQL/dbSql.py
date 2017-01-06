#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')

cur = conn.cursor()

cur.execute('create table demo(num int,str varchar(20));')

cur.execute('insert into demo VALUES (%d,"%s")'%(1,'aaa'))
cur.execute('insert into demo VALUES (%d,"%s")'%(2,'bbb'))
cur.execute('insert into demo VALUES (%d,"%s")'%(3,'ccc'))

cur.execute('update demo SET str = "%s" where num = %d'%('ddd',3))

cur.execute('SELECT * FROM demo;')
rows = cur.fetchall()
print('number of records:',len(rows))

for i in rows:
	print(i)
	
conn.commit()

cur.close()

conn.close()