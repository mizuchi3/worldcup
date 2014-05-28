from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^predict/(?P<userid>[\w]{6})/?$', 'predictor.views.predict'),
    url(r'^register/?$','predictor.views.register'),
)
