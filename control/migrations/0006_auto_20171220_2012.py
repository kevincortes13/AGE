# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0005_auto_20171220_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrenador',
            name='cargo',
            field=models.CharField(choices=[('vacio', ' '), ('entrenador', 'Entrenador')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entrenador',
            name='club',
            field=models.ForeignKey(related_name='c_entrenador', null=True, blank=True, to='control.Club'),
        ),
    ]
