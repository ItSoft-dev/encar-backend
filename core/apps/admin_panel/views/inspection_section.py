from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import views, generics

from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import inspection_section as serializers
from core.apps.cars.models import CarInspection, InspectionSection


class AdminInspectionSectionCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminInspectionSectionSerializer
    queryset = InspectionSection.objects.all()
    permission_classes = [AdminPermission]


class AdminInspectionSectionListApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, car_inspection_id):
        car_inspection = get_object_or_404(CarInspection, id=car_inspection_id)
        inspection_sections = InspectionSection.objects.filter(inspection=car_inspection)
        serializer = serializers.AdminInspectionSectionSerializer(inspection_sections, many=True)
        return Response(serializer.data, status=200)


class AdminInspectionSectionUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminInspectionSectionSerializer
    queryset = InspectionSection.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'


class AdminInspectionSectionDeleteApiView(generics.DestroyAPIView):
    serializer_class = serializers.AdminInspectionSectionSerializer
    queryset = InspectionSection.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'