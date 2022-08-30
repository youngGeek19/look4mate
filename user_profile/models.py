from config import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.cache import cache
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    avatar = models.ImageField(upload_to='profile/avatar', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', blank=True)
    it_stack = models.CharField(max_length=150, verbose_name='Направление в IT', blank=True)
    work_exp = models.PositiveSmallIntegerField(verbose_name='Стаж работы', blank=True)
    location = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username

    def last_seen(self):
        return cache.get('seen_' + self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    def __str__(self):
        return f'Post by {self.user.username} at {self.published}'

