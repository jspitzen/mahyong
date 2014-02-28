from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone

from mahyong_game.models import *

class IndexView(generic.ListView):
    template_name = 'mahyong_game/index.html'
    context_object_name = 'games'

    def get_queryset(self):
        """Return all active games"""
        return Game.objects.all()

class GameDetailView(generic.DetailView):
    model = Game
    context_object_name = 'object_set'

    def get_context_data(self, **kwargs):
        context = {}
        context['menu']   = Game.objects.all()
        context['active'] = super(GameDetailView, self).get_context_data(**kwargs)
        context['now']    = timezone.now()
        return context
