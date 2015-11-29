# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0004_auto_20151128_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='visibility',
            field=models.CharField(max_length=7, choices=[('private', 'private'), ('public', 'public')], default='private'),
        ),
    ]
