from authapp.models import Users
from authapp.serializer import UserSerializer
from productapp.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    
    creator = UserSerializer()
    editor = UserSerializer()
    # 

    
    class Meta:
        model = Product
        fields = '__all__'
        