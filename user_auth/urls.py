from django.urls import path
from .views import *



app_name = 'user_auth'
urlpatterns = [
    path('login_form/', LoginView, name='login'),
    path('register_form/', RegisterView, name='register'),
    path('logout/', UserLogOutView, name='logout')
]