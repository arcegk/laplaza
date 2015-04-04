# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0017_pedido_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telefono',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='observaciones',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
