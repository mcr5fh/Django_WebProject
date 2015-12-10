# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0017_auto_20151130_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='report',
            field=models.ForeignKey(to='myapplication.Report', related_name='attachment_set', verbose_name='Report'),
        ),
    ]
