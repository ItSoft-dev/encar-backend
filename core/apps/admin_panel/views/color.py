from rest_framework import generics, views

from core.apps.admin_panel.serializers import color as serializers
from core.apps.cars.models import Color
from core.apps.admin_panel.permissions.admin_permission import AdminPermission


class AdminColorListApiView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = serializers.AdminColorListSerializer
    permission_classes = [AdminPermission]