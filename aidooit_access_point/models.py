from django.db import models


class AidooitAccessPoint(models.Model):
    """The Aidooit Access Point (AAP) its where people can login.

    AAP implements many ways for people to login. It could be using
    QR codes, fingerprints, facial recognition, etc.
    An AAP can share information with other AAP to get the network up to date.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name
