from rest_framework import serializers

from core.apps.cars.models import CarPricing


class AdminCarPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPricing
        fields = [
            'id', 'car', 'agent_service', 'car_cost', 'expences_in_korea', 'custom_dutie',
            'utilsbor', 'custom_broker', 'car_transporter'
        ]