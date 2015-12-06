# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0021_auto_20151128_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.CharField(max_length=200)),
                ('lon', models.CharField(max_length=200)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='plato',
            name='tipo',
            field=models.CharField(max_length=25, choices=[(b'SOPA', b'SOPA'), (b'PRINCIPIO', b'PRINCIPIO'), (b'PROTEINA', b'PROTEINA'), (b'ENSALADA', b'ENSALADA'), (b'ARROZ', b'ARROZ'), (b'BEBIDA', b'BEBIDA'), (b'ADICIONAL', b'ADICIONAL'), (b'PRINCIPAL', b'PRINCIPAL'), (b'ACOMPANANTE', b'ACOMPANANTE'), (b'ESPECIAL', b'ESPECIAL')]),
            preserve_default=True,
        ),
    ]
