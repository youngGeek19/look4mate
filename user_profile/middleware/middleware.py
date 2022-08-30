import datetime
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin
from config import settings


class ActiveUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        current_user = request.user
        if request.user.is_authenticated:
            now = datetime.datetime.now()
            cache.set('seen_' + current_user.username, now, settings.USER_LASTSEEN_TIMEOUT)