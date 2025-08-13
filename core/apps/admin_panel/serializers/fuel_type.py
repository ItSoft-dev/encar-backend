from rest_framework import serializers

from core.apps.cars.models import FuelType


class AdminFuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = ['id', 'name']