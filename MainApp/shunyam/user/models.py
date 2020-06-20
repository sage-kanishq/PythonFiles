from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,AbstractUser
)
from phonenumber_field.modelfields import PhoneNumber,PhoneNumberField

class Account(AbstractUser):
    # username = models.CharField(max_length=128,unique=True,blank=False)
    # firstname = models.CharField(max_length=64)
    # lastname = models.CharField(max_length=64)
    date_of_birth = models.DateField(null = True)

    # email = models.EmailField(
    #     verbose_name='email address',
    #     max_length=255,
    #     unique=False,
    # )

    phone = PhoneNumberField()
    active = models.BooleanField(default=False,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
     
    # active = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email','first_name','last_name'] # Email & Password are required by default.
    @property
    def full_name(self):
        # The user is identified by their email address
        return self.first_name +" "+self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return getattr(self,self.USERNAME_FIELD)
