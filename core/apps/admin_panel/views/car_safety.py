from django.shortcuts import get_object_or_404

from rest_framework import generics, views
from rest_framework.response import Response

from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import car_safety as serializers
from core.apps.cars.models import CarSafety, Car


class AdminCarSafetyCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminCarSafetySerializer
    queryset = CarSafety.objects.all()
    permission_classes = [AdminPermission]


class AdminCarSafetyApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        safety = CarSafety.objects.filter(car=car)
        serializer = serializers.AdminCarSafetySerializer(safety, many=True)
        return Response(serializer.data, status=200)
    

class AdminCarSafetyUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminCarSafetySerializer
    queryset = CarSafety.objects.all()
    lookup_field = 'id'
    permission_classes = [AdminPermission]


class AdminCarSafetyDeleteApiView(generics.DestroyAPIView):
    serializer_class = None
    queryset = CarSafety.objects.all()
    lookup_field = 'id'
    permission_classes = [AdminPermission]

