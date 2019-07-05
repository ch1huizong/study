from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_files, name='list_files'),
    path('viewlog/<str:sortmethod>/<str:filename>/', views.view_log, name='view_log'),
]
