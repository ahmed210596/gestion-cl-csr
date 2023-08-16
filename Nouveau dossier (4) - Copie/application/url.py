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
from .views import KeyCSRDetails, changestatus
# from .views import SendPasswordResetEmail

#from .views import ChangePasswordView,SendPasswordResetEmailView,reset_request
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#from .views import  LogoutView,MyObtainTokenPairView,login_user,Register_Users
#from .views import LoginAPI, RegisterAPI,logout
from django.urls import path
from knox import views as knox_views


from .views import ListKeyCSR

urlpatterns=[
   url(r'^user/$', views.UsersList),
   url(r'^user/([0-9]+)$',views.UserDetail),
   #path('user/<int:pk>/activate', activate, name='activate'),

#    path('signup/', views.signup),
#    path('login/', views.login),
   
    #url(r'^product/$',ProductList),
    #url(r'^product/([0-9]+)$',ProductDetail),
    path('keycsrs/', ListKeyCSR, name='list_keycsrs'),
    path('keycsrs/<int:pk>', KeyCSRDetails, name='keycsr_details'),
    path('keycsrs/<int:pk>/changestatus', changestatus, name='change status'),
    #url(r'^serial/$',SerialList),
    #url(r'^serial/([0-9]+)$',SerialDetail),
    #url(r'^keycsr/$',ListKeyCSR),
    #url(r'^KeyCSRDetail/([0-9]+)$',KeyCSRDetails),
    #path('api/register/', RegisterAPI.as_view(), name='register'),
    #path('api/login/', LoginAPI.as_view(), name='login'),
    #path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    #path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
    #path('change-password/', ChangePasswordView, name='change_password'),
    # path('register/', Register_Users, name='register'),
    #path('login/', views.login_user, name='login'),
   
    #path('reset-password/<str:uidb64>/<str:token>/', ResetPassword, name='reset_password'),   
    # path('send-password-reset-email/', SendPasswordResetEmail, name='send_password_reset_email'),   
    path('employer-boards/', views.employer_boards, name='employer_boards'),
    path('admin-boards/', views.admin_boards, name='admin_boards'),
    path('index/', views.index, name='home'),
    path('all/', views.HomeView, name='home'),
    # path('product/search/', views.ProductSearch, name='product-search'),
    # path('user/search/', views.UserSearch, name='USER-search'),
    # path('serial/search/', views.SerialSearch, name='serial-search'),

    # ... your other URL patterns
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


