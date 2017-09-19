# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170919_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='class_teacher',
            field=models.ManyToManyField(to='app.Class', null=True, verbose_name='\u6559\u5e08\u6240\u5728\u73ed\u7ea7', blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='number',
            field=models.CharField(default=datetime.datetime(2017, 9, 19, 8, 27, 14, 764365, tzinfo=utc), max_length=30, verbose_name='\u6559\u5e08id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school_teacher',
            field=models.ForeignKey(verbose_name='\u6559\u5e08\u6240\u5728\u5b66\u6821', blank=True, to='app.School', null=True),
        ),
    ]
