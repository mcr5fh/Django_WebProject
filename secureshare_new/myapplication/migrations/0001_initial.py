# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('short', models.CharField(max_length=200)),
                ('detailed', models.TextField()),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d', blank=True)),
            ],
        ),
    ]
