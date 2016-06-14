# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20160610_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swiss_bill',
            name='user',
        ),
        migrations.DeleteModel(
            name='Swiss_Bill',
        ),
        migrations.AddField(
            model_name='bill',
            name='swiss_bill_score',
            field=models.IntegerField(default=0, verbose_name='Кол-во очков по швец. системе'),
            preserve_default=True,
        ),
    ]
