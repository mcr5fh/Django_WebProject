# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '0003_remove_message_should_enc'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='encrypted',
            field=models.BooleanField(default=False, verbose_name='enc'),
        ),
    ]
