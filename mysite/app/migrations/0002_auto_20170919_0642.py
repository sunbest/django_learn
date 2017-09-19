# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_school',
            field=models.ForeignKey(verbose_name='\u73ed\u7ea7\u6240\u5728\u5b66\u6821', blank=True, to='app.School', null=True),
        ),
    ]
