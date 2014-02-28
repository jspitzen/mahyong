from django.conf.urls import patterns, url

from mahyong_game import views

urlpatterns = patterns('',
    url(r'^game/(?P<pk>\d+)/$', views.GameDetailView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
)
