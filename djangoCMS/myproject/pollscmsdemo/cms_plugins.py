#!/usr/bin/python

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from pollscmsdemo.models import PollPluginModel
from django.utils.translation import ugettext as _


class PollPluginPublisher(CMSPluginBase):
	model = PollPluginModel  # model where plugin data are saved
	module = _("Polls")
	name = _("Poll Plugin")  # name of the plugin in the interface
	render_template = "pollscmsdemo/poll_plugin.html"

	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context

plugin_pool.register_plugin(PollPluginPublisher)  # register the plugin