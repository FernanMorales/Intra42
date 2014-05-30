from django.conf.urls import patterns, include, url
from ticket_engine import views

urlpatterns = patterns('',
    url(r'^$', views.accueil, name='accueil'),
    url(r'^(?P<ticket_id>\d+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create_ticket, name='create'),
)