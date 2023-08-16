from base64 import urlsafe_b64decode
import json
from django.utils.encoding import force_bytes, force_str
import logging
from authapp.models import Users
from authapp.serializer import RegisterSerializer, UserSerializer
from .serializer import EmployerBoardSerializer
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

from .models import Data, KeyCSR
from application.serializer import KeyCSRSerializer
#from .serializer import LoginSerializer, SendPasswordResetEmailSerializer, SerialSerializer, UserPasswordResetSerializer

# Create your views here.
from .models import Product
from .models import Serial
#from .models import Users
from .serializer import UserChangePasswordSerializer
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
from .serializer import ProductSerializer,KeyCSRSerializer
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
# from .models import Users

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.http import HttpResponse
@api_view(['GET'])
def employer_boards(request):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    if request.method == 'GET':
        total_products = Product.objects.count()
        total_serials = Serial.objects.count()
        auth_header=request.META.get('HTTP_AUTHORIZATION', '')
        #auth_header = request.META.get('Authorization')
        print(auth_header)
        # Check if the auth_header is present and has a valid format
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]  # Extract the token value
            print(token)
            
            # Get the user based on the token 
            user = get_user_from_token(token)
            print(user)
            print(user.username)
            # Deserialize the request data
            #data = request.data.copy()
            #data['creator'] = user.username if user else None
            products_created = Product.objects.filter(creator=user).count()
            serials_created = Serial.objects.filter(creator=user).count()
            data={
        "total_products": total_products,
        "total_serials": total_serials,
        "products_created": products_created,
        "serials_created": serials_created}
            #d=Data({'total_products': total_products,'total_serials': total_serials,'products_created': products_created,'serials_created': serials_created})
            #serializer = EmployerBoardSerializer(d)
            
    # Retrieve the serialized representation
              #serialized_data = serializer.data
            json_data = json.dumps(data,indent=4)
            
            #print(type(json_data))
            return Response(json_data, content_type='application/json', status=status.HTTP_200_OK)
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid or missing authorization header'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def admin_boards(request):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    if request.method == 'GET':
        total_products = Product.objects.count()
        total_serials = Serial.objects.count()
        auth_header=request.META.get('HTTP_AUTHORIZATION', '')
        #auth_header = request.META.get('Authorization')
        print(auth_header)
        # Check if the auth_header is present and has a valid format
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]  # Extract the token value
            print(token)
            
            # Get the user based on the token 
            user = get_user_from_token(token)
            print(user)
            print(user.username)
            # Deserialize the request data
            #data = request.data.copy()
            #data['creator'] = user.username if user else None
            products_created = Product.objects.get(pk=user.pk).count()
            serials_created = Serial.objects.get(pk=user.pk).count()
            return Response(data={
        'total_products': total_products,
        'total_serials': total_serials,
        'products_created': products_created,
        'serials_created': serials_created
        })
        return Response({'error': 'Invalid or missing authorization header'}, status=status.HTTP_401_UNAUTHORIZED)

class MyPagination(PageNumberPagination):
    page_size = 3  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Maximum number of items per pag
    def paginate_queryset(self, queryset, request, view=None):
        page = request.query_params.get('page')
        paginated_queryset = super().paginate_queryset(queryset, request, view=view)
        serializer = UserSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
class MyPaginationp(PageNumberPagination):
    page_size = 3  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Maximum number of items per pag
    def paginate_queryset(self, queryset, request, view=None):
        page = request.query_params.get('page')
        paginated_queryset = super().paginate_queryset(queryset, request, view=view)
        serializer = ProductSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
""" class MyPaginations(PageNumberPagination):
    page_size = 3  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Maximum number of items per pag
    def paginate_queryset(self, queryset, request, view=None):
        page = request.query_params.get('page')
        paginated_queryset = super().paginate_queryset(queryset, request, view=view)
        serializer = SerialSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })     """
       
@api_view(['GET', 'POST'])
def UsersList(request):
    
    if request.method == 'GET':
        tasks = Users.objects.all()
        
        return MyPagination().paginate_queryset(tasks, request, view=request)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
@api_view(['GET', 'PUT','DELETE'])
def UserDetail(request,pk):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = UserSerializer(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
class ProductListPagination(PageNumberPagination):
    page_size = 3  # Number of products per page
    page_size_query_param = 'page_size'
    max_page_size = 100  
"""@api_view(['GET', 'POST'])
def ProductList(request):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   # print(request.META['HTTP_AUTHORIZATION'])
    
    if request.method == 'GET':
        products = Product.objects.all()

        # Apply pagination
        paginator = ProductListPagination()
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)   

    elif request.method == 'POST':
        auth_header=request.META.get('HTTP_AUTHORIZATION', '')
        #auth_header = request.META.get('Authorization')
        print(auth_header)
        # Check if the auth_header is present and has a valid format
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]  # Extract the token value
            print(token)
            
            # Get the user based on the token 
            user = get_user_from_token(token)
            print(user)
            print(user.username)
            # Deserialize the request data
            data = request.data.copy()
            data['creator'] = user.username if user else None
            #print(data)
            p=Product(product_code=data['product_code'],typer=data['typer'],designation=data['designation'],creator=user)
            #serializer = ProductSerializer(data=data)
            p.save()
            
            print(p.creator)
            #if serializer.is_valid():
            #serializer.validated_data['creator']=request.user
               #serializer.save()







               
            return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid or missing authorization header'}, status=status.HTTP_401_UNAUTHORIZED) """
def get_user_from_token(token):
    try:
        # Decode the token and extract the user ID
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']
        
        # Retrieve the user based on the user ID
        user = Users.objects.get(pk=user_id)
        return user
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, Users.DoesNotExist):
        raise AuthenticationFailed('Invalid or expired token')    

""" @api_view(['GET', 'PUT','DELETE'])
def ProductDetail(request,pk):
    
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
        return Response(status=status.HTTP_204_NO_CONTENT)"""
""" @api_view(['GET', 'POST'])    
def SerialList(request):
   
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        tasks = Serial.objects.all()
        paginator = ProductListPagination()
        paginated_products = paginator.paginate_queryset(tasks, request)

        serializer = SerialSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        auth_header=request.META.get('HTTP_AUTHORIZATION', '')
        #auth_header = request.META.get('Authorization')
        print(auth_header)
        # Check if the auth_header is present and has a valid format
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]  # Extract the token value
            print(token)
            
            # Get the user based on the token 
            user = get_user_from_token(token)
            print(user)
            print(user.username)
            # Deserialize the request data
            data = request.data.copy()
            data['creator'] = user.username if user else None
            #print(data)
            s=Serial(serial_number=data['serial_number'],creator=user)
            #serializer = ProductSerializer(data=data)
            s.save()
            
            print(s.creator)
            #if serializer.is_valid():
            #serializer.validated_data['creator']=request.user
               #serializer.save()







               
            return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid or missing authorization header'}, status=status.HTTP_401_UNAUTHORIZED) """
    

""" @api_view(['GET', 'PUT','DELETE'])
def SerialDetail(request,pk):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    try:
        s = Serial.objects.get(pk=pk)
    except Serial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SerialSerializer(s)
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
            
            
            s.serial_number=data['serial_number']
            
            
            s.editor=user1
            #serializer = ProductSerializer(data=data)
            s.save()
            
            print(s.editor)
            #if serializer.is_valid():
            #serializer.validated_data['creator']=request.user
               #serializer.save()







               
            return Response({'message': 'Product udated successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid or missing authorization header'}, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        s.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """


logger = logging.getLogger('signal')

@api_view(['GET', 'POST'])
def ListKeyCSR(request):
    logger.info(f"Received {request.method} request for ListKeyCSR")

    if request.method == 'GET':
        # Get all keycsr objects from the database
        keycsrs = KeyCSR.objects.all()

        # Serialize the keycsr objects and return the response
        serializer = KeyCSRSerializer(keycsrs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')

        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]  # Extract the token value

            user = get_user_from_token(token)

            if user:
                logger.info(f"User '{user.username}' successfully authenticated for POST request.")
            else:
                logger.warning("Invalid user token provided for POST request.")

            data = request.data.copy()
            data['creater'] = user.username if user else None

            pk = data['serial']
            ser = Serial.objects.get(pk=pk)
            pkk = data['product']
            prod = Product.objects.get(pk=pkk)

            s = KeyCSR(
                serial=ser,
                product=prod,
                state=data['state'],
                country=data['country'],
                locality=data['locality'],
                organization=data['organization'],
                org_unit=data['org_unit'],
                common_name=data['common_name'],
                duree=data['duree'],
                creater=user
            )

            s.generate_keycsr()
            s.save()

            logger.info(f"KeyCSR object created successfully by user '{user.username}' for POST request.")

            return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)

        logger.warning("Invalid or missing authorization header for POST request.")
        return Response({'error': 'Invalid or missing authorization header'}, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['GET', 'PUT', 'DELETE'])    
def KeyCSRDetails(request,pk):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]

   try:
        key_csr = KeyCSR.objects.get(pk=pk)
   except KeyCSR.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

   if request.method == 'GET':
        serializer = KeyCSRSerializer(key_csr)
        return Response(serializer.data)

   elif request.method == 'PUT':
        auth_header=request.META.get('HTTP_AUTHORIZATION', '')
        #auth_header = request.META.get('Authorization')
        print(auth_header)
        # Check if the auth_header is present and has a valid format
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]  # Extract the token value
            print(token)
            
            # Get the user based on the token 
            user = get_user_from_token(token)
            print(user)
            print(user.username)
            # Deserialize the request data
            data = request.data.copy()
            #data['editor'] = user if user else None
            #print(data)


            print(data['serial'])
            pk=data['serial']
            #print(pk.id)
            
            
            ser=Serial.objects.get(pk=pk)
            pkk=data['product']
            print()
            prod=Product.objects.get(pk=pkk)
            print('oki')
            key_csr.serial=ser
            #print(key_csr.serial)
            key_csr.product=prod
            #print(key_csr.product)
            key_csr.state=data['state']
            key_csr.country=data['country']
            key_csr.locality=data['locality']
            key_csr.organization=data['organization']
            key_csr.org_unit=data['org_unit']
            key_csr.common_name=data['common_name']
            key_csr.editor=user
            print(key_csr.editor)
            """ data = {
    'serial': ser,
    'product': prod,
    'state': data['state'],
    'country': data['country'],
    'locality': data['locality'],
    'organization': data['organization'],
    'org_unit': data['org_unit'],
    'common_name': data['common_name']
    }  """      
            """ serializer = KeyCSRSerializer(data=data)
            if serializer.is_valid():
              s=serializer.save(creater=user)
              s.generate_keycsr() """
            print('oki')
            #serializer = ProductSerializer(data=data)
            #key_csr.generate_keycsr()
            key_csr.save()
            
            
            







               
            return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid or missing authorization header'}, status=status.HTTP_401_UNAUTHORIZED)
        

   elif request.method == 'DELETE':
        key_csr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def changestatus(request, pk):
    try:
        key_csr = KeyCSR.objects.get(pk=pk)
    except KeyCSR.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Extract the status value from the request data
    new_status = request.data.get('status')

    if new_status is not None:
        key_csr.status = new_status
        key_csr.save()
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)
           

""" @api_view(['PUT'])
def activate(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Extract the status value from the request data
    new_status = request.data.get('is_activate')
    print(new_status)
    if new_status is not None:
        user.is_active =new_status
        print(user.is_activate)
        user.save()
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST) """

@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    # Get the request body and load it as JSON
    reqBody = json.loads(request.body)
    email = reqBody.get('email')
    password = reqBody.get('password')
    
    # If email or password is missing, raise a validation error
    if not email or not password:
        raise ValidationError({'message': 'Please provide email and password'})
    
    # Authenticate the user
    user = authenticate(request=request, username=email, password=password)
    
    # If authentication fails, raise a validation error
    if not user:
        raise ValidationError({'message': 'Incorrect login credentials'})
    
    # Generate a new token for the user
    token, created = Token.objects.get_or_create(user=user)
    
    # If the user is not active, raise a validation error
    if not user.is_active:
        raise ValidationError({'message': 'User is not active'})
    
    # Login the user
    login(request, user)
    
    # Return a JSON response with the token
    return JsonResponse({'token': token.key})




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):

    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def HomeView(request):
  if request.method == 'GET':  
      data = {
        "message": "Welcome to the solution sagemcom application!",
        "author": "created by ahmed nouri",
        "version": "1.0"
     }
      return Response(data,status=status.HTTP_200_OK)
@api_view(['GET'])
def ProfileView(request):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def ChangePasswordView(request):
    
    if request.method == 'GET':
        serializer = UserChangePasswordSerializer(request.user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'password changed'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def reset_request(request):
    data = request.data
    email = data['email']
    user = Users.objects.get(email=email)
    if Users.objects.filter(email=email).exists():
        # send email with otp
        send_mail(
        'Subject here',
        f'Here is the message with {user.matricule}.',
        'anouri339@gmail.com',
        [user.email],
        fail_silently=False,
        )
        message = {
            'detail': 'Success Message'}
        return Response(message, status=status.HTTP_200_OK)
    else:
        message = {
            'detail': 'Some Error Message'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)





from rest_framework_simplejwt.views import TokenObtainPairView



from rest_framework import generics






# Register API
 
   
""" @api_view(['POST'])
def signup(request):
    serializer = RegisterSerializer(data=request.data)
    
   
    if serializer.is_valid():
        serializer.save()
        #user = Users.objects.get(email=request.POST.get('email'))
        # user.set_password(request.data['password'])
        #user.create_user(request.data)
        
        return Response({ 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK) """
import jwt
from django.conf import settings
""" @api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
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
        return Response({'error': 'Invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) """

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
""" @csrf_exempt
@api_view(['POST'])
def SendPasswordResetEmail(request):
    if request.method == 'POST':
        email = request.data.get('email')  # Use request.data to retrieve POST data

        if email:
            user = Users.objects.filter(email=email).first()

            if user:
                print(force_bytes(user.pk))
                # Generate a password reset token
                token_generator = default_token_generator
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
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
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) """

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
""" @api_view(['POST'])
def ResetPassword(request, uidb64=None, token=None):
    if request.method == 'POST':
        try:
            uid = urlsafe_b64decode(uidb64).decode()
            user = Users.objects.get(pk=uid)
            print(uid)
            #print(user)
            if  user is not None and default_token_generator.check_token(user, token):
                # Set the user's new password
                   print(default_token_generator.check_token(user, token))
                   password = request.data.get('new_password')
                   print(password)
                   user.set_password(password)
                   user.save()

                   return Response({'status': 'password reset successful'}, status=status.HTTP_200_OK)
            
            
            else:
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except (TypeError, ValueError, OverflowError, Users.DoesNotExist):
            return Response({'error': 'Invalid user'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) """


""" @api_view(['GET'])
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
        return Response(serializer.data, status=status.HTTP_200_OK) """
""" @api_view(['GET'])
def SerialSearch(request):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        query = request.query_params.get('q', '')  # Get the search query from the request parameters

        serials = Serial.objects.filter(
            Q(serial_number__icontains=query)| 
            Q(creator__username__icontains=query)|
 
             Q(editor__username__icontains=query)
        )

        serializer = SerialSerializer(serials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) """
""" @api_view(['GET'])
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
        return Response(serializer.data, status=status.HTTP_200_OK)         """

from django.http import HttpResponse
from django.shortcuts import render
#from .task import add

def index(request):
 logger = logging.getLogger("signal")
 message = {
  'message' : "user visits index()"
 }
 logger.info(message)
 return HttpResponse("hello")