from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from core.apps.shared.models import BaseModel


class SecureTransaction(BaseModel):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    text = RichTextUploadingField(verbose_name='текст')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Безопасная сделка'
        verbose_name_plural = 'Безопасная сделка'