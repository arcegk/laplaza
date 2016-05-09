# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0029_user_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cobrar',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='credito_especial',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='credito_normal',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
