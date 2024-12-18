from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import serializers.CharField()
from rest_framework import get_user_model().objects.create_user
User = get_user_model()  # Ensures compatibility with the custom user model.

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensures password is write-only.

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']

    def create(self, validated_data):
        # Create a user using the built-in create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # Automatically create a token for the new user.
        return user

from rest_framework import serializers
from django.contrib.auth import get_user_model

# Dynamically get the custom user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Password is write-only to avoid exposing it.

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']
        extra_kwargs = {'followers': {'read_only': True}}  # Followers can only be read via API.

    def create(self, validated_data):
        """
        Create a new user using the `create_user` method, which handles password hashing.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
