from django.db import models

from core.apps.shared.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=200, db_index=True)
    icon = models.ImageField(upload_to='brand/icons/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'


class Model(BaseModel):
    name = models.CharField(max_length=200, db_index=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'модели'


class Generation(BaseModel):
    name = models.CharField(max_length=200, db_index=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='generations')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'поколение'
        verbose_name_plural = 'поколение'


class Transmission(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Трансмиссия'
        verbose_name_plural = 'Трансмиссии'


class BodyType(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Тип кузова'


class FuelType(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'тип топлива'
        verbose_name_plural = 'тип топлива'


class Color(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвет'