from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
	'''
	Модель чатов
	'''
	user_first = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_chats')
	user_second = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'Chat {self.user_first.username} with {self.user_second.username}'

	class Meta:
		verbose_name = 'Чат'
		verbose_name_plural = 'Чаты'


class Message(models.Model):
	'''
	Модель сообщений
	'''
	user_sent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sent_messages')
	text = models.TextField()
	#image = models.ImageField(upload_to=f'chat/{user_sent.username}/to_{user_recieved.username}//%Y/%m/%d/images', blank=True)
	sent_date = models.DateTimeField(auto_now_add=True)
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_messages')

	def __str__(self):
		return f'{self.user_sent.username} message to {self.chat.user_second}'

	class Meta:
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'


