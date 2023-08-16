from django.urls import re_path as url,path,include
from application import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
#from .views import  ProfileView, RegisterAPI, ResetPassword, SendPasswordResetEmailView,SerialList,SerialDetail,HomeView, UpdateProfileView, UserPasswordResetView
#from .views import UsersList,UserDetail,ProductList,ProductDetail,ListKeyCSR, KeyCSRDetails
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SerialDetail, SerialList, SerialSearch

#from .views import ChangePasswordView,SendPasswordResetEmailView,reset_request
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#from .views import  LogoutView,MyObtainTokenPairView,login_user,Register_Users
#from .views import LoginAPI, RegisterAPI,logout
from django.urls import path
from knox import views as knox_views




urlpatterns=[
   
  
   
    
    
    url(r'^serial/$',SerialList),
    url(r'^serial/([0-9]+)$',SerialDetail),
    path('serial/search', SerialSearch, name='product-search'),
    
    
    
    
   
       
    
    
    

    # ... your other URL patterns
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)