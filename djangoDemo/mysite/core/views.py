from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from feeds.views import feeds
# Create your views here.

def home(request):
		if request.user.is_authenticated():
			return feeds(request) # -> redirect
		else:
			return HttpResponseRedirect(reverse('login'))