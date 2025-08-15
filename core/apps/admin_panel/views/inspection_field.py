from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import views, generics

from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import inspection_field as serializers
from core.apps.cars.models import InspectionSection, InspectionField


class AdminInspectionFieldCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminInspectionFieldSerializer
    queryset = InspectionField.objects.all()
    permission_classes = [AdminPermission]


class AdminInspectionFieldListApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, inspection_section_id):
        inspection_section = get_object_or_404(InspectionSection, id=inspection_section_id)
        inspection_fields = InspectionField.objects.filter(section=inspection_fields)
        serializer = serializers.AdminInspectionFieldSerializer(inspection_fields, many=True)
        return Response(serializer.data, status=200)
    

class AdminInspectionFieldUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminInspectionFieldSerializer
    queryset = InspectionField.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'


class AdminInspectionFieldDeleteApiView(generics.DestroyAPIView):
    serializer_class = serializers.AdminInspectionFieldSerializer
    queryset = InspectionField.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'

