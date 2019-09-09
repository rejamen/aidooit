from rest_framework import serializers
from .models import Login


class LoginSerializer(serializers.ModelSerializer):
    """Serialice Login class."""

    class Meta:
        model = Login
        fields = ('id', 'date', 'person', 'aap',)
