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
    swiss_rivel = models.CharField(blank=True, null=True, max_length=50, verbose_name='Rivel list')

    def __str__(self):
        return "%s" % self.bill_fio




class Couples_List(models.Model):
    class Meta:
        db_table = "couples_list"
        verbose_name = "Couples_list"
        verbose_name_plural = "Couples_lists"

    couples_list = models.CharField(max_length=1000, verbose_name='Couples list')

    def __str__(self):
        return self.couples_list
