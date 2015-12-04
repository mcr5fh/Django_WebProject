# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0008_auto_20151129_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='files',
            field=models.ForeignKey(default=1, to='myapplication.File'),
        ),
        migrations.AlterField(
            model_name='file',
            name='property',
            field=models.ForeignKey(default=1, to='myapplication.Report'),
        ),
    ]
