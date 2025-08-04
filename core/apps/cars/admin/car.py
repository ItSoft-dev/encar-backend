from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from core.apps.cars.models.car import Car, CarMedia, CarInteryer, CarMultimedia, CarSafety, CarSeats, CarPricing, CarInspection, CarInspectionIncident, InspectionField, InspectionSection


class CarMediaInline(admin.TabularInline):
    model = CarMedia
    extra = 0


class CarInteryerInline(admin.StackedInline):
    model = CarInteryer 
    extra = 0


class CarMultimediaInline(admin.StackedInline):
    model = CarMultimedia 
    extra = 0


class CarSafetyInline(admin.StackedInline):
    model = CarSafety 
    extra = 0


class CarSeatsInline(admin.StackedInline):
    model = CarSeats 
    extra = 0


class CarPricingInline(admin.StackedInline):
    model = CarPricing
    extra = 0


class CarInspectionInline(admin.StackedInline):
    model = CarInspection
    extra = 0
    readonly_fields = ['link']

    def link(self, obj):
        if obj.pk:
            url = reverse('admin:cars_carinspection_change', args=[obj.pk])
            return format_html('<a href="{}" target="_blank">Tahrirlash</a>', url)
        return "-"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'price', 'color', 'year', 'month']
    list_filter = ['brand', 'model', 'generation', 'fuel_type', 'body_type', 'transmission','color']
    inlines = [
        CarMediaInline, CarInteryerInline, CarSeatsInline, CarSafetyInline, CarMultimediaInline,
        CarPricingInline, CarInspectionInline
    ]


@admin.register(CarMedia)
class CarMediaAdmin(admin.ModelAdmin):
    list_display = ['car', 'media']


class CarInspectionIncidentInline(admin.TabularInline):
    model = CarInspectionIncident
    extra = 0


class InspectionFieldInline(admin.TabularInline):
    model = InspectionField
    extra = 0


class InspectionSectionInline(admin.StackedInline):
    model = InspectionSection
    extra = 0

    readonly_fields = ['link']

    def link(self, obj):
        if obj.pk:
            url = reverse('admin:cars_inspectionsection_change', args=[obj.pk])
            return format_html('<a href="{}" target="_blank">Tahrirlash</a>', url)
        return "-"


@admin.register(CarInspection)
class CarInspectionAdmin(admin.ModelAdmin):
    list_display = ['car', 'inspection_date', 'diagnosis_date', 'vin', 'engine_type']
    search_fields = ['car__brand', 'car__model', 'vin']
    list_filter = ['inspection_date', 'engine_type']
    inlines = [CarInspectionIncidentInline, InspectionSectionInline]
    fieldsets = (
        ('Основные данные', {
            'fields': (
                'car', 'inspection_date', 'diagnosis_date', 'vin',
                'engine_type', 'year', 'incidents', 'usage_type',
            )
        }),
        ('Состояние кузова', {
            'fields': (
                'front_left_door', 'front_right_door',
                'rear_left_door', 'rear_right_door',
                'hood', 'trunk',
            )
        }),
    )


@admin.register(InspectionSection)
class InspectionSectionAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

    inlines = [InspectionFieldInline]


@admin.register(CarInspectionIncident)
class CarInspectionIncidentAdmin(admin.ModelAdmin):
    
    def has_module_permission(self, request):
        return False



@admin.register(InspectionField)
class InspectionFieldAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        return False
