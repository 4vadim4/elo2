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
import copy

def welcome(request):
        return render_to_response('welcome.html')

def logout(request):
    auth.logout(request)
#    return redirect('/')
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
            bill.save()

            return redirect('index/')

    else:

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


        Rating_A_new = round(Bill.objects.get(bill_fio=y4astnik1).bill_elo + K * (res_igri1 - Expect_A), 1)
        rating_A = Bill.objects.get(bill_fio=y4astnik1)
        rating_A.bill_elo = Rating_A_new
        rating_A.bill_kol_igr = rating_A.bill_kol_igr + 1
        rating_A.save()


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
        rating_B.bill_kol_igr = rating_B.bill_kol_igr + 1
        rating_B.save()



    arg = {}
    arg.update(csrf(request))
    arg['elo_data'] = Bill.objects.all()
#    arg['username'] = auth.get_user().username

    return render_to_response('result2.html', arg, context_instance=RequestContext(request))


def swiss(request):
    args = {}
    args.update(csrf(request))
    index = Bill.objects.all()
    args['index'] = Bill.objects.all()
    args['username'] = auth.get_user(request).username

    nov_por = Bill.objects.filter().order_by('-swiss_bill_score')

    a = nov_por.count() // 2
    nov_por_1 = (nov_por[:a])
    nov_por_2 = (nov_por[a:])

    res_1 = [(nov_por_1[n].bill_fio) for n in range(nov_por_1.count()) if nov_por_1[n] in nov_por_1]
    res_2 = [(nov_por_2[n].bill_fio) for n in range(nov_por_2.count()) if nov_por_2[n] in nov_por_2]
    players = zip_longest(res_1, res_2)

    res_couple = []
    for couple in players:
        res_couple.append(couple)



    return render_to_response('swiss.html', {'players':players, 'index':index, 'res_couple':res_couple, 'nov_por':nov_por},
                              context_instance=RequestContext(request))



def first_step(request):
#   select players from the dictionary and define points
    game_data = request.POST
    for key, value in game_data.items():
        if key == 'csrfmiddlewaretoken':
            pass

        elif value == 'no':
            split_player = key.split(', ')

            for player in split_player:
                player_name = re.sub(r'[^\w\s-]+', r'', player).strip()
                standoff = Bill.objects.get(bill_fio = player_name)
                standoff.swiss_bill_score = standoff.swiss_bill_score + 0.5
                standoff.bill_kol_igr = standoff.bill_kol_igr + 1
                standoff.save()

        else:
            bill = Bill.objects.get(bill_fio = value)
            bill.swiss_bill_score = bill.swiss_bill_score + 1
            bill.bill_kol_igr = bill.bill_kol_igr + 1
            bill.save()


    for key, value in game_data.items():
        if key == 'csrfmiddlewaretoken':
            pass
        else:

            if 'None' in key:
                pass
            else:
                # если найдена пара игроков
                spisok = []
                wr_split_player = key.split(', ')
                for rw_player in wr_split_player:
                    rw_player_name = re.sub(r'[^\w\s-]+', r'', rw_player).strip()
                    rw_player_id = Bill.objects.get(bill_fio = rw_player_name).id
                    spisok.append(rw_player_id)
                    spisok.sort()


                # записываем в переменную с кем игрок уже сыграл
                rival_1 = Bill.objects.get(id = spisok[0]).swiss_rivel

                if len(rival_1) == 0:
                    rival_1 = Bill.objects.get(id = spisok[0])
                    rival_1.swiss_rivel = spisok[1]
                    rival_1.save()
                else:
                    rival_1 = Bill.objects.get(id = spisok[0])
                    rival_1.swiss_rivel = str(rival_1.swiss_rivel) + ', ' + str(spisok[1])
                    rival_1.save()

                rival_2 = Bill.objects.get(id = spisok[1]).swiss_rivel

                if len(rival_2) == 0:
                    rival_2 = Bill.objects.get(id = spisok[1])
                    rival_2.swiss_rivel = spisok[0]
                    rival_2.save()
                else:
                    rival_2 = Bill.objects.get(id = spisok[1])
                    rival_2.swiss_rivel = str(rival_2.swiss_rivel) + ', ' + str(spisok[0])
                    rival_2.save()










    swiss_players = Bill.objects.all().order_by('-swiss_bill_score')
    new_game = swiss_players.count() // 2
    new_group_1 = (swiss_players[:new_game])
    new_group_2 = (swiss_players[new_game:])

    id_new_group_1 = []
    id_new_group_2 = []

    # формируем группу сильнейщих и слабейших, записываем их id
    for n1 in new_group_1:
        igrok = Bill.objects.get(bill_fio = n1)
        id_igrok = igrok.id
        id_new_group_1.append(id_igrok)

    for n2 in new_group_2:
        igrok = Bill.objects.get(bill_fio = n2)
        id_igrok = igrok.id
        id_new_group_2.append(id_igrok)

    # формируем след пару игроков, которые еще не играли друг с другом

    result_finish = []
    tmp_players = []

    for single_id in id_new_group_1:
        tmp_id_new_group_2 = copy.deepcopy(id_new_group_2)
        tmp_rival = []

        rival_data_1 = Bill.objects.get(id=single_id).swiss_rivel
        if not rival_data_1:
            for j in tmp_players:
                j = int(j)
                if j not in tmp_id_new_group_2:
                    continue
                tmp_id_new_group_2.remove(j)
            result = [single_id, random.choice(tmp_id_new_group_2)]
            tmp_players.append(result[1])
            result_2 = [str(Bill.objects.get(id=result[0])), str(Bill.objects.get(id=result[1]))]
            result_finish.append(result_2)
        else:
            rival_data_1 = re.split(r', ', rival_data_1)
            for i in rival_data_1:
                i = int(i)
                tmp_rival.append(i)
            tmp_rival.extend(tmp_players)
            for j in tmp_rival:
                j = int(j)
                if j not in tmp_id_new_group_2:
                    continue
                tmp_id_new_group_2.remove(j)

            if not tmp_id_new_group_2:
                return render_to_response('finish_play.html', {'swiss_players':swiss_players, 'result_finish':result_finish},
                              context_instance=RequestContext(request))


            result = [single_id, random.choice(tmp_id_new_group_2)]
            tmp_players.append(result[1])
            result_2 = [str(Bill.objects.get(id=result[0])), str(Bill.objects.get(id=result[1]))]
            result_finish.append(result_2)

    id_new_group_1.extend(tmp_players)

    for one in id_new_group_1:
        one = int(one)
        if one not in id_new_group_2:
            continue
        id_new_group_2.remove(one)
    if id_new_group_2:
        end_player = [None, str(Bill.objects.get(id=id_new_group_2[0]))]
        result_finish.append(end_player)


    return render_to_response('swiss_result.html', {'swiss_players':swiss_players, 'result_finish':result_finish},
                              context_instance=RequestContext(request))


def reset(request):
    Bill.objects.all().update(swiss_rivel='')
    return redirect('/index')
#    return render_to_response('index.html',
 #                             context_instance=RequestContext(request))



