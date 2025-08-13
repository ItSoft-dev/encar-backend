from rest_framework import serializers

from core.apps.cars.models import CarSeats


class CarSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSeats
        fields = [
            'id', 'car', 'seat_leather', 'seat_electric_adjustment_driver_passenger', 'seat_electric_adjustment_rear_seats', 'seat_heating_all',
            'seat_memory_all', 'seat_ventilation_driver_passenger', 'seat_ventilation_back',
            'seat_massage'
        ]
    