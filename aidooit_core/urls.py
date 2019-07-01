"""Main urls file for aidooit."""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]
