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
	dtime = timezone.now()+ datetime.timedelta(days=10)
	games = Game.objects.all().order_by('match_date')
	updates_made = False
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

	predictions = Prediction.objects.filter(user=user)
	allpredictions = Prediction.objects.all()
	endtime =  "2014-06-28"#"2014-07-04""2014-07-08""2014-07-10""2014-07-13"
	for game in games:
		p = predictions.filter(game=game)
		ap = allpredictions.filter(game=game).exclude(user=user)
		if p.count()==1:
			game.prediction = p[0]
			game.outcome = outcome(p[0].predict_a,p[0].predict_b,game.goals_a,game.goals_b)

		for pp in ap:
			pp.outcome = outcome(pp.predict_a,pp.predict_b,game.goals_a,game.goals_b)
		game.open = user is not None and dtime < game.match_date and game.match_date.strftime('%Y-%m-%d') < endtime 
	 	game.allpredictions = ap
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

		if outcome(p.predict_a,p.predict_b,p.game.goals_a,p.game.goals_b):
			s+=3
	
		p.points_awarded = s
		p.save()

	users = User.objects.annotate(points=Sum('prediction__points_awarded')).order_by('-points')

	userid = ''
	if 'userid' in request.session.keys():
		userid = request.session['userid']

	return render(request, 'scores.html', {'users':users,'userid':userid})

def outcome(pA,pB,gA,gB):

	if pA is None or pB is None or gA is None or gB is None:
		return None
	if pA>pB and gA>gB:
		return True
	if pB>pA and gB>gA:
		return True
	if pA==pB and gA==gB:
		return True

	return False



