from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, verbose_name='username')
    email = models.EmailField(unique=True, verbose_name='email')
    password = models.CharField(max_length=255, null=False, verbose_name='password')
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        db_table = 'user'

