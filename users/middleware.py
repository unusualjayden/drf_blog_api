from django.utils import timezone
from rest_framework_simplejwt import authentication

from users.models import User


class LastUserRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        user = request.user
        if user:
            User.objects.filter(id=user.id).update(last_active=timezone.now())
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            request.user = authentication.JWTAuthentication().authenticate(request)[0]
        except TypeError:
            pass
