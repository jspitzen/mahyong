from django.contrib import admin

from mahyong_game.models import Player, Family, Game, Round, PlayerRound

# Register your models here.
admin.site.register(Player)
admin.site.register(Family)
admin.site.register(Game)
admin.site.register(Round)
admin.site.register(PlayerRound)
