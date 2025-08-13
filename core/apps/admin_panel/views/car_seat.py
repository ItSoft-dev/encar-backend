from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import generics, views

from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import car_seats as serializers
from core.apps.cars.models import CarSeats, Car


class CarSeatCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.CarSeatSerializer
    queryset = CarSeats.objects.all()
    permission_classes = [AdminPermission]


class CarSeatListApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        seat = CarSeats.objects.filter(car=car)
        serializer = serializers.CarSeatSerializer(seat, many=True)
        return Response(serializer.data, status=200)


class CarSeatDeleteApiView(generics.DestroyAPIView):
    lookup_field = 'id'
    permission_classes = [AdminPermission]
    queryset = CarSeats.objects.all()
    serializer_class = None
        
    
class CarSeatUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.CarSeatSerializer
    queryset = CarSeats.objects.all()
    permission_classes = [AdminPermission]
