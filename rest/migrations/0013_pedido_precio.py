# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0012_auto_20150113_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='precio',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
