from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.list_files, name='list_files'),
    url(r'^viewlog/(?P<sortmethod>.*?)/(?P<filename>.*?)/$', views.view_log, name='view_log'),
]
