from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json

def jsonData(request):
     if request.method == 'GET':
          data = {'a':'hello,json'}
          return HttpResponse(json.dumps(data))
