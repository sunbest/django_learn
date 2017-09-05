# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class School(models.Model):
    school_id = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    principal=models.CharField(max_length=30)
    def __str__(self):
   	    return self.name
    
    @classmethod
    def create(cls, school_id,name,principal):
        sch= cls(school_id=school_id,name=name,principal=principal)
        return sch

	def sch_stu(self):
   		return self. student_set 

   	def sch_teacher(self):
   	    return self.teacher_set 

schools=School.create(00001,"zhongxue","tianwei")
s=School.objects.get(pk=1)
f=s.sch_stu()
class Class(models.Model):
    class_id = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    school_class=models.ForeignKey(School)
    def __str__(self):
   	    return self.name
    
class Teacher(models.Model):
	teacher_id = models.CharField(max_length=30)    
	name = models.CharField(max_length=50)
	class_teacher= models.ManyToManyField(Class)
	school_teacher=models.ForeignKey(School) 
	def __str__(self):
   	    return self.name   

class Student(models.Model):
    student_id = models.CharField(max_length=30) 
    name = models.CharField(max_length=50)
    class_student=models.ForeignKey(Class)
    teach=models.ForeignKey(Teacher)
    def __str__(self):
   	    return self.name

       

  
