from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^survey/create$', views.create),
    url(r'^submit$', views.submit),
    url(r'^survey/goback$', views.goback),
    url(r'^reset$', views.reset)
]