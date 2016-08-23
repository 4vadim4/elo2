from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elo2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'result.views.welcome', name='welcome'),
    url(r'^index/$', 'result.views.index', name='xindex'),
    url(r'^index/elo/$', 'result.views.elo', name='xelo'),
    url(r'^index/swiss/$', 'result.views.swiss', name='xswiss'),
    url(r'^index/swiss/first_step/$', 'result.views.first_step', name='first_step'),

    url(r'^logout/$', 'result.views.logout', name='logout'),
    url(r'^openlogin/$', 'django.contrib.auth.views.login', name='openlogin'),

    url(r'^index/add_res/', 'result.views.add_res', name='add_res'),

    url(r'^reset/$', 'result.views.reset', name='reset'),

)
