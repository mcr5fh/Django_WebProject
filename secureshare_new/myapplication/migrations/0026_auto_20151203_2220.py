# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0025_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='detailed',
            field=models.TextField(default=''),
        ),
    ]
