"""Model for aidooit people app."""
import random

from django.db import models
from django.utils import timezone


class Person(models.Model):
    """Person model for aidooit people."""

    def _generate_access_key():
        """Generate an unique random access code for each Aidooit Person."""
        choices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*&#_/|+-'
        key = random.choices(choices, k=10)
        access_key = ''.join(key)
        # TODO: Check if generated key already exists
        return access_key

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    access_key = models.CharField(max_length=10, default=_generate_access_key)

    def __str__(self):
        """How str is displayed."""
        res = '{} {}'.format(self.name, self.last_name)
        return res


class PersonHistory(models.Model):
    """Set of historical records."""

    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=500)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Person Historical"
