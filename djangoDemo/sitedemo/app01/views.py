# coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

import os
from app01.forms import MomentForm
from django.core.urlresolvers import reverse

def moment_input(req):
	if req.method == 'POST':
		form = MomentForm(req.POST)
		if form.is_valid():
			moment = form.save()
			moment.save()
			return HttpResponseRedirect(reverse('welcome'))
	else:
		form = MomentForm()
	
	PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	return render(req, os.path.join(PROJECT_ROOT, 'app01/templates','moments_input.html'), {'form':form})
	#数据渲染HTML
	
def welcome(req):
	return HttpResponse('<h1>Welcome to my tiny twitter!</h1>')#直接构造HTML