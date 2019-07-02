"""Core views for aidooit people."""
from django.shortcuts import get_object_or_404, render

from .models import Person


def index(request):
    """Home page for aidooit people."""
    people_list = Person.objects.order_by('name')[:10]
    template = 'aidooit_people/index.html'
    context = {
        'people_list': people_list,
    }
    return render(request, template, context)


def person_details(request, person_id):
    """View with people details."""
    person = get_object_or_404(Person, pk=person_id)
    template = 'aidooit_people/person_details.html'
    context = {
        'person': person,
    }
    return render(request, template, context)
