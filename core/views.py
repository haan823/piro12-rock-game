from random import choice

from django.shortcuts import redirect, render
from django.urls import reverse

from core.models import Game, User

CHOICE = ['Rock', 'Paper', 'Scissors']


def rps_list(request):
    games = Game.objects.all()
    user = request.user
    data = {
        'user': user,
        'games': games
    }
    return render(request, 'rps_list.html', data)

def play_user(request, pk):
    if request.method == 'POST':
        defender = request.POST.get('defender', None)
        atk_choice = request.POST.get('atk_choice', None)
        Game.objects.create(
            atk_user = User.objects.get(pk=pk),
            dfn_user = User.objects.get(pk=defender),
            atk_choice = atk_choice,
            dfs_choice = '',
            result = '진행중'
        )
        return redirect(reverse('rps_list'))
    elif request.method == 'GET':
        users = User.objects.all().exclude(name=request.user)
        user = User.objects.get(pk=pk),
        data = {
            'user': user,
            'users': users,
        }
        return render(request, 'rps_play.html', data)


def play_computer(request):
    pass