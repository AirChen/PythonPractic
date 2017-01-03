"""mysite01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog1 import views as blog_view
from add import views as add_view
from reJson import views as json_view
from reJson import data as json_data
from home import views as home_view

urlpatterns = [
    url(r'^$',blog_view.index),
    url(r'^admin/', admin.site.urls),
    url(r'^add/$',add_view.add),
    url(r'^add/(\d+)/(\d+)/$',add_view.add2),
    url(r'^json/$',json_view.jsonData),
    url(r'^json_data/$',json_data.jsonData),
    url(r'^home/$',home_view.home),
]
