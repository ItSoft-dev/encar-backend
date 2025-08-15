from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import generics, views

from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import car_inspection as serializers
from core.apps.cars.models import Car, CarInspection


class AdminCarInpspectionCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminCarInspectionSerializer
    queryset = CarInspection.objects.all()
    permission_classes = [AdminPermission]


class AdminCarInspectionListByCarIdApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        car_inspection = CarInspection.objects.filter(car=car)
        serializer = serializers.AdminCarInspectionSerializer(car_inspection, many=True)
        return Response(serializer.data, status=200)
    

class AdminCarInspectionUpdateApiView(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = CarInspection.objects.all()
    lookup_field = 'id'
    serializer_class = serializers.AdminCarInspectionSerializer


class AdminCarInspectionDeleteApiView(generics.DestroyAPIView):
    permission_classes = [AdminPermission]
    queryset = CarInspection.objects.all()
    lookup_field = 'id'
    serializer_class = serializers.AdminCarInspectionSerializer
