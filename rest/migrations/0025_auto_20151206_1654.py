# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0024_plato_precio_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='precio_extra',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
