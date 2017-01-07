#!/usr/bin/python

from django.forms import ModelForm
from app01.models import Moment

class MomentForm(ModelForm):
	class Meta:
		model = Moment
		fields = '__all__'