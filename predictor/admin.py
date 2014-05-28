from django.contrib import admin
from predictor.models import *

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name','team')


class ScorerInline(admin.TabularInline):
    model = GoalCount


class GameAdmin(admin.ModelAdmin):
	list_display=('team_a','team_b','odds_a_win','odds_b_win','odds_draw','match_date','goals_a','goals_b')
	inlines = [
        ScorerInline,
    ]

class PredictionAdmin(admin.ModelAdmin):
	list_display=('user','game','predict_a','predict_b','points_awarded')


class BestPlayerAdmin(admin.ModelAdmin):
	list_display = ('user', 'player')

class UserInfoAdmin(admin.ModelAdmin):
	list_display = ('user','keyphrase','paid')


admin.site.register(Player,PlayerAdmin)
admin.site.register(Game,GameAdmin)
admin.site.register(Prediction,PredictionAdmin)
admin.site.register(BestPlayer,BestPlayerAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
