from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer,UserSerializer


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ['username','firstname','lastname','password','email','phone','date_of_birth']