"""Main urls file for aidooit."""
from django.urls import path
from . import views

app_name = 'aidooit_core'
urlpatterns = [
    path('', views.index, name='index'),
]
