"""Core views for aidooit people."""
from django.http import HttpResponse


def index(request):
    """Home page for aidooit people."""
    return HttpResponse('Hello, your are in People index :D')
