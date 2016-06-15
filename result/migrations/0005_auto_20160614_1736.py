# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_auto_20160610_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='swiss_bill_score',
            field=models.FloatField(default=0, verbose_name='Кол-во очков по швец. системе'),
        ),
    ]
