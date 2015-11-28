# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0003_auto_20151128_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='visibility',
            field=models.CharField(choices=[('private', 'private'), ('public', 'public')], default='private', max_length=1),
        ),
    ]
