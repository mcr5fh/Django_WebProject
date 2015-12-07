# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0026_auto_20151203_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='encrypt',
            field=models.BooleanField(default=False),
        ),
    ]
