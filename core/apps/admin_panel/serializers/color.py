from rest_framework import serializers

from core.apps.cars.models import Color


class AdminColorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']
    