from django.db import models
from django.contrib.auth.models import AbstractUser

from core.apps.accounts.managers.user import UserManager
from core.apps.shared.models import BaseModel


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    role = models.CharField(
        choices=[('user', 'User'), ('admin', 'Admin')], default='user', max_length=10
    )
    full_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'