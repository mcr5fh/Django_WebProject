# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0010_auto_20151129_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='property',
            field=models.ForeignKey(to='myapplication.Report'),
        ),
    ]
