from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import views, generics

from core.apps.cars.models import CarInspection, CarInspectionIncident
from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import car_inspection_incident as serializers


class AdminCarInspectionIncidentCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminCarInspectionIncidentSerializer
    queryset = CarInspectionIncident.objects.all()
    permission_classes = [AdminPermission]


class AdminCarInspectionListByCarInspectionIdApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, car_inspection_id):
        car_inspection = get_object_or_404(CarInspection, id=car_inspection_id)
        car_inspection_incidents = CarInspectionIncident.objects.filter(inspection=car_inspection)
        serializer = serializers.AdminCarInspectionIncidentSerializer(car_inspection_incidents, many=True)
        return Response(serializer.data, status=200)
    

class AdminCarInspectionIncidentUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminCarInspectionIncidentSerializer
    queryset = CarInspectionIncident.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'


class AdminCarInspectionIncidentDeleteApiView(generics.DestroyAPIView):
    serializer_class = serializers.AdminCarInspectionIncidentSerializer
    queryset = CarInspectionIncident.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'
