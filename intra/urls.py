from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'intra.views.home', name='home'),
    url(r'^annuaire/$', 'annuaire.views.users', name='register'),
    url(r'^user/(?P<username>\w+)/$', 'profils.views.user_profile', name='detailed_profile'),

   	url(r'^login/$', 'ldaplogin.views.login_view'),
    url(r'^logout/$', 'ldaplogin.views.logout_view'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^planning/', 'planning.views.calendar'),
    url(r'^elearning/', 'elearning.views.home'),

    url(r'^ticket/', include('ticket_engine.urls')),



    url(r'^forum/$', 'forum.views.main'),
    url(r'^forum/(?P<c_name>[-\w]+)/$', 'forum.views.sub_category'),
    url(r'^forum/(?P<c_name>[-\w]+)/(?P<sc_name>[-\w]+)/$', 'forum.views.thread'),
    url(r'^forum/create/(?P<c>[-\w]+)/(?P<sc>[\w]+)/$', 'forum.views.create'),
    url(r'^forum/(?P<c_name>[-\w]+)/(?P<sc_name>[-\w]+)/(?P<t_name>[-\w ]+)/$', 'forum.views.post'),
    url(r'^forum/reply/(?P<c_name>[-\w]+)/(?P<sc_name>[\w]+)/(?P<t_name>[-\w ]+)/$', 'forum.views.reply'),
    url(r'^forum/register/thread/(?P<c_name>[-\w]+)/(?P<sc_name>[-\w]+)/$', 'forum.views.create_thread'),
)
