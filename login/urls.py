from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elo2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', 'login.views.login', name='login'),
    url(r'^logout/$', 'login.views.logout', name='logout'),

)
