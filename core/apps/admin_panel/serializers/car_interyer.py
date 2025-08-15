from rest_framework import serializers

from core.apps.cars.models import CarInteryer


class AdminCarInteryerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInteryer
        fields = [
            'side_airbag', 'curtain_airbag', 'abs', 'traction_control', 
            'esc', 'tpms', 'ldws', 'rear_view_camera', 'car'
        ]


class AdminCarInterterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInteryer
        fields = [
            'id', 'side_airbag', 'curtain_airbag', 'abs', 'traction_control', 
            'esc', 'tpms', 'ldws', 'rear_view_camera',
        ]
