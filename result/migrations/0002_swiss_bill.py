# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swiss_Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('swiss_bill_score', models.IntegerField(default=0, verbose_name='Кол-во очков по швец. системе')),
                ('swiss_bill_fio', models.OneToOneField(to='result.Bill')),
            ],
            options={
                'db_table': 'swiss_bill',
                'verbose_name': 'Список участников',
                'verbose_name_plural': 'Список участников',
            },
            bases=(models.Model,),
        ),
    ]
