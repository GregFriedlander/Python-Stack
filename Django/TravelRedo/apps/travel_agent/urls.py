from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^homepage$', views.homepage),
    url(r'^add$', views.add),
    url(r'^join/(?P<trip_id>\d+)$', views.join),
    url(r'^processtrip$', views.processtrip),
    url(r'^destination/(?P<trip_id>\d+)$', views.trip),
]
    
