# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0025_auto_20151206_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cod_referido',
            field=models.CharField(max_length=6, unique=True, null=True),
            preserve_default=True,
        ),
    ]
