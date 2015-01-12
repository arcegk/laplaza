# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0009_auto_20150112_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='direccion',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='empresa',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plato',
            name='seccion',
            field=models.CharField(max_length=25, choices=[(b'DESAYUNO', b'DESAYUNO'), (b'ALMUERZO', b'ALMUERZO'), (b'ADICIONAL', b'ADICIONAL')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='empresa',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
    ]
