"""Main urls file for aidooit_people."""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'aidooit_people'
urlpatterns = [
    path('', views.IndexView.as_view(), name='people_index'),
    path('<int:pk>/', views.DetailView.as_view(), name='person_detail'),
    path('api/', views.PersonList.as_view()),
    path('api/<int:pk>/', views.PersonDetail.as_view()),
]

# DRY way to refer to a specific file format for a URL endpoint.
# It means our API will be able to handle URls such as
# http://localhost/api/items/4.json rather than just
# http://localhost/api/items/4
urlpatterns = format_suffix_patterns(urlpatterns)
