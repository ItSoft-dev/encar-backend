from django.db import models

from ckeditor.fields import RichTextField

from core.apps.shared.models import BaseModel


class FAQ(BaseModel):
    question = models.CharField(max_length=200, verbose_name='вопрос')
    answer = RichTextField(verbose_name='отвечать')

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = 'Часто задаваемые вопросы'


class Partner(BaseModel):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    text = RichTextField(verbose_name='текст')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Партнерам'
        verbose_name_plural = 'Партнерам'
