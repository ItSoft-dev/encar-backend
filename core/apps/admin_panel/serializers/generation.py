from rest_framework import serializers

from core.apps.cars.models import Generation


class AdminGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generation
        fields = ['id', 'name']