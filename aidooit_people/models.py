"""Model for aidooit people app."""
from django.db import models


class Person(models.Model):
    """Person model for aidooit people."""

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)

    def __str__(self):
        """How str is displayed."""
        res = '{} {}'.format(self.name, self.last_name)
        return res
