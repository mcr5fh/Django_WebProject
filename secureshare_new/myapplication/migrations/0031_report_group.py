# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('myapplication', '0030_auto_20151207_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ManyToManyField(to='auth.Group', null=True),
        ),
    ]
