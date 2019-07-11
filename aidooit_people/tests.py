"""Testing aidooit people."""
from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from django.urls import reverse

from .models import Person


def create_person(name, last_name, mobile, phone, email):
	"""Create a person with fiven args."""
	return Person.objects.create(name=name, last_name=last_name, mobile=mobile, phone=phone, email=email)

class PersonIndexViewTests(TestCase):
    """All aidooit person tests are here."""

    def test_no_people(self):
        """If none people exists, show a message."""
        response = self.client.get(reverse('aidooit_person:people_index')) 
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "No people available.")
        self.assertQuerysetEqual(response.context['people_list'], [])
