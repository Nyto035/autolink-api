from django.contrib.auth import get_user_model
from rest_framework import serializers

import bina_bikers.user.models as models


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    image = serializers.ImageField(source='user_profile.image', read_only=True)

    class Meta:
        model = models.User
        fields = (
            'id', 'first_name', 'last_name', 'id', 'email', 'full_name', 'is_active',
            'password', 'image', 'phone_number', 'user_type', 'is_admin')
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }
        read_only_fields = ('last_login', )

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'user', 'image',)
