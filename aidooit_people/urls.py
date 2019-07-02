"""Main urls file for aidooit_people."""
from django.urls import path
from . import views

app_name = 'aidooit_people'
urlpatterns = [
    path('', views.people_index, name='people_index'),
    path('<int:person_id>/', views.person_details, name='person_details'),

]
