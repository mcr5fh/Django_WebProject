# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='visibility',
            field=models.CharField(choices=[('1', 'private'), ('2', 'public')], blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True),
        ),
    ]
