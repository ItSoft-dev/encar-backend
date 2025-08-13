from django.db import transaction

from rest_framework import serializers

from core.apps.cars.models import Brand


class AdminBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'icon']


class AdminBrandCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    icon = serializers.ImageField()

    def create(self, validated_data):
        with transaction.atomic():
            return Brand.objects.create(name=validated_data.get('name'), icon=validated_data.get('icon'))
        

class AdminBrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'icon']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.save()
        return instance
    