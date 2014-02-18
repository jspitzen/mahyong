from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse

from mahyong_game.models import *

class IndexView(generic.ListView):
    template_name = 'mahyong_game/index.html'
    context_object_name = 'active_games'

    def get_queryset(self):
        """Return all active games"""
        return Game.objects.all()
