from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    team_a = models.CharField(max_length=65)
    team_b = models.CharField(max_length=65)
    match_date = models.DateTimeField()
    goals_a = models.IntegerField(null=True,blank=True)
    goals_b = models.IntegerField(null=True,blank=True)
    def __unicode__(self):
		return '%s v %s' %(self.team_a,self.team_b)
    class Meta:
        db_table = 'games'

class Prediction(models.Model):
	user = models.ForeignKey(User)
	game = models.ForeignKey(Game)
	predict_a = models.IntegerField(default=0)
	predict_b = models.IntegerField(default=0)
	points_awarded = models.FloatField(null=True,blank=True)
	class Meta:
		db_table = 'predictions'

class UserInfo(models.Model):
	user = models.ForeignKey(User, unique=True)
	paid = models.BooleanField(default=False)
	keyphrase = models.CharField(max_length=12,unique=True)
	class Meta:
		db_table = 'userinfo'


