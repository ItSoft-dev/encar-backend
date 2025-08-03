from django.contrib import admin 
from django.utils.html import format_html
from django.urls import reverse

from core.apps.cars.models import feture as models


class ModelInline(admin.TabularInline):
    model = models.Model
    extra = 0
    readonly_fields = ['link']

    def link(self, obj):
        if obj.pk:
            url = reverse('admin:cars_model_change', args=[obj.pk])
            return format_html('<a href="{}" target="_blank">Tahrirlash</a>', url)
        return "-"


class GenerationInline(admin.TabularInline):
    model = models.Generation
    extra = 0


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

    inlines = [ModelInline]


@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    inlines = [GenerationInline]

    def has_module_permission(self, request):
        return False


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