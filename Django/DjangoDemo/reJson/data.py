from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json

def jsonData(request):
    if request.method == 'GET':
        data = {'data':{'needCache':True,'content':"var alertView = require('UIAlertView').alloc().init();alertView.setTitle('Alert');alertView.setMessage('AlertView from js AirChen');alertView.addButtonWithTitle('OK');alertView.show();"}}
        return HttpResponse(json.dumps(data))
