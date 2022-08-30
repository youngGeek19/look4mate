from django.urls import path

from .views import *

app_name = 'chat'
urlpatterns = [
	path('', ChatView, name='chat'),
	path('<str:room_name>/', dialog, name='dialog')
]