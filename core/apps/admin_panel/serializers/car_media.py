from rest_framework import serializers

from core.apps.cars.models import CarMedia


class AdminCarMediaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMedia
        fields = ['car', 'media']


class AdminCarMediaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMedia
        fields = ['id', 'car', 'media']


class AdminCarMediaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMedia
        fields = ['id', 'media']