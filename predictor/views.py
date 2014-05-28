from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from predictor.models import *


def register(request):
	return render(request, 'register.html', {})

def predict(request,userid):
	user = User.objects.filter(username=userid)
	games = Game.objects.all()
	return render(request, 'predictions.html', {'valid_user':user.count()!=1,
												'games':games})