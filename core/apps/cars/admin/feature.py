from django.contrib import admin 

from core.apps.cars.models import feture as models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand']
    search_fields = ['name']


@admin.register(models.Generation)
class GenerationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model']
    search_fields = ['name']


@admin.register(models.Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(models.BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(models.FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']