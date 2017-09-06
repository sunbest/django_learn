# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import xlrd
class School(models.Model):
    school_id = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    principal=models.CharField(max_length=30)
    
    class Meta:
    	verbose_name_plural=u"学校"
    def __unicode__(self):
        return self.name
    
    @classmethod
    def create(cls, school_id,name,principal):
        sch= cls(school_id=school_id,name=name,principal=principal)
        return sch
    def sch_stu(self):
        return self.student_set 

    def sch_teacher(self):
        return self.teacher_set 

workbook = xlrd.open_workbook(r'/home/tianwe/project/test.xlsx')
sheet2 = workbook.sheet_by_index(1)
row_one = sheet2.col_values(0)
row_two = sheet2.col_values(1)
row_three = sheet2.col_values(2)
ID=[int(ID) for ID in row_one ]
name=[name for name in row_two ]
principal=[principal for principal in row_three]
d=zip(ID,name,principal)
id_list= School.objects.values_list('school_id',flat=1)
for id_lists in id_list:
    for school in d:
        if id_lists in ID:
            pass
        else:
            School.create(*school)

class Class(models.Model):
    class_id = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    school_class=models.ForeignKey(School)

    class Meta:
    	verbose_name_plural=u"班级"
    def __unicode__(self):
        return self.name
    
class Teacher(models.Model):
    teacher_id=models.CharField(max_length=30)    
    name = models.CharField(max_length=50)
    class_teacher=models.ManyToManyField(Class)
    school_teacher=models.ForeignKey(School)

    class Meta:
    	verbose_name_plural=u"教师" 
    def __unicode__(self):
        return self.name   

class Student(models.Model):
    student_id = models.CharField(max_length=30) 
    name = models.CharField(max_length=50)
    class_student=models.ForeignKey(Class)
    teach=models.ForeignKey(Teacher)

    class Meta:
    	verbose_name_plural=u"学生"
    def __unicode__(self):
        return self.name

       

  
