# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('short', models.CharField(max_length=200)),
                ('detailed', models.TextField()),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
