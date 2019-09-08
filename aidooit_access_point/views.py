"""Core views for aidooit access point."""
from django.views import generic

from .models import AidooitAccessPoint


class IndexView(generic.ListView):
    """Generic view for index."""

    template_name = 'aidooit_access_point/index.html'
    context_object_name = 'aap_list'

    def get_queryset(self):
        """Return the list of login."""
        return AidooitAccessPoint.objects.order_by('name')


class DetailView(generic.DetailView):
    """Generic view for details."""

    model = AidooitAccessPoint
    #  by default it return an object named person (like model name)
    #  use context_object_name if you want specify other
    context_object_name = 'aap'
    template_name = 'aidooit_access_point/aap_details.html'
