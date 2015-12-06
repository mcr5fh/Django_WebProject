# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0012_auto_20151129_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='property',
        ),
        migrations.RemoveField(
            model_name='report',
            name='stuff',
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
