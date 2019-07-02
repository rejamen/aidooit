"""Main urls file for aidooit_people."""
from django.urls import path
from . import views

app_name = 'aidooit_people'
urlpatterns = [
    path('', views.IndexView.as_view(), name='people_index'),
    path('<int:pk>/', views.DetailView.as_view(), name='person_detail'),
]
