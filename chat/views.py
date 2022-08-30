from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *


def ChatView(request):
	chats = Chat.objects.all()
	context = {
		'section': 'chat',
		'chats': chats,
	}
	return render(request, 'chat/chat.html', context)

def dialog(request, room_name):
	chat = Chat.objects.get(pk=room_name)
	messages = chat.chat_messages.order_by('-sent_date')
	context = {
		'section': 'chat',
		'chat_id': room_name,
		'user_name': request.user.username, 
		'messages': messages,
	}
	return render(request, 'chat/chat_window.html', context)