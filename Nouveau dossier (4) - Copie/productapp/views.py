from django.shortcuts import render
from application.views import ProductListPagination, get_user_from_token

from productapp.models import Product
from base64 import urlsafe_b64decode
import json
from django.utils.encoding import force_bytes, force_str
from django.db.models import Q
from sqlite3 import IntegrityError
from xml.dom import ValidationErr
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from productapp.serializer import ProductSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.pagination import PageNumberPagination
#from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from rest_framework.request import Request
from django.http import HttpRequest

#from .models import KeyCSR
from application.serializer import KeyCSRSerializer
#from .serializer import LoginSerializer, SendPasswordResetEmailSerializer, SerialSerializer, UserPasswordResetSerializer

# Create your views here.
# from .models import Product
# from .models import Serial
#from .models import Users
#from .serializer import UserChangePasswordSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.views import LogoutView
from rest_framework.decorators import permission_classes

from django.http import Http404

from django.shortcuts import get_object_or_404

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
#from .serializer import UserSerializer
#from .serializer import ProductSerializer,KeyCSRSerializer
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from django.views import View
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
#from .models import Users
#from .serializer import UserSerializer


from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from django.contrib.auth import views as auth_views
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
#from .serializer import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


#from .serializer import UserSerializer






     
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
# Create your views here.
import logging

logger = logging.getLogger('signal')

@api_view(['GET', 'POST'])
def ProductList(request):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    if request.method == 'GET':
        products = Product.objects.all()

        # Apply pagination
        paginator = ProductListPagination()
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)   

    elif request.method == 'POST':
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        logger.debug('Authorization header: %s', auth_header)
        
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]
            logger.debug('Extracted token: %s', token)
            
            user = get_user_from_token(token)
            logger.debug('Authenticated user: %s', user)
            
            data = request.data.copy()
            data['creator'] = user.username if user else None
            p = Product(product_code=data['product_code'], typer=data['typer'], designation=data['designation'], creator=user)
            p.save()
            
            logger.info('Product created by user: %s', p.creator)
            
            return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
        
        logger.warning('Invalid or missing authorization header')
        return Response({'error': 'Invalid or missing authorization header'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT','DELETE'])
def ProductDetail(request,pk):
    """
    Retrieve, update or delete a product instance.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    try:
        p = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(p)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
            
        auth_header=request.META.get('HTTP_AUTHORIZATION', '')
        
        # Check if the auth_header is present and has a valid format
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]  # Extract the token value
            
            # Get the user based on the token (You need to implement this logic)
            user1 = get_user_from_token(token)
            
            # Deserialize the request data
            data = request.data.copy()
            
            data['editor'] = user1 if user1 else None
            
            
            p.product_code=data['product_code']
            p.typer=data['typer']
            p.designation=data['designation']
            p.editor=user1
            #serializer = ProductSerializer(data=data)
            p.save()
            
            print(p.creator)
            #if serializer.is_valid():
            #serializer.validated_data['creator']=request.user
               #serializer.save()







               
            return Response({'message': 'Product udated successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid or missing authorization header'}, status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'DELETE':
        p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def ProductSearch(request):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        query = request.query_params.get('q', '')  # Get the search query from the request parameters

        products = Product.objects.filter(
            Q(product_code__icontains=query) |
            Q(typer__icontains=query) |
            Q(designation__icontains=query)
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

