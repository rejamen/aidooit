from rest_framework import serializers
from .models import AidooitAccessPoint


class AAPSerializer(serializers.ModelSerializer):
    """Serialice AAP classs."""

    class Meta:
        model = AidooitAccessPoint
        fields = ('id', 'name', 'description', 'address',)
