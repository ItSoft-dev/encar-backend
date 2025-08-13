from rest_framework import serializers

from core.apps.cars.models import Model


class AdminModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'name']
    

class AdminModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['name', 'brand']

    def create(self, validated_data):
        return Model.objects.create(**validated_data)