from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone

from mahyong_game.models import *
from mahyong_game.utils import *

class IndexView(generic.ListView):
    template_name = 'mahyong_game/index.html'

    def get_queryset(self):
        """Return all active games"""
        return Game.objects.all()

class GameDetailView(generic.DetailView):
    model = Game
    template_name = 'mahyong_game/game_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Game.objects.all()
        return super(generic.DetailView, self).get_context_data(**kwargs)
