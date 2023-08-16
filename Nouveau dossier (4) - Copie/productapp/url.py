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
# from .views import SendPasswordResetEmail

#from .views import ChangePasswordView,SendPasswordResetEmailView,reset_request
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#from .views import  LogoutView,MyObtainTokenPairView,login_user,Register_Users
#from .views import LoginAPI, RegisterAPI,logout
from django.urls import path
from knox import views as knox_views


from .views import ProductDetail, ProductList, ProductSearch

urlpatterns=[
   
    
    url(r'^product/$',ProductList),
    url(r'^product/([0-9]+)$',ProductDetail),
    
       
    
    
    
    path('product/search/', ProductSearch, name='product-search'),
   

    # ... your other URL patterns
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)