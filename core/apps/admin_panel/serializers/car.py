from rest_framework import serializers

from core.apps.cars.models import Car


class AdminCarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'name', 'brand', 'model', 'generation', 'body_type', 'fuel_type', 'color', 'transmission',
            'price', 'year', 'month', 'engine_capacity', 'miliage',
        ]
    
    def create(self, validated_data):
        region = self.context.get('region')
        return Car.objects.create(region=region, **validated_data)


class AdminCarListSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    body_type = serializers.SerializerMethodField()
    fuel_type = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    transmission = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField(method_name='get_image')

    class Meta:
        model = Car
        fields = [
            'name', 'brand', 'price', 'body_type', 'fuel_type', 'color', 'transmission', 'image'
        ]

    def get_brand(self, obj):
        return {
            'id': str(obj.brand.id), 'name': obj.brand.name
        }

    def get_body_type(self, obj):
        return {'id': str(obj.body_type.id), 'name': obj.body_type.name}
    
    def get_fuel_type(self, obj):
        return {'id': str(obj.fuel_type.id), 'name': obj.fuel_type.name}
    
    def get_color(self, obj):
        return {'id': str(obj.color.id), 'name': obj.color.name}
    
    def get_transmission(self, obj):
        return {'id': str(obj.transmission.id), 'name': obj.transmission.name}
        
    def get_image(self, obj):
        media = obj.car_medias.first()
        return {
            'id': str(media.id), 'media': media.media.url
        } if media else None
    


class AdminCarDetailSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    body_type = serializers.SerializerMethodField()
    fuel_type = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    transmission = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    generation = serializers.SerializerMethodField()
    
    class Meta:
        model = Car
        fields = [
            'name', 'brand', 'price', 'body_type', 'fuel_type', 'color', 'transmission',
            'model', 'generation', 'year', 'month', 'engine_capacity', 'miliage', 'is_sold'
        ]

    def get_brand(self, obj):
        return {
            'id': str(obj.brand.id), 'name': obj.brand.name
        }

    def get_body_type(self, obj):
        return {'id': str(obj.body_type.id), 'name': obj.body_type.name}
    
    def get_fuel_type(self, obj):
        return {'id': str(obj.fuel_type.id), 'name': obj.fuel_type.name}
    
    def get_color(self, obj):
        return {'id': str(obj.color.id), 'name': obj.color.name}
    
    def get_transmission(self, obj):
        return {'id': str(obj.transmission.id), 'name': obj.transmission.name}
        
    def get_model(self, obj):
        return {'id': str(obj.model.id), 'name': obj.model.name}
    
    def get_generation(self, obj):
        return {'id': str(obj.generation.id), 'name': obj.generation.name}
    