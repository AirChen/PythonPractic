#!/usr/bin/python
# coding=utf-8

from peewee import *

db = SqliteDatabase('sampleDB.db')

class BaseModel(Model):
	class Meta:
		database = db
		

class Course(BaseModel):
	id = PrimaryKeyField()
	title = CharField(null = False)
	period = IntegerField()
	description = CharField()
		
class Teacher(BaseModel):
	id = PrimaryKeyField()
	name = CharField()
	gender = BooleanField()
	address = CharField()
	course_id = ForeignKeyField(Course,to_field = 'id',related_name = 'course')
		
if __name__ == "__main__":
	Course.create_table()
	Teacher.create_table()
	
	Course.create(id = 1, title = u'经济学',period = 320,description = u'好学')
	Course.create(id = 2, title = u'大学英语',period = 30,description = u'不好学')
	Course.create(id = 3, title = u'哲学',period = 320,description = u'云里雾里')
	Course.create(id = 104, title = u'编译原理',period = 320,description = u'计算机基础')
	Course.create(id = 5, title = u'高数',period = 320,description = u'搞不懂')
	
	Teacher.create(name = u'白白', gender = True,address = '...',course_id = 1)
	Teacher.create(name = u'嘿嘿', gender = False,address = '...',course_id = 1)
	Teacher.create(name = u'大熊', gender = True,address = '...',course_id = 1)
	Teacher.create(name = u'小熊', gender = True,address = '...',course_id = 1)
	
	record = Course.get(Course.title == u'大学英语')
	print("Course:%s, period:%d"%(record.title,record.period))
	
	record.period = 200
	record.save()
	
	record.delete_instance()
	
	course = Course.select()
	total = Course.select(fn.Avg (Course.period).alias('avg_period'))
	
	Course.update(period = 300).where(Course.id > 100).execute()
	
	Record = Course.select().join(Teacher).where(Teacher.gender == True)