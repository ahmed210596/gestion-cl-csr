


from authapp.models import Users
from django.contrib.auth.hashers import make_password


User = Users

from rest_framework import serializers
#from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username','is_superuser','matricule','password','password_confirm','is_active']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'matricule','username', 'email', 'password','password_confirm')
 
 
 
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['matricule'], validated_data['email'], make_password(validated_data['password']))

        return user
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Password fields didn't match")
        return attrs
class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=8, max_length=128) 
    confirm_password = serializers.CharField(min_length=8, max_length=128)   