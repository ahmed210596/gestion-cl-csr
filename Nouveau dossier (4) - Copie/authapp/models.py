from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
# Create your models here.
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from OpenSSL import crypto
from django.utils.translation import gettext_lazy as _
import threading
from django.core.validators import RegexValidator
class CustomUserManager(BaseUserManager):
    def create_user(self, matricule, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            matricule=matricule,
            username=username,
            email=self.normalize_email(email),
        )
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricule, username, email, password):
        user = self.create_user(
            matricule=matricule,
            username=username,
            email=email,
            password=password,
            
        )
        user.is_admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user




class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    password_confirm=models.CharField(max_length=255)
    username = models.CharField(unique=True,max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    matricule = models.CharField(max_length=255)
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','matricule','password']

    def __str__(self):
        return self.email