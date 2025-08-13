from rest_framework import serializers

from core.apps.cars.models import CarMultimedia


class AdminCarMultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMultimedia
        fields = [
            'id', 'car', 'cruise_control', 'leather_seats', 'seat_electric_adjustment_front', 
            'seat_electric_adjustment_rear', 'seat_heating_front_rear', 'seat_memory_front', 
            'seat_ventilation_front', 'seat_ventilation_rear', 'massage_seats', 'abs_system',
            'rear_av_monitor', 'cd_player', 'usb_port', 'aux_port'
        ]