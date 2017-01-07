#!/usr/bin/python

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^moment_input',views.moment_input),
	url(r'^view',views.welcome,name = 'welcome'),
]