from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views
urlpatterns = [
  	path('', views.index, name = 'index'),
  	url(r'^details/(?P<id>\w{0,50})/$', views.details),
  	path('add', views.add, name = 'add'),
    #path('details/(?P<id>\w{0,50}/)', views.details)
]