from django.shortcuts import render
# Create your views here.

from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import api_view

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

@api_view(['POST'])
def user_register(response):
    if response.method =="POST":
        serializer = UserSerializer(data=response.data)
        if serializer.is_valid():
            print(type(serializer.validated_data))
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

