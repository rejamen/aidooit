"""Core views for aidooit people."""
from django.views import generic
from rest_framework import generics
from .serializers import PersonSerializer

from .models import Person


class IndexView(generic.ListView):
    """Generic view for index."""

    template_name = 'aidooit_people/index.html'
    context_object_name = 'people_list'

    def get_queryset(self):
        """Return the list of people."""
        return Person.objects.order_by('name')


class DetailView(generic.DetailView):
    """Generic view for details."""

    model = Person
    #  by default it return an object named person (like model name)
    #  use context_object_name if you want specify other
    #  context_object_name = 'other_name'
    template_name = 'aidooit_people/person_detail.html'


class PersonList(generics.ListCreateAPIView):
    """List of people for API."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    """Person details for API."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
