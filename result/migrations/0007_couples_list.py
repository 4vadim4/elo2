# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0006_auto_20160615_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Couples_List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('couples_list', models.CharField(max_length=1000, verbose_name='Couples list')),
            ],
            options={
                'db_table': 'couples_list',
                'verbose_name': 'Couples_list',
                'verbose_name_plural': 'Couples_lists',
            },
            bases=(models.Model,),
        ),
    ]
