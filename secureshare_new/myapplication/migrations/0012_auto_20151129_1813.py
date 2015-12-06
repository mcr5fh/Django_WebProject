# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0011_auto_20151129_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='files',
            new_name='stuff',
        ),
        migrations.AlterField(
            model_name='file',
            name='property',
            field=models.ForeignKey(related_name='files', to='myapplication.Report'),
        ),
    ]
