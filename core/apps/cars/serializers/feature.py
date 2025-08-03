from rest_framework import serializers

from core.apps.cars.models import feture as models


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Generation
        fields = [
            'id', 'name'
        ]


class ModelSerializer(serializers.ModelSerializer):
    generations = GenerationSerializer(many=True)

    class Meta:
        model = models.Model
        fields = [
            'id', 'name', 'generations'
        ]


class BrandSerializer(serializers.ModelSerializer):
    models = ModelSerializer(many=True)

    class Meta:
        model = models.Brand
        fields = [
            'id', 'name', 'icon', 'models'
        ]


class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transmission
        fields = ['id', 'name']


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BodyType
        fields = ['id', 'name']
        

class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FuelType
        fields = ['id', 'name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = ['id', 'name']
        