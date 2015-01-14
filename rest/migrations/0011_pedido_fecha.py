# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0010_auto_20150112_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 1, 13, 22, 38, 27, 347827, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
