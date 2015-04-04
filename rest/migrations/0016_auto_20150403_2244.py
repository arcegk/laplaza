# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0015_auto_20150403_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='nombre',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='observaciones',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
