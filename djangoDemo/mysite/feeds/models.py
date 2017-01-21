from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Feed(models.Model):
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	post = models.TextField(max_length=255)
	parent = models.ForeignKey('Feed', null=True, blank=True)
	likes = models.IntegerField(default=0)
	comments = models.IntegerField(default=0)

	class Meta:
		verbose_name = _('Feed')
		verbose_name_plural = _('Feeds')
		ordering = ('-date',)

	def __str__(self):
		return self.post