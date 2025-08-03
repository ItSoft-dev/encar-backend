from django.contrib import admin 

from core.apps.cars.models import Like, Comparison


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'car']


@admin.register(Comparison)
class ComparisonAdmin(admin.ModelAdmin):
    list_display = ['user']
