# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0022_auto_20151206_1455'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ubicaciones',
            new_name='Ubicacion',
        ),
    ]
