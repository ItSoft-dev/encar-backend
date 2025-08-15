from rest_framework import serializers

from core.apps.cars.models import InspectionSection


class AdminInspectionSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionSection
        fields = [
            'id', 'inspection', 'title'
        ]
    