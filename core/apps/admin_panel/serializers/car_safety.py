from rest_framework import serializers

from core.apps.cars.models import CarSafety


class AdminCarSafetySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSafety
        fields = [
            'id', 'car', 'epb', 'automatic_ac', 'smart_key', 'wireless_door_lock', 'rain_sensor',
            'auto_light', 'navigation', 'bluetooth', 'usb_port'
        ]