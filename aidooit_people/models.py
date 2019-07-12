"""Model for aidooit people app."""
from django.db import models
from django.utils import timezone


class Person(models.Model):
    """Person model for aidooit people."""

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=40, blank=True)

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
