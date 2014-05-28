from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^games/(?P<userid>[\w]+)?/?$', 'predictor.views.predict'),
    url(r'^register/?$','predictor.views.register'),
)
