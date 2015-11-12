from django.shortcuts import render, render_to_response, redirect
from django.shortcuts import render_to_response, redirect
from .models import Bill
from .forms import AddData
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.urlresolvers import reverse
import random


def welcome(request):
        return render_to_response('welcome.html')


def index(request):
#    import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = AddData(request.POST)
        if form.is_valid():
            fio = form.cleaned_data['bill_fio']
            elo = form.cleaned_data['bill_elo']
            kol_igr = random.randint(0, 100)
            if kol_igr <= 30:
                koe = 40
            elif kol_igr > 30 and elo >= 2400:
                koe = 10
            else:
                koe = 20
            elo2 = elo + 10
            import pdb; pdb.set_trace()
            bill = Bill.objects.create(bill_fio=fio, bill_elo=elo, bill_koef=koe, bill_mat_ozh=elo2)

#            import pdb; pdb.set_trace()
            bill.save()

            return redirect('index/')

    else:
#        add_data = AddData
#        args = {}
#        args.update(csrf(request))
#        args['index'] = Bill.objects.all()
#        args['form'] = add_data
#        args['username'] = auth.get_user().username

#        return render_to_response('result.html', args)
         pass

    add_data = AddData
    args = {}
    args.update(csrf(request))
    args['index'] = Bill.objects.all()
    args['form'] = add_data
    args['username'] = auth.get_user(request).username
    return render_to_response('result.html', args)

def elo(request):
        arg = {}
        arg.update(csrf(request))
        arg['elo_data'] = Bill.objects.all()
        arg['username'] = auth.get_user(request).username
        return render_to_response('result2.html', arg)

def add_res(request):

    if request.method == 'POST':
        form2 = request.POST
        y4astnik1 = form2['select1']
        resultat1 = form2['option1']
        if resultat1 == 'a1':
            res_igri1 = 1
        elif resultat1 == 'a2':
            res_igri1 = 0.5
        elif resultat1 == 'a3':
            res_igri1 = 0
        y4astnik2 = form2['select2']
        resultat2 = form2['option2']
        if resultat2 == 'b1':
            res_igri2 = 1
        elif resultat2 == 'b2':
            res_igri2 = 0.5
        elif resultat2 == 'b3':
            res_igri2 = 0


        EA = 1 / (1 + 10 ** ((Bill.objects.get(bill_fio=y4astnik2).bill_elo - Bill.objects.get(bill_fio=y4astnik1).bill_elo) / 400))

        if Bill.objects.get(bill_fio=y4astnik1).bill_kol_igr > 30 and Bill.objects.get(bill_fio=y4astnik1).bill_elo >= 2400:
            K = 10
        elif Bill.objects.get(bill_fio=y4astnik1).bill_kol_igr > 30 and Bill.objects.get(bill_fio=y4astnik1).bill_elo < 2400:
            K = 20
        elif Bill.objects.get(bill_fio=y4astnik1).bill_kol_igr <= 30:
            K = 40

        RAnew = round(Bill.objects.get(bill_fio=y4astnik1).bill_elo + K * (res_igri1 - EA), 2)
        new_RAnew = Bill.objects.get(bill_fio=y4astnik1)
        print(new_RAnew)
        new_RAnew.bill_elo = RAnew
        new_RAnew.save()

        EB = 1 / (1 + 10 ** ((Bill.objects.get(bill_fio=y4astnik1).bill_elo - Bill.objects.get(bill_fio=y4astnik2).bill_elo) / 400))

        if Bill.objects.get(bill_fio=y4astnik2).bill_kol_igr > 30 and Bill.objects.get(bill_fio=y4astnik2).bill_elo >= 2400:
            K = 10
        elif Bill.objects.get(bill_fio=y4astnik2).bill_kol_igr > 30 and Bill.objects.get(bill_fio=y4astnik2).bill_elo < 2400:
            K = 20
        elif Bill.objects.get(bill_fio=y4astnik2).bill_kol_igr <= 30:
            K = 40

        RBnew = round(Bill.objects.get(bill_fio=y4astnik2).bill_elo + K * (res_igri2 - EB), 2)
        new_RBnew = Bill.objects.get(bill_fio=y4astnik2)
        new_RBnew.bill_elo = RBnew
        new_RBnew.save()




        print(EA, RAnew)
        print(EB, RBnew)
#        return render_to_response('result2.html')

    arg = {}
    arg.update(csrf(request))
    arg['elo_data'] = Bill.objects.all()
    arg['username'] = auth.get_user().username

    return render_to_response('result2.html', arg)
