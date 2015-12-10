# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0002_auto_20151128_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='visibility',
            field=models.CharField(max_length=1, choices=[('1', 'private'), ('2', 'public')], default='1'),
        ),
    ]
