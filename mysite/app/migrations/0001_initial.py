# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('principal', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('class_student', models.ForeignKey(to='app.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('class_teacher', models.ManyToManyField(to='app.Class')),
                ('school_teacher', models.ForeignKey(to='app.School')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teach',
            field=models.ForeignKey(to='app.Teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='school_class',
            field=models.ForeignKey(to='app.School'),
        ),
    ]
