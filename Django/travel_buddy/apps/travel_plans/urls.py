from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    # url(r'^logout$', views.logout),
    # url(r'^homepage$', views.homepage),
    # url(r'^destination/(?P<trip_id>\d+)$', views.trip),
    # url(r'^add$', views.add),
    # url(r'^process$', views.process),
]