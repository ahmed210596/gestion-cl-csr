from django.db import models

from tries import settings

# Create your models here.


class Serial(models.Model):
    
    serial_number = models.CharField(max_length=100,unique=True,null=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, related_name='serials_created',default=None)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, related_name='serials_edited')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 