# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0007_auto_20150111_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='seccion',
            field=models.CharField(default=b'', max_length=25, choices=[(b'DESAYUNO', b'DESAYUNO'), (b'ALMUERZO', b'ALMURZO'), (b'ADICIONAL', b'ADICIONAL')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plato',
            name='tipo',
            field=models.CharField(max_length=25, choices=[(b'SOPA', b'SOPA'), (b'PRINCIPIO', b'PRINCIPIO'), (b'CARNE', b'CARNE'), (b'ENSALADA', b'ENSALADA'), (b'ARROZ', b'ARROZ'), (b'BEBIDA', b'BEBIDA'), (b'ADICIONAL', b'ADICIONAL')]),
            preserve_default=True,
        ),
    ]
