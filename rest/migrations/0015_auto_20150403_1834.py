# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0014_auto_20150330_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='telefono',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plato',
            name='tipo',
            field=models.CharField(max_length=25, choices=[(b'SOPA', b'SOPA'), (b'PRINCIPIO', b'PRINCIPIO'), (b'CARNE', b'CARNE'), (b'ENSALADA', b'ENSALADA'), (b'ARROZ', b'ARROZ'), (b'BEBIDA', b'BEBIDA'), (b'ADICIONAL', b'ADICIONAL'), (b'PRINCIPAL', b'PRINCIPAL'), (b'ACOMPANANTE', b'ACOMPANANTE')]),
            preserve_default=True,
        ),
    ]
