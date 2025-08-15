from rest_framework import serializers

from core.apps.cars.models import InspectionField


class AdminInspectionFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionField
        fields = [
            'id', 'section', 'name', 'status'
        ]