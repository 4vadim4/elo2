# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Bill


class AddData(ModelForm):
    class Meta:
        model = Bill
        fields = ['bill_fio', 'bill_elo', 'bill_kol_igr']


#    list_fio = forms.CharField(max_length=50)
#    list_elo = forms.IntegerField()
#    list_koef = forms.IntegerField()
