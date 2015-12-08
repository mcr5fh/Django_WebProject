# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0027_report_encrypt'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='username',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
