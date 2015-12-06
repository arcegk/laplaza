# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0023_auto_20151206_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='precio_extra',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
