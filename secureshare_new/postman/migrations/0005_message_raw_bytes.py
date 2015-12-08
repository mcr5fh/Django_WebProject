# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '0004_message_encrypted'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='raw_bytes',
            field=models.BinaryField(verbose_name='raw', null=True),
        ),
    ]
