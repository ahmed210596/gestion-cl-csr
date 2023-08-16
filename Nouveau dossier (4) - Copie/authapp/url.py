from django.urls import re_path as url,path,include
from authapp import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from .views import  ResetPassword

from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SendPasswordResetEmail

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path
from knox import views as knox_views




urlpatterns=[
  
   path('signup/', views.signup),
   path('login/', views.login),
   
   
   
    
    #path('change-password/', ChangePasswordView, name='change_password'),
    
   
    path('reset-password/<str:uidb64>/<str:token>/', ResetPassword,TemplateView.as_view(template_name="templates/password_reset_email.html"), name='reset_password'),   
    path('send-password-reset-email/', SendPasswordResetEmail, name='send_password_reset_email'),   
   
    path('user/search/', views.UserSearch, name='USER-search'),
    

    # ... your other URL patterns
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)