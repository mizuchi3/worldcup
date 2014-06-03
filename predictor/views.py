from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum
from django.core.mail import send_mail
from django.core.urlresolvers import resolve
from django.db import transaction
from django.db.transaction import commit_on_success
from predictor.models import *
import string,random,datetime

import time

def register(request):
	registered = False
	if request.method == 'POST':
		email = request.POST.get("email")
                if len(email)<10:
			return render(request, 'register.html', {'registered':registered})

		newid = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
		u = User.objects.get_or_create(username=email)
		userinfo,created = UserInfo.objects.get_or_create(user=u[0])
		userinfo.keyphrase = newid
		userinfo.save()
		registered = True
		send_mail('bc2_geeks World Cup 2014',
		 """Thanks for registering for bc2_geeks World Cup 2014 Predictions!

You will need to use the following link to make your predictions, if you feel
you need to reset the link, just visit the registration page again.

http://bc2-login04.bc2.unibas.ch:8014/games/%s

""" % (newid),
		  'bc2_geeks@unibas.ch',
		  [email],
		  fail_silently=False)

	return render(request, 'register.html', {'registered':registered})


def predict(request,userid=None):
	user = None
	userinfo = UserInfo.objects.filter(keyphrase=userid)
	keyphrase = None
	predictions=None
	dtime = timezone.now()#+ datetime.timedelta(days=13)
	games = Game.objects.all().order_by('match_date')
	updates_made = False
	a = int(time.time()*1000)
	if userinfo.count()==1:
		request.session['userid'] = userid
		user = userinfo[0].user
		if request.method=='POST':
			user = userinfo[0].user
			#with transaction.commit_on_success():
			for key in request.POST.keys():
				if key.endswith('_a'):
					g_id = key[4:key.find('_')]
					bkey = 'game%s_b' % g_id
					game = games.get(id=g_id)
					if dtime < game.match_date:
						prediction = Prediction.objects.get_or_create(user=user,
							game=game)[0]
						prediction.predict_a = request.POST.get(key)
						prediction.predict_b = request.POST.get(bkey)
						prediction.save()
						updates_made = True

	#print  int(time.time()*1000) -a
	a = int(time.time()*1000)
	predictions = Prediction.objects.filter(user=user)
	allpredictions = Prediction.objects.all()
	for game in games:
		p = predictions.filter(game=game)
		ap = allpredictions.filter(game=game).exclude(user=user)
		if p.count()==1:
			game.prediction = p[0]
		game.open = user is not None and game.match_date > dtime
	 	game.allpredictions = ap
	#print int(time.time()*1000) -a
	return render(request, 'predictions.html', {'user':user,'games':games, 'updates_made':updates_made})

def scores(request):
	predictions = Prediction.objects.filter(points_awarded__isnull=True)
	for p in predictions:
		if p.game.goals_a is None or p.game.goals_b is None:
			continue
		s = 0
		if p.predict_a==p.game.goals_a:
			s += 2
		if p.predict_b==p.game.goals_b:
			s += 2
		if p.predict_a>p.predict_b and p.game.goals_a>p.game.goals_b:
			s+=3
		if p.predict_b>p.predict_a and p.game.goals_b>p.game.goals_a:
			s+=3
		if p.predict_a==p.predict_b and p.game.goals_a==p.game.goals_b:
			s+=3

		p.points_awarded = s
		p.save()

	users = User.objects.annotate(points=Sum('prediction__points_awarded')).order_by('-points')

	userid = ''
	if 'userid' in request.session.keys():
		userid = request.session['userid']

	return render(request, 'scores.html', {'users':users,'userid':userid})




