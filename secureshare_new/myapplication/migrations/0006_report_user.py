# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0005_auto_20151128_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
