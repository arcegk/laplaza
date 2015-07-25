# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0019_auto_20150616_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='nombre',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
