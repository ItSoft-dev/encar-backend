from rest_framework import generics, permissions, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from core.apps.cars.models import Car
from core.apps.cars.serializers import car as serializers
from core.apps.shared.pagination.custom import CustomPageNumberPagination
from core.apps.cars.filters.car import CarFilter


class CarListApiView(generics.ListAPIView):
    serializer_class = serializers.CarListSerializer
    queryset = Car.objects.select_related(
        'brand', 'model', 'generation', 'fuel_type', 'color'
    ).prefetch_related(
        'car_medias', 'car_interyer', 'car_multimedia', 'car_safety', 'car_seats'
    )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter


class CarDetailApiView(generics.RetrieveAPIView):
    serializer_class = serializers.CarDeatilSerializer
    queryset = Car.objects.select_related(
        'brand', 'model', 'generation', 'fuel_type', 'body_type', 'transmission', 'color',
        'car_interyer', 'car_multimedia', 'car_safety', 'car_seats', 'car_pricing', 'car_inspections'
    ).prefetch_related('car_medias')
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]