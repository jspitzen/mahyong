from django.conf.urls import patterns, url

from mahyong_game import views

urlpatterns = patterns('',
    url(r'^game/(?P<pk>\d+)/$', views.GameDetailView.as_view(), name='index'),
    url(r'^player/(?P<pk>\d+)/$', views.PlayerDetailView.as_view(), name='index'),
    url(r'^$', views.GameIndexView.as_view(), name='index'),
    url(r'^game/$', views.GameIndexView.as_view(), name='index'),
    url(r'^player/$', views.PlayerIndexView.as_view(), name='index'),
)
