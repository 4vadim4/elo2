# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_swiss_bill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='swiss_bill',
            options={'verbose_name': 'Список участников Swiss sys', 'verbose_name_plural': 'Список участников Swiss sys'},
        ),
        migrations.RenameField(
            model_name='swiss_bill',
            old_name='swiss_bill_fio',
            new_name='user',
        ),
    ]
