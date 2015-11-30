# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0006_auto_20151129_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='testing',
            new_name='file',
        ),
        migrations.AlterField(
            model_name='report',
            name='files',
            field=models.ManyToManyField(related_name='files', to='myapplication.File'),
        ),
    ]
