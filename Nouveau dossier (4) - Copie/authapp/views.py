#from base64 import urlsafe_b64decode
from django.utils.http import urlsafe_base64_decode
import json
from django.utils.encoding import force_bytes, force_str

from django.db.models import Q
from sqlite3 import IntegrityError
from xml.dom import ValidationErr
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
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




# Create your views here.

from .models import Users
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.views import LogoutView
from rest_framework.decorators import permission_classes
from django.utils.encoding import force_text
from django.http import Http404

from django.shortcuts import get_object_or_404

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializer import ResetPasswordSerializer, UserSerializer
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from django.views import View
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Users
from .serializer import UserSerializer
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
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

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.http import HttpResponse
import jwt
from django.conf import settings
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None and user.is_active==True:
            # Generate a JWT token with user ID and email
            payload = {
                'user_id': user.id,
                'email': user.email,
                'is_supeuser':user.is_superuser,
                'matricule':user.matricule,
                'username':user.username
            }
            # login(request, user)
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            serializer = UserSerializer(user)
            return Response({'token': token})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def signup(request):
    serializer = RegisterSerializer(data=request.data)
    
   
    if serializer.is_valid():
        serializer.save()
        #user = Users.objects.get(email=request.POST.get('email'))
        # user.set_password(request.data['password'])
        #user.create_user(request.data)
        
        return Response({ 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)    

@api_view(['POST'])
#
def ResetPassword(request, uidb64=None, token=None):
 if request.method == 'POST':
    try:    
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(Users, pk=uid)
        if default_token_generator.check_token(user, token):
            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')
                # Set the user's new password
                

                # Set the user's new password
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return Response({'detail': 'Password reset successful!'})


            else:
                 return Response({'detail': 'Passwords do not match.'}, status=400)

        else:
             return Response({'detail': 'Invalid token.'}, status=400)
    
    except (TypeError, ValueError, OverflowError, Users.DoesNotExist):
        return Response({'detail': 'Invalid uidb64.'}, status=400)



@csrf_exempt
@api_view(['POST'])
def SendPasswordResetEmail(request):
    if request.method == 'POST':
        email = request.data.get('email')  # Use request.data to retrieve POST data

        if email:
            user = Users.objects.filter(email=email).first()

            if user:
                #print(force_bytes(user.pk))
                # Generate a password reset token
                token_generator = default_token_generator
                pk=str(user.pk)
                bytes_to_encode = pk.encode('utf-8')
                uidb64 = urlsafe_base64_encode(bytes_to_encode)
                token = token_generator.make_token(user)
                
                uidb64_str =  force_str(uidb64)
                
                # Build the password reset URL
                current_site = get_current_site(request)
                domain = current_site.domain
                reset_url = f"http://localhost:4200/reset-password/{uidb64_str}/{token}"

                # Render the password reset email template
                email_subject = "Password Reset"
                email_message = render_to_string('password_reset_email.html', {
                    'user': user.username,
                    'reset_url': reset_url
                })

                # Send the password reset email
                send_mail(
                    email_subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

            # Always return a success response to prevent email harvesting
            return Response({'status': 'password reset email sent'}, status=status.HTTP_200_OK)

        else:
            # Return a bad request response if email is not provided
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Return a method not allowed response for any other request method
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def UserSearch(request):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        query = request.query_params.get('q', '')  # Get the search query from the request parameters

        users = Users.objects.filter(
            Q(email__icontains=query) |
            Q(username__icontains=query) |
            Q(matricule__icontains=query)
        )

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)