from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.cars'

    def ready(self):
        from . import admin
        from core.apps.cars import signals