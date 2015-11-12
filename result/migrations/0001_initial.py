# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_fio', models.CharField(max_length=50, verbose_name='ФИО')),
                ('bill_kol_igr', models.IntegerField(null=True, verbose_name='Сыгранных игр', blank=True)),
                ('bill_elo', models.IntegerField(null=True, verbose_name='Показатель ЭЛО', blank=True)),
                ('bill_koef', models.IntegerField(null=True, verbose_name='Коэфициент', blank=True)),
                ('bill_mat_ozh', models.IntegerField(null=True, verbose_name='Мат. ожидание кол. очков', blank=True)),
            ],
            options={
                'db_table': 'bill',
                'verbose_name': 'Список участников',
                'verbose_name_plural': 'Список участников',
            },
            bases=(models.Model,),
        ),
    ]
