# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_remove_plato_en_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='arroz',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='ensalada',
        ),
        migrations.AddField(
            model_name='pedido',
            name='direccion',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='empresa',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
    ]
