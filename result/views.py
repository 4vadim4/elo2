from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from .models import Bill
from .forms import AddData
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.urlresolvers import reverse
import random
from itertools import zip_longest
import re

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


def swiss(request):
    add_data = AddData
    args = {}
    args.update(csrf(request))
    args['index'] = Bill.objects.all()

 #   args['swiss_data'] = Swiss_Bill.objects.all()
#    args['form'] = add_data
    args['username'] = auth.get_user(request).username


    nov_por = Bill.objects.filter().order_by('-bill_mat_ozh')


    a = nov_por.count() // 2
    nov_por_1 = (nov_por[:a])
    nov_por_2 = (nov_por[a:])

    res_1 = [(nov_por_1[n].bill_fio) for n in range(nov_por_1.count()) if nov_por_1[n] in nov_por_1]
    res_2 = [(nov_por_2[n].bill_fio) for n in range(nov_por_2.count()) if nov_por_2[n] in nov_por_2]
    players = zip_longest(res_1, res_2)


#, fillvalue='-'

    args['res_1'] = res_1
    args['res_2'] = res_2
    args['players'] = players


    return render_to_response('swiss.html', args)


 #   import pdb; pdb.set_trace()
def first_step(request):
    game_data = request.POST
    for key, value in game_data.items():
        print(key, ' ', value)
        if key == 'csrfmiddlewaretoken':
            print('csrfmiddlewaretoken')

        elif value == 'no':
            split_player = key.split(', ')
            for player in split_player:
                player_name = re.sub(r'[^\w\s-]+', r'', player).strip()

                standoff = Bill.objects.get(bill_fio = player_name)
                standoff.swiss_bill_score = standoff.swiss_bill_score + 0.5
                standoff.save()

        else:
            bill = Bill.objects.get(bill_fio = value)
            bill.swiss_bill_score = bill.swiss_bill_score + 1
            bill.save()

    swiss_players = Bill.objects.all().order_by('-swiss_bill_score')
    new_game = swiss_players.count() // 2
    new_group_1 = (swiss_players[:new_game])
    new_group_2 = (swiss_players[new_game:])

    result_1 = [(new_group_1[n].bill_fio) for n in range(new_group_1.count()) if new_group_1[n] in new_group_1]
    result_2 = [(new_group_2[n].bill_fio) for n in range(new_group_2.count()) if new_group_2[n] in new_group_2]
    players = zip_longest(result_1, result_2)


    return render_to_response('swiss_result.html', {'swiss_players':swiss_players,
                                                    'players':players}, context_instance=RequestContext(request))



def porjadok():

    nov_por = Bill.objects.filter().order_by('bill_elo')

    a = nov_por.count() // 2
    nov_por_1 = (nov_por[:a])
    nov_por_2 = (nov_por[a:])
    count_nov_por_2 = nov_por_2.count()


