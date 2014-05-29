from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
	name = models.CharField(max_length=65)
	team = models.CharField(max_length=65,default=None,blank=True)
	def __unicode__(self):
		return '%s (%s)' %(self.name,self.team)
	class Meta:
		db_table = 'players'


class Game(models.Model):
    team_a = models.CharField(max_length=65)
    team_b = models.CharField(max_length=65)
    odds_a_win = models.FloatField(null=True,blank=True)
    odds_b_win = models.FloatField(null=True,blank=True)
    odds_draw = models.FloatField(null=True,blank=True)
    match_date = models.DateTimeField()
    goals_a = models.IntegerField(null=True,blank=True)
    goals_b = models.IntegerField(null=True,blank=True)
    scorer = models.ManyToManyField(Player,through='GoalCount',default=None,blank=True)
    def __unicode__(self):
		return '%s v %s' %(self.team_a,self.team_b)
    class Meta:
        db_table = 'games'

class GoalCount(models.Model):
	player = models.ForeignKey(Player)
	game = models.ForeignKey(Game)
	goals_scored = models.IntegerField(default=0)

class Prediction(models.Model):
	user = models.ForeignKey(User)
	game = models.ForeignKey(Game)
	predict_a = models.IntegerField(default=0)
	predict_b = models.IntegerField(default=0)
	points_awarded = models.FloatField(null=True,blank=True)
	class Meta:
		db_table = 'predictions'

class BestPlayer(models.Model):
	user = models.ForeignKey(User)
	player = models.ForeignKey(Player)
	class Meta:
		db_table = 'bestplayer'

class UserInfo(models.Model):
	user = models.ForeignKey(User, unique=True)
	paid = models.BooleanField(default=False)
	keyphrase = models.CharField(max_length=12,unique=True)
	class Meta:
		db_table = 'userinfo'


