from rest_framework import serializers
from .models import AidooitAccessPoint


class AAPSerializer(serializers.ModelSerializer):
    """Serialice AidooitAccessPoint classs."""

    class Meta:
        model = AidooitAccessPoint
        fields = ('id', 'name', 'description', 'address',)
