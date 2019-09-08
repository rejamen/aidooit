"""Main urls file for aidooit_login."""
from django.urls import path
from . import views

app_name = 'aidooit_login'
urlpatterns = [
    path('', views.IndexView.as_view(), name='login_index'),
    path('<int:pk>/', views.DetailView.as_view(), name='login_details'),
]
