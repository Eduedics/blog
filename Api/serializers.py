from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
class PostSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        
#  serializer used to handle user registration
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
'''
email = serializers.EmailField(...)

Marks the email field as required.

Applies a UniqueValidator to make sure no other user in the database already has this email (User.objects.all()).

Prevents duplicate emails during registration.

password = serializers.CharField(write_only=True)

Makes the password write-only (it can be set during creation but not read when serialized).

Prevents the password from being exposed in API responses.
Overrides the default create method to:

Use User.objects.create_user(...), which automatically hashes the password before saving.

Returns the newly created user instance.

This is important because saving a password directly (User.objects.create(...)) would store it in plain text, which is a security risk.
'''
    

    