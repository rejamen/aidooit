"""Core views for aidooit people."""
from django.shortcuts import get_object_or_404, render
from django.views import generic

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
    template_name = 'aidooit_people/person_detail.html'
