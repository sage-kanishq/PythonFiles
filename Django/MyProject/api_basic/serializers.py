from rest_framework import serializers
from django.utils import timezone
from .models import Article


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields  = ['title','author','email']
        fields  = '__all__'




        
        