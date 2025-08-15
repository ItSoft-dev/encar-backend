from rest_framework import serializers

from core.apps.cars.models import CarInspection


class AdminCarInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInspection
        fields = [
            'id', 'car', 'inspection_date', 'diagnosis_date', 'vin', 'engine_type', 'incidents', 
            'year', 'usage_type', 'front_left_door', 'front_right_door', 'rear_left_door', 'trunk',
            'rear_right_door', 'hood',
        ]