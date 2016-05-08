# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0028_user_is_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
