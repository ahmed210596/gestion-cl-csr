from django.db import models

from tries import settings

class Product(models.Model):
    product_code = models.CharField(max_length=20, unique=True)
    typer = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='product_created',null=True,default=None)
    #creator = CurrentUserField(Users,related_name='product_created')
    #editor = CurrentUserField(Users,on_update=True,related_name='product_updated')
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_edited',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
