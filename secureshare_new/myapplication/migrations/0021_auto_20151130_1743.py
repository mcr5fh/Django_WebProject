# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0020_auto_20151130_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='report',
        ),
        migrations.AddField(
            model_name='report',
            name='file1',
            field=models.FileField(blank=True, upload_to='attachments', null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='file2',
            field=models.FileField(blank=True, upload_to='attachments', null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='file3',
            field=models.FileField(blank=True, upload_to='attachments', null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='file4',
            field=models.FileField(blank=True, upload_to='attachments', null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='file5',
            field=models.FileField(blank=True, upload_to='attachments', null=True),
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
    ]
