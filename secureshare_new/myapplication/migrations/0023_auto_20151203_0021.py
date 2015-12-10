# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0022_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report_folder',
            name='files',
        ),
        migrations.AlterModelOptions(
            name='report',
            options={},
        ),
        migrations.DeleteModel(
            name='Report_Folder',
        ),
    ]
