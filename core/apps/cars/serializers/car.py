from rest_framework import serializers

from core.apps.cars.models import (
    Car, CarMedia, CarInteryer, CarMultimedia, CarSafety, CarSeats, CarPricing, CarInspectionIncident, CarInspection, InspectionSection, InspectionField, Like, Comparison,
    Region
)

class CarMediaLiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMedia 
        fields = [
            'id', 'media'
        ]


class CarListSerializer(serializers.ModelSerializer):
    fuel_type = serializers.SerializerMethodField(method_name='get_fuel_type')
    color = serializers.SerializerMethodField(method_name='get_color')
    like = serializers.SerializerMethodField(method_name='get_like')
    comparison = serializers.SerializerMethodField(method_name='get_comparison')
    car_medias = CarMediaLiserSerializer(many=True)
    
    class Meta:
        model = Car
        fields = [
            'id', 'name', 'fuel_type', 'color','price', 'year', 'miliage', 'updated_at', 'like',
            'comparison', 'main_image', 'car_medias'
        ]

    def get_like(self, obj):
        return Like.objects.filter(user=self.context.get('user'), car=obj).exists()
    
    def get_comparison(self, obj):
        return Comparison.objects.filter(user=self.context.get('user'), cars=obj).exists()

    def get_fuel_type(self, obj):
        return {
            'id': obj.fuel_type.id,
            'name': obj.fuel_type.name
        }

    def get_color(self, obj):
        return {
            'id': obj.color.id,
            'name': obj.color.name
        }
    

class CarInteryerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInteryer
        fields = '__all__'


class CarMultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMultimedia
        fields = '__all__'


class CarSafetySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSafety
        fields = '__all__'
    

class CarSeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSeats
        fields = '__all__'


class CarPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPricing 
        fields = '__all__'


class CarIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInspectionIncident
        fields = ['id', 'name', 'value']


class InspectionFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionField
        fields = ['id', 'name', 'status']


class InspectionSectionSerializer(serializers.ModelSerializer):
    fields = InspectionFieldSerializer(many=True)
    class Meta:
        model = InspectionSection
        fields = [
            'id', 'title', 'fields'
        ]


class CarInspectionSerializer(serializers.ModelSerializer):
    car_incidents = CarIncidentSerializer(many=True)
    sections = InspectionSectionSerializer(many=True)

    class Meta:
        model = CarInspection
        fields = '__all__'


class CarDeatilSerializer(serializers.ModelSerializer):
    fuel_type = serializers.SerializerMethodField(method_name='get_fuel_type')
    color = serializers.SerializerMethodField(method_name='get_color')
    car_medias = CarMediaLiserSerializer(many=True)
    transmission = serializers.SerializerMethodField(method_name='get_transmission')
    body_type = serializers.SerializerMethodField(method_name='get_body_type')
    car_interyer = CarInteryerSerializer()
    car_multimedia = CarMultimediaSerializer()
    car_safety = CarSafetySerializer()
    car_seats = CarSeatsSerializer()
    car_pricing = CarPricingSerializer()
    car_inspections = CarInspectionSerializer()
    like = serializers.SerializerMethodField(method_name='get_like')
    comparison = serializers.SerializerMethodField(method_name='get_comparison')

    class Meta:
        model = Car
        fields = [
            'id', 'name', 'fuel_type', 'main_image', 'color','price', 'year', 'miliage', 'updated_at', 'car_medias', 'month','engine_capacity', 'transmission', 'body_type',
            'car_interyer', 'car_multimedia', 'car_safety', 'car_seats', 'car_pricing',
            'car_inspections', 'like', 'comparison',
        ]
    
    def get_like(self, obj):
        return Like.objects.filter(user=self.context.get('user'), car=obj).exists()
    
    def get_comparison(self, obj):
        return Comparison.objects.filter(user=self.context.get('user'), cars=obj).exists()

    def get_body_type(self, obj):
        return {
            'id': obj.body_type.id,
            'name': obj.body_type.name
        }

    def get_transmission(self, obj):
        return {
            'id': obj.transmission.id,
            'name': obj.transmission.name
        }

    def get_fuel_type(self, obj):
        return {
            'id': obj.fuel_type.id,
            'name': obj.fuel_type.name
        }

    def get_color(self, obj):
        return {
            'id': obj.color.id,
            'name': obj.color.name
        }
    

class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region 
        fields = ['id', 'name']