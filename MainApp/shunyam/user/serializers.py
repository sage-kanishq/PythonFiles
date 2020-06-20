from rest_framework import serializers
from .models import Account
# from djoser.serializers import UserCreateSerializer,UserSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True,style={"input_type":"password"})
    class Meta:
        model = Account
        fields = ['username','firstname','lastname','password','email','phone','date_of_birth']