# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0018_auto_20150404_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='direccion',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
