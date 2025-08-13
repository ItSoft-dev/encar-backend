from rest_framework import serializers

from core.apps.cars.models import Model


class AdminModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'name']