from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feeds(request):
	return HttpResponse('<h1>Welcome Home View!</h1>')