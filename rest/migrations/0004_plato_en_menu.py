# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20150109_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='en_menu',
            field=models.BooleanField(default=False, verbose_name=b'en men\xc3\xba'),
            preserve_default=True,
        ),
    ]
