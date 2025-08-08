from django.db import models

from ckeditor.fields import RichTextField

from core.apps.shared.models import BaseModel


class Contact(BaseModel):
    text = RichTextField(verbose_name='текст')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class OfferAgreement(BaseModel):
    text = RichTextField(verbose_name='текст')

    class Meta:
        verbose_name = 'Договор-оферта'
        verbose_name_plural = 'Договор-оферта'


class PrivacyPolicy(BaseModel):
    text = RichTextField(verbose_name='текст')

    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'


class ReturnPolicy(BaseModel):
    text = RichTextField(verbose_name='текст')

    class Meta:
        verbose_name = 'Политика возврата'
        verbose_name_plural = 'Политика возврата'


class Disclaimer(BaseModel):
    text = RichTextField(verbose_name='текст')

    class Meta:
        verbose_name = 'Отказ от ответственности'
        verbose_name_plural = 'Отказ от ответственности'


class AboutProject(BaseModel):
    text = RichTextField(verbose_name='текст')

    class Meta:
        verbose_name = 'О проекте'
        verbose_name_plural = 'О проекте'


class FeedBack(BaseModel):
    text = RichTextField(verbose_name='текст')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'