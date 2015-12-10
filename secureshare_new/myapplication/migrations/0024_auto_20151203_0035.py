# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0023_auto_20151203_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='user',
            new_name='username',
        ),
    ]
