# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0009_auto_20151129_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='files',
            field=models.ForeignKey(to='myapplication.File'),
        ),
    ]
