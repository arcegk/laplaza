# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0013_pedido_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='tipo',
            field=models.CharField(max_length=25, choices=[(b'SOPA', b'SOPA'), (b'PRINCIPIO', b'PRINCIPIO'), (b'CARNE', b'CARNE'), (b'ENSALADA', b'ENSALADA'), (b'ARROZ', b'ARROZ'), (b'BEBIDA', b'BEBIDA'), (b'ADICIONAL', b'ADICIONAL'), (b'PRINCIPAL', b'PRINCIPAL')]),
            preserve_default=True,
        ),
    ]
