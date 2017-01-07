from django.contrib import admin

# Register your models here.
from .models import Moment

class MomentAdmin(admin.ModelAdmin):
	empty_value_display = "Empty"
	
class MyAdminSite(admin.AdminSite):
	site_header = 'Hello,World!'

admin_site = MyAdminSite()
admin_site.register(Moment,MomentAdmin)