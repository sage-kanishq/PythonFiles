from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    date_postead = models.DateTimeField(default = timezone.now)