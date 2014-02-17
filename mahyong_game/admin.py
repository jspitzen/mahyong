from django.contrib import admin

from mahyong_game.models import Player, Family, Game, Round, PlayerRound

class PlayerRoundInline(admin.StackedInline):
    model = PlayerRound
    extra = 0

class RoundInline(admin.TabularInline):
    model = Round

class PlayerAdmin(admin.ModelAdmin):
    inlines = [PlayerRoundInline]

class GameAdmin(admin.ModelAdmin):
    inlines = [RoundInline]

# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Family)
admin.site.register(Game, GameAdmin)
admin.site.register(Round)
admin.site.register(PlayerRound)
