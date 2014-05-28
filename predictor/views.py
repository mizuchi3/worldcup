from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from predictor.models import *
import string,random


def register(request):
	if request.method == 'POST':
		email = request.POST.get("email")
		newid = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
		u = User.objects.get_or_create(username=email)
		userinfo,created = UserInfo.objects.get_or_create(user=u[0])
		userinfo.keyphrase = newid
		userinfo.save()
		return redirect('/games/'+newid)

	return render(request, 'register.html', {})

def predict(request,userid=None):
	user = None
	userinfo = UserInfo.objects.filter(keyphrase=userid)
	keyphrase = None
	predictions=None
	games = Game.objects.all()
	if userinfo.count()==1:
		user = userinfo[0].user
		if request.method=='POST':
			user = userinfo[0].user
			for key in request.POST.keys():
				if key.endswith('_a'):
					g_id = key[4:key.find('_')]
					bkey = 'game%s_b' % g_id
					game = Game.objects.get(id=g_id)
					prediction = Prediction.objects.get_or_create(user=user,
								game=game)[0]
					prediction.predict_a = request.POST.get(key)
					prediction.predict_b = request.POST.get(bkey)
					prediction.save()

		predictions = Prediction.objects.filter(user=user)
		for game in games:
			p = predictions.filter(game=game)
			if p.count()==1:
				game.prediction = p[0]
	
	return render(request, 'predictions.html', {'user':user,'games':games})