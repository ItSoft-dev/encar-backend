from django.contrib import admin

from core.apps.cars.models.car import Car, CarMedia, CarInteryer, CarMultimedia, CarSafety, CarSeats


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


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'price', 'color', 'year', 'month']
    list_filter = ['brand', 'model', 'generation', 'fuel_type', 'body_type', 'transmission','color']
    inlines = [
        CarMediaInline, CarInteryerInline, CarSeatsInline, CarSafetyInline, CarMultimediaInline
    ]


@admin.register(CarMedia)
class CarMediaAdmin(admin.ModelAdmin):
    list_display = ['car', 'media']
