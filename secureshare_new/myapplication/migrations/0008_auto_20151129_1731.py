# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0007_auto_20151129_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='files',
        ),
        migrations.AddField(
            model_name='file',
            name='property',
            field=models.ForeignKey(related_name='files', default=1, to='myapplication.Report'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='documents/%Y/%m/%d', blank=True),
        ),
    ]
