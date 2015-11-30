# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0016_auto_20151129_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='report',
            field=models.ForeignKey(to='myapplication.Report', related_name='file_set', verbose_name='Report'),
        ),
    ]
