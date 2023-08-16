from base64 import urlsafe_b64decode, urlsafe_b64encode
from ctypes.wintypes import HINSTANCE
from authapp.serializer import UserSerializer
from productapp.serializer import ProductSerializer
from serialapp.serializer import SerialSerializer


from  .utils import Util
from typing import Self
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from rest_framework import serializers
# from .models import Users
from .models import Data, Product, Serial, KeyCSR
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.hashers import make_password

#class PrivilegeSerializer(serializers.ModelSerializer):
   # class Meta:
      #  model = Privilege
       # fields = ['id', 'role']#
# User = Users

from rest_framework import serializers
#from django.contrib.auth.models import User

# User Serializer
""" class UserSerializer(serializers.ModelSerializer):
    class Meta:
        #model = User
        fields = ['id','email', 'username','is_superuser','matricule','password','password_confirm'] """
        
    
        
# Register Serializer
""" class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'matricule','username', 'email', 'password','password_confirm') 
 
 
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['matricule'], validated_data['email'], make_password(validated_data['password']))

        return user
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Password fields didn't match")
        return attrs """
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError('Invalid email or password')

            if not user.is_active:
                raise serializers.ValidationError('User account is disabled')

            attrs['user'] = user
            return attrs

        else:
            raise serializers.ValidationError('Email and password are required')
     

""" class ProductSerializer(serializers.ModelSerializer):
    
    # creator = UserSerializer()
    # editor = UserSerializer()
    # 

    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at','updated_at')
        def create(self, validated_data):
         creator_username = validated_data.pop('creator', None)
         editor_username = validated_data.pop('editor', None)
         if creator_username:
            creator = Users.objects.get(id=creator_username)
            validated_data['creator'] = creator
         if editor_username:
            editor = Users.objects.get(username=creator_username)
            validated_data['editor'] = editor    
            return super().create(validated_data)   """

       
""" class SerialSerializer(serializers.ModelSerializer):
    # creator = UserSerializer()
    # editor = UserSerializer()

    class Meta:
        model = Serial
        fields = ('id', 'serial_number','creator','editor','created_at', 'updated_at') """



class KeyCSRSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    serial = SerialSerializer()
    creater = UserSerializer()
    editor = UserSerializer()

    class Meta:
        model = KeyCSR
        fields = ('id', 'product', 'serial', 'creater', 'editor', 'created_at', 'updated_at', 'files', 'country','state','locality','organization','org_unit','common_name','status','timestamp_epoch_time_start','timestamp_epoch_time_end')



class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        # model = Users
        fields = ('old_password', 'password', 'password2')
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("The old password is incorrect")
        return value
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    def save(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != HINSTANCE.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
""" class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        # model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
        

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance   """  





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
""" class SendPasswordResetEmailSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    fields = ['email']

  def validate(self, attrs):
    email = attrs.get('email')
    if Users.objects.filter(email=email).exists():
      user = Users.objects.get(email = email)
      uid = urlsafe_b64encode(force_bytes(user.id))
      print('Encoded UID', uid)
      token = PasswordResetTokenGenerator().make_token(user)
      print('Password Reset Token', token)
      link = 'http://localhost:4200/change-password/'+uid+'/'+token
      print('Password Reset Link', link)
      # Send EMail
      body = 'Click Following Link to Reset Your Password '+link
      data = {
        'subject':'Reset Your Password',
        'body':body,
        'to_email':user.email
      }
      Util.send_email(data)
      return attrs
    else:
      raise serializers.ValidationError('You are not a Registered User')
  
class UserPasswordResetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    try:
      password = attrs.get('password')
      password2 = attrs.get('password2')
      uid = self.context.get('uid')
      token = self.context.get('token')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      id = smart_str(urlsafe_b64decode(uid))
      user = Users.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(user, token):
        raise serializers.ValidationError('Token is not Valid or Expired')
      user.set_password(password)
      user.save()
      return attrs
    except DjangoUnicodeDecodeError as identifier:
      PasswordResetTokenGenerator().check_token(user, token)
      raise serializers.ValidationError('Token is not Valid or Expired') """
class EmployerBoardSerializer(serializers.Serializer):
    class Meta:
        model = Data
        fields = ('total_products', 'total_serials', 'products_created', 'serials_created')   