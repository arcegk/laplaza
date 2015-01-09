# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20150108_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='arroz',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='ensalada',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plato',
            name='tipo',
            field=models.CharField(max_length=25, choices=[(b'SOPA', b'SOPA'), (b'PRINCIPIO', b'PRINCIPIO'), (b'CARNE', b'CARNE'), (b'ENSALADA', b'ENSALADA'), (b'ARROZ', b'ARROZ')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name=b'tel\xc3\xa9fono', blank=True),
            preserve_default=True,
        ),
    ]
