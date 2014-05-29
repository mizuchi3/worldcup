from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum
from django.core.mail import send_mail
from predictor.models import *
import string,random,datetime
from django.core.urlresolvers import resolve

def register(request):
	registered = False
	if request.method == 'POST':
		email = request.POST.get("email")
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

http://somewhere.com/games/%s

""" % (newid),
		  'bc2_geeks@unibas.ch',
		  [email],
		  fail_silently=True)

	return render(request, 'register.html', {'registered':registered})

def predict(request,userid=None):
	user = None
	userinfo = UserInfo.objects.filter(keyphrase=userid)
	keyphrase = None
	predictions=None
	dtime = timezone.now()#+ datetime.timedelta(days=18)
	games = Game.objects.all().order_by('match_date')
	updates_made = False
	if userinfo.count()==1:
		request.session['userid'] = userid
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
					updates_made = True

		predictions = Prediction.objects.filter(user=user)
		for game in games:
			p = predictions.filter(game=game)
			if p.count()==1:
				game.prediction = p[0]
			game.open = game.match_date > dtime
	
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




