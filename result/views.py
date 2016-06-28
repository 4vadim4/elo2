from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from .models import Bill, Couples_List
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


        resultat1 = form2['player1']


        if resultat1 == 'win':
            res_igri1 = 1
        elif resultat1 == 'standoff':
            res_igri1 = 0.5
        elif resultat1 == 'loss':
            res_igri1 = 0
        y4astnik2 = form2['select2']
        resultat2 = form2['player2']
        if resultat2 == 'win':
            res_igri2 = 1
        elif resultat2 == 'standoff':
            res_igri2 = 0.5
        elif resultat2 == 'loss':
            res_igri2 = 0


        Expect_A = 1 / (1 + 10 ** ((Bill.objects.get(bill_fio=y4astnik2).bill_elo - Bill.objects.get(bill_fio=y4astnik1).bill_elo) / 400))

        if Bill.objects.get(bill_fio=y4astnik1).bill_kol_igr > 30 and Bill.objects.get(bill_fio=y4astnik1).bill_elo >= 2400:
            K = 10
        elif Bill.objects.get(bill_fio=y4astnik1).bill_kol_igr > 30 and Bill.objects.get(bill_fio=y4astnik1).bill_elo < 2400:
            K = 20
        elif Bill.objects.get(bill_fio=y4astnik1).bill_kol_igr <= 30:
            K = 40

#        print(Bill.objects.get(bill_fio=y4astnik1), '  ', K, '  ', res_igri1)



        Rating_A_new = round(Bill.objects.get(bill_fio=y4astnik1).bill_elo + K * (res_igri1 - Expect_A), 1)
#        print(Rating_A_new)

        rating_A = Bill.objects.get(bill_fio=y4astnik1)
#        print(type(rating_A))
#        print(rating_A)

        rating_A.bill_elo = 300
#        print(type(rating_A))

        rating_A.save()

#        print(Bill.objects.filter(bill_fio=y4astnik1))

        Expect_B = 1 / (1 + 10 ** ((Bill.objects.get(bill_fio=y4astnik1).bill_elo - Bill.objects.get(bill_fio=y4astnik2).bill_elo) / 400))

        if Bill.objects.get(bill_fio=y4astnik2).bill_kol_igr > 30 and Bill.objects.get(bill_fio=y4astnik2).bill_elo >= 2400:
            K = 10
        elif Bill.objects.get(bill_fio=y4astnik2).bill_kol_igr > 30 and Bill.objects.get(bill_fio=y4astnik2).bill_elo < 2400:
            K = 20
        elif Bill.objects.get(bill_fio=y4astnik2).bill_kol_igr <= 30:
            K = 40

        Rating_B_new = round(Bill.objects.get(bill_fio=y4astnik2).bill_elo + K * (res_igri2 - Expect_B), 1)
        rating_B = Bill.objects.get(bill_fio=y4astnik2)
        rating_B.bill_elo = Rating_B_new
        rating_B.save()



    arg = {}
    arg.update(csrf(request))
    arg['elo_data'] = Bill.objects.all()
#    arg['username'] = auth.get_user().username

    return render_to_response('result2.html', arg, context_instance=RequestContext(request))


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

    for rw_player in players:
        spisok = []
        for one_rw_player in rw_player:
            if one_rw_player == None:
                pass
            else:

                rw_player_name = re.sub(r'[^\w\s-]+', r'', one_rw_player).strip()
                rw_player_id = Bill.objects.get(bill_fio = rw_player_name).id
                spisok.append(rw_player_id)
                spisok.sort()
        print(spisok)
        length = len(spisok)

        if length == 2:
            rival_1 = Bill.objects.get(id = spisok[0])
            rival_2 = Bill.objects.get(id = spisok[1])
            rival_1.swiss_rivel = spisok[1]
            rival_2.swiss_rivel = spisok[0]
            rival_1.save()
            rival_2.save()
        else:
            pass



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

    id_new_group_1 = []
    id_new_group_2 = []

    for n1 in new_group_1:
        igrok = Bill.objects.get(bill_fio = n1)
        id_igrok = igrok.id
        id_new_group_1.append(id_igrok)

    for n2 in new_group_2:
        igrok = Bill.objects.get(bill_fio = n2)
        id_igrok = igrok.id
        id_new_group_2.append(id_igrok)

    for single_id in id_new_group_1:
        result = [single_id, random.choice(id_new_group_2)]
#        print(result, 'начальный')
#        print('игрок - ', result[0], 'уже играл с ', Bill.objects.get(id=result[0]).swiss_rivel,  'сейчас играет с ', result[1])

        if Bill.objects.get(id=result[0]).swiss_rivel is not None:
            while str(result[1]) in Bill.objects.get(id=result[0]).swiss_rivel:
                result = [single_id, random.choice(id_new_group_2)]
                break
        else:
            result = [single_id, random.choice(id_new_group_2)]


#        while Bill.objects.get(id=result[0]).swiss_rivel is not None and str(result[1]) in Bill.objects.get(id=result[0]).swiss_rivel:
#                result = [single_id, random.choice(id_new_group_2)]
#                break


#        if (str(result[1])) in Bill.objects.get(id=result[0]).swiss_rivel:
#            print('True')
#        else:
#            print('False')
#            while (str(result[1]) + ',') in Bill.objects.get(id=result[0]).swiss_rivel:
 #               result = [single_id, random.choice(id_new_group_2)]

#        while ' result[1],' in Bill.objects.get(id=result[0]).swiss_rivel:
#            result = [k, random.choice(id_new_group_2)]
#            print(result, 'пробный')
        id_new_group_2.remove(result[1])
        print(result, 'конечный')
    print(id_new_group_2)

#    print(id_new_group_1)
#    print(id_new_group_2)

#    print(random.choice(id_new_group_1))



#    print(new_group_2)
'''
    result_1 = [(new_group_1[n].bill_fio) for n in range(new_group_1.count()) if new_group_1[n] in new_group_1]
    result_2 = [(new_group_2[n].bill_fio) for n in range(new_group_2.count()) if new_group_2[n] in new_group_2]
    players = zip_longest(result_1, result_2)



    for pl in players:
        if None not in pl:
            w_pl = []
            for p in pl:

                igrok = Bill.objects.get(bill_fio = p)
                id_igrok = igrok.id

                print(p, ' - это вывод !')



    return render_to_response('swiss_result.html', {'swiss_players':swiss_players,
                                                    'players':players}, context_instance=RequestContext(request))

'''

def porjadok():

    nov_por = Bill.objects.filter().order_by('bill_elo')

    a = nov_por.count() // 2
    nov_por_1 = (nov_por[:a])
    nov_por_2 = (nov_por[a:])
    count_nov_por_2 = nov_por_2.count()


