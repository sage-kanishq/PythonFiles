from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    content = models.CharField(max_length=100000,default="")
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' ' +str(self.pk)