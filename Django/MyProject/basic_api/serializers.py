from rest_framework import serializers
from .models import Article
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.TextField()
    author = serializers.ForeignKey(User,on_delete = models.CASCADE)
    date_postead = serializers.DateTimeField()
    

    def create(self,validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.author = validated_data.get('author',instance.author)
        instance.content = validated_data.get('content',instance.content)
        instance.date_posted = validated_data.get('date_posted',instance.date_posted)
        instance.save()
        return instance