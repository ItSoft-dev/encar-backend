from rest_framework import generics, views

from core.apps.cars.models import Transmission
from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import transmission as serializers



class TransmissionListApiView(generics.ListAPIView):
    serializer_class = serializers.AdminTransmissionListSerializer
    queryset = Transmission.objects.all()
    permission_classes = [AdminPermission]

    