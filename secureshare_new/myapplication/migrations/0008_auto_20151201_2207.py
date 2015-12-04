# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0007_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user', models.CharField(default=True, max_length=200)),
                ('folder_name', models.CharField(max_length=200, null=True)),
                ('visibility', models.CharField(default='private', choices=[('private', 'private'), ('public', 'public')], max_length=7)),
            ],
            options={
                'ordering': ('folder_name',),
            },
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('user',)},
        ),
        migrations.AddField(
            model_name='report_folder',
            name='files',
            field=models.ManyToManyField(to='myapplication.Report'),
        ),
    ]
