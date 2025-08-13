from rest_framework import generics, views

from core.apps.cars.models import FuelType
from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import fuel_type as serializers



class FuelTypeListApiView(generics.ListAPIView):
    serializer_class = serializers.AdminFuelTypeSerializer
    queryset = FuelType.objects.all()
    permission_classes = [AdminPermission]

    