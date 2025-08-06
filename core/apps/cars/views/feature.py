from rest_framework import generics, status, permissions
from rest_framework.response import Response

from core.apps.cars.serializers import feature as serializers
from core.apps.cars.models import feture as models


class BrandListApiView(generics.ListAPIView):
    serializer_class = serializers.BrandSerializer
    queryset = models.Brand.objects.prefetch_related('models').order_by('name')
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TransmissionListApiView(generics.ListAPIView):
    serializer_class = serializers.TransmissionSerializer
    queryset = models.Transmission.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BodyTypeListApiView(generics.ListAPIView):
    serializer_class = serializers.BodyTypeSerializer
    queryset = models.BodyType.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FuelTypeListApiView(generics.ListAPIView):
    serializer_class = serializers.FuelTypeSerializer
    queryset = models.FuelType.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ColorListApiView(generics.ListAPIView):
    serializer_class = serializers.ColorSerializer
    queryset = models.Color.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


