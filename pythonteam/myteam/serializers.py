from rest_framework import serializers
from .models import UserProfileInfo.


class UserProfileInfoSerializer(serializers.ModelSerializer):
    # Serializer to map the Model instance into JSON format.

    class Meta:
        # Meta class to map serializer's fields with the model fields.
        model = UserProfileInfo
        fields = ('email', 'username', 'password')
