# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_auto_20150109_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plato',
            name='en_menu',
        ),
    ]
