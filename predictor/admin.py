from django.contrib import admin
from predictor.models import *


class GameAdmin(admin.ModelAdmin):
	list_display=('team_a','team_b','match_date','goals_a','goals_b')
	ordering = ('match_date',)

class PredictionAdmin(admin.ModelAdmin):
	list_display=('user','game','predict_a','predict_b','points_awarded')


class UserInfoAdmin(admin.ModelAdmin):
	list_display = ('user','keyphrase','paid')

admin.site.register(Game,GameAdmin)
admin.site.register(Prediction,PredictionAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
