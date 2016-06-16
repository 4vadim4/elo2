# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_auto_20160614_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_elo',
            field=models.FloatField(null=True, verbose_name='Показатель ЭЛО', blank=True),
        ),
    ]
