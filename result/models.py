# -*- coding: utf-8 -*-
from django.db import models


class Bill(models.Model):
    class Meta:
        db_table = "bill"
        verbose_name = "Список участников"
        verbose_name_plural = "Список участников"


    bill_fio = models.CharField(max_length=50, verbose_name='ФИО')
    bill_kol_igr = models.IntegerField(blank=True, null=True, verbose_name='Сыгранных игр')
    bill_elo = models.FloatField(blank=True, null=True, verbose_name='Показатель ЭЛО')
    bill_koef = models.IntegerField(blank=True, null=True, verbose_name='Коэфициент')
    bill_mat_ozh = models.IntegerField(blank=True, null=True, verbose_name='Мат. ожидание кол. очков')
    swiss_bill_score = models.FloatField(default=0, verbose_name='Кол-во очков по швец. системе')

    def __str__(self):
        return self.bill_fio



"""
class Swiss_Bill(models.Model):
    class Meta:
        db_table = "swiss_bill"
        verbose_name = "Список участников Swiss sys"
        verbose_name_plural = "Список участников Swiss sys"

    user = models.OneToOneField(Bill)

    swiss_bill_score = models.IntegerField(default=0, verbose_name='Кол-во очков по швец. системе')

    def __str__(self):
        return self.swiss_bill_fio
"""