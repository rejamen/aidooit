from django.db import models
from datetime import datetime
from aidooit_people.models import Person
from aidooit_access_point.models import AidooitAccessPoint


class Login(models.Model):
    """This class store all data related with login in The Aidoit Network.

    This login could be from one person in one Aidooit Access Point.
    """

    date = models.DateTimeField()
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )
    aap = models.ForeignKey(
        AidooitAccessPoint,
        on_delete=models.CASCADE,
        verbose_name='AAP',
    )

    def __str__(self):
        DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
        date = datetime.strftime(self.date, DATETIME_FORMAT)
        person = self.person
        aap = self.aap
        return ('{} ({} -> {})'.format(person, aap, date))
