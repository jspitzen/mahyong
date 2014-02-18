from django.conf.urls import patterns, url

from mahyong_game import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
)
