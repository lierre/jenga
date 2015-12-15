from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'www.views.home', name='home'),
                       url(r'^mail/', 'www.views.mail_team', name='mail-team'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
