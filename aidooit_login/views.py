"""Core views for aidooit login."""
from django.views import generic

from .models import Login


class IndexView(generic.ListView):
    """Generic view for index."""

    template_name = 'aidooit_login/index.html'
    context_object_name = 'login_list'

    def get_queryset(self):
        """Return the list of login."""
        return Login.objects.order_by('date')


class DetailView(generic.DetailView):
    """Generic view for details."""

    model = Login
    #  by default it return an object named person (like model name)
    #  use context_object_name if you want specify other
    #  context_object_name = 'other_name'
    template_name = 'aidooit_login/login_details.html'
