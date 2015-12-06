# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0005_auto_20151128_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('testing', models.FileField(upload_to='files', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='file',
        ),
        migrations.AddField(
            model_name='report',
            name='files',
            field=models.ManyToManyField(related_name='file', to='myapplication.File'),
        ),
    ]
