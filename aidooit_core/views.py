"""Core views for aidooit."""
from django.shortcuts import render


def index(request):
    """Home page for aidooit."""
    data = {}
    template = 'core/index.html'
    return render(request, template, data)


def error_404_view(request, exception):
    """Custom 404 Error."""
    data = {
        "name": "Aidooit.com"
    }
    template = 'core/error_404.html'
    return render(request, template, data)
