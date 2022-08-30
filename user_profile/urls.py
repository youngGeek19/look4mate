from django.urls import path
from .views import *

app_name = 'user_profile'
urlpatterns = [
    path('', ProfileView, name='profile'),
    path('edit_profile/', ProfileEditView, name='edit_profile')
]