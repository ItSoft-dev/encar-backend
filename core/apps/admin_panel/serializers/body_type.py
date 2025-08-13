from rest_framework import serializers

from core.apps.cars.models import BodyType



class AdminBodyTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ['id', 'name']