from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from core.apps.cars.models import Car, Region
from core.apps.cars.serializers import car as serializers
from core.apps.shared.pagination.custom import CustomPageNumberPagination
from core.apps.cars.filters.car import CarFilter


class CarListApiView(generics.ListAPIView):
    serializer_class = serializers.CarListSerializer
    queryset = Car.objects.select_related(
        'brand', 'model', 'generation', 'fuel_type', 'color'
    ).prefetch_related('likes', 'comparisons', 'car_medias').exclude(is_sold=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        return context


class CarDetailApiView(generics.RetrieveAPIView):
    serializer_class = serializers.CarDeatilSerializer
    queryset = Car.objects.select_related(
        'brand', 'model', 'generation', 'fuel_type', 'body_type', 'transmission', 'color',
        'car_interyer', 'car_multimedia', 'car_safety', 'car_seats', 'car_pricing', 'car_inspections'
    ).prefetch_related('car_medias', 'likes', 'comparisons')
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        return context
    
class CarSimilarApiView(generics.GenericAPIView):
    serializer_class = serializers.CarListSerializer
    queryset = Car.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        car = get_object_or_404(Car, id=id)
        cars = Car.objects.filter(brand=car.brand, fuel_type=car.fuel_type)[:6]
        serializer = self.serializer_class(cars, many=True)
        return Response(serializer.data, status=200)
    

class RegionListApiView(generics.ListAPIView):
    serializer_class = serializers.RegionListSerializer
    queryset = Region.objects.all()
