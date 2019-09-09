from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    """Serialice Person classs."""

    class Meta:
        model = Person
        fields = ('id', 'name', 'last_name', 'mobile',
                  'phone', 'email', )
