import datetime
from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.core.files.base import ContentFile
from django.conf import settings
import os
# Create your models here.
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from productapp.models import Product
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from OpenSSL import crypto
from django.utils.translation import gettext_lazy as _
import threading
from django.core.validators import RegexValidator
from cryptography.hazmat.primitives import serialization
from serialapp.models import Serial
import time
import socket
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from os.path import exists, join
""" class CustomUserManager(BaseUserManager):
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
        return self.email """
  

""" class Product(models.Model):
    product_code = models.CharField(max_length=20, unique=True)
    typer = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='product_created',null=True,default=None)
    #creator = CurrentUserField(Users,related_name='product_created')
    #editor = CurrentUserField(Users,on_update=True,related_name='product_updated')
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_edited',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  """
    
    

""" class Serial(models.Model):
    
    serial_number = models.CharField(max_length=100,unique=True,null=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, related_name='serials_created',default=None)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, related_name='serials_edited')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  """
    

from django.db import models
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID  
from cryptography.hazmat.primitives import hashes

# Rest of the code...


class Data(models.Model):
    total_products = models.IntegerField()
    total_serials = models.IntegerField()
    products_created = models.IntegerField()
    serials_created = models.IntegerField()
class KeyCSR(models.Model):
    serial = models.ForeignKey(Serial, related_name='key_Serial', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='key_products', null=True, on_delete=models.CASCADE)
    creater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='key_created', editable=True, null=True, blank=True)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='key_edited', editable=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    files = models.FileField(upload_to='', blank=True, null=True)
    country = models.CharField(max_length=500)
    state = models.CharField(max_length=250,default=None)
    locality = models.CharField(max_length=500)
    organization = models.CharField(max_length=500)
    org_unit = models.CharField(max_length=500)
    common_name = models.CharField(max_length=500)
    duree=models.BigIntegerField(null=True,blank=True)
    status = models.BooleanField(default=True)
    timestamp_epoch_time_start = models.DateTimeField(null=True)
    timestamp_epoch_time_end = models.DateTimeField(null=True)
    def generate_keycsr(self):
        key = crypto.PKey()
        key.generate_key(crypto.TYPE_RSA, 2048)

        req = crypto.X509Req()
        timestamp_epoch_time_start = int(time.time())
        print(timestamp_epoch_time_start )
        timestamp_epoch_time_end = timestamp_epoch_time_start + int(self.duree) 
        print(timestamp_epoch_time_start )
        print(req.get_subject())

        req.get_subject().C = self.country
        print(req.get_subject().C)
        req.get_subject().ST = self.state
        print(req.get_subject().ST)
        req.get_subject().L = self.locality
        print(req.get_subject().L)
        req.get_subject().O = self.organization
        print(req.get_subject().O )
        req.get_subject().OU = self.org_unit
        req.get_subject().CN = self.common_name

        req.set_pubkey(key)
        req.sign(key, "sha256")
        print(req)

        csr_pem = crypto.dump_certificate_request(crypto.FILETYPE_PEM, req)
        key_pem = key.to_cryptography_key().private_bytes(
             encoding=serialization.Encoding.PEM,

             format=serialization.PrivateFormat.PKCS8,

             encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
        )
        print('oki')
        csr_filename = f"{self.files.name}.csr"
        key_filename = f"{self.files.name}.key"
        print(csr_filename)
        print(csr_pem)

        base_path = settings.MEDIA_ROOT
        save_dir = 'data'
        print(save_dir)
        print(base_path)
        # Save CSR
        
        csr_path = os.path.join(base_path, save_dir, csr_filename)
        csr_content = ContentFile(csr_pem)
        self.files.save(csr_path, csr_content)

        # Save private key
        key_path = os.path.join(base_path, save_dir, key_filename)
        key_content = ContentFile(key_pem)
        self.files.save(key_path, key_content)
        
        # Update the file paths in the model
        self.files.name = csr_path

# Extract the expiration date from the certificate
        

# Convert the expiration date to a more readable format
        self.timestamp_epoch_time_start = datetime.datetime.fromtimestamp(timestamp_epoch_time_start)
        
        self.timestamp_epoch_time_end = datetime.datetime.fromtimestamp(timestamp_epoch_time_end)

        self.save(update_fields=['files', 'timestamp_epoch_time_start', 'timestamp_epoch_time_end'])
        
   

