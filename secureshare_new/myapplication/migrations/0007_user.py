# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0006_report_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=200, default='null')),
                ('last_name', models.CharField(max_length=200, default='null')),
                ('username', models.CharField(max_length=200, default='null')),
                ('password', models.CharField(max_length=200, default='null')),
                ('is_superuser', models.BooleanField(default='false')),
            ],
        ),
    ]
