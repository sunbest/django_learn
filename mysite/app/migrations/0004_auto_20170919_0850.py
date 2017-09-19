# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170919_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_student',
            field=models.ForeignKey(verbose_name='\u5b66\u751f\u6240\u5728\u73ed\u7ea7', blank=True, to='app.Class', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_school',
            field=models.ForeignKey(verbose_name='\u5b66\u751f\u6240\u5728\u5b66\u6821', blank=True, to='app.School', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(verbose_name='\u4efb\u6559\u6559\u5e08', blank=True, to='app.Teacher', null=True),
        ),
    ]
