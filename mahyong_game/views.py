from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone

from mahyong_game.models import *
from mahyong_game.utils import *

class GameIndexView(generic.ListView):
    template_name = 'mahyong_game/game_index.html'

    def get_queryset(self):
        """Return all active games"""
        return Game.objects.all()

class PlayerIndexView(generic.ListView):
    template_name = 'mahyong_game/player_index.html'

    def get_queryset(self):
        """Return all players"""
        return Player.objects.all()

class GameDetailView(generic.DetailView):
    model = Game
    template_name = 'mahyong_game/game_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Game.objects.all()
        return super(generic.DetailView, self).get_context_data(**kwargs)

class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'mahyong_game/player_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Player.objects.all()
        return super(generic.DetailView, self).get_context_data(**kwargs)
