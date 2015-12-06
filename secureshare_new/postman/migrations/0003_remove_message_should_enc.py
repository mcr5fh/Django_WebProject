# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '0002_message_should_enc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='should_enc',
        ),
    ]
