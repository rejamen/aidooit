"""Core views for aidooit."""
from django.http import HttpResponse


def index(request):
    """Home page for aidooit."""
    return HttpResponse('Hello, your are in aidooit index :D')
