"""Main urls file for aidooit_access_point."""
from django.urls import path
from . import views

app_name = 'aidooit_access_point'
urlpatterns = [
    path('', views.IndexView.as_view(), name='aap_index'),
    path('<int:pk>/', views.DetailView.as_view(), name='aap_details'),
]
