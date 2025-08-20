from django.db import models

from core.apps.shared.models import BaseModel



class SiteConfig(BaseModel):
    email_host = models.CharField(max_length=200, default='smtp.gmail.com')
    email_host_password = models.CharField(max_length=200)
    bot_token = models.CharField(max_length=200)
    channel_username = models.CharField(max_length=200)
    manager = models.URLField(default='https://t.me/telegram')

    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"
    
