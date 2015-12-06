# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0014_report_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('file', models.FileField(upload_to='attachments', verbose_name='Attachment')),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='file',
        ),
        migrations.AddField(
            model_name='attachment',
            name='report',
            field=models.ForeignKey(to='myapplication.Report', verbose_name='Report'),
        ),
    ]
