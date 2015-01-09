# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_plato_en_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platos', models.ManyToManyField(to='rest.Plato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='plato',
            name='en_menu',
            field=models.BooleanField(default=False, verbose_name=b'en menu'),
            preserve_default=True,
        ),
    ]
