from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser,BaseUserManager
# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length = 10,unique=True)
    age = models.IntegerField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']



