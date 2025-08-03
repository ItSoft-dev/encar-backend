from django.db import models

from core.apps.shared.models import BaseModel
from core.apps.cars.models import Car
from core.apps.accounts.models import User


class Like(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.car} liked {self.user}"
    
    class Meta:
        verbose_name = 'Лайк'              
        verbose_name_plural = 'Лайки'  
        unique_together = ("user", 'car')


class Comparison(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comparisons')
    cars = models.ManyToManyField(Car, related_name='comparisons')

    def __str__(self):
        return f'{self.user} comparisons'
    
    class Meta:
        verbose_name = 'Сравнение'
        verbose_name_plural = 'Сравнения'