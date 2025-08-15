from rest_framework import serializers

from core.apps.cars.models import CarInspectionIncident


class AdminCarInspectionIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInspectionIncident
        fields = [
            'id', 'inspection', 'name', 'value',
        ]