from rest_framework import serializers

from core.apps.cars.models import Transmission


class AdminTransmissionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ['id', 'name']
        