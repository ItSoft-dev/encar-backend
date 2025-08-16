from rest_framework import generics, views

from core.apps.cars.models import BodyType
from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import body_type as serializers



class BodyTypeListApiView(generics.ListAPIView):
    serializer_class = serializers.AdminBodyTypeListSerializer
    queryset = BodyType.objects.all()
    permission_classes = [AdminPermission]


class BodyTypeCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminBodyTypeListSerializer
    queryset = BodyType.objects.all()
    permission_classes = [AdminPermission]


class BodyTypeUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminBodyTypeListSerializer
    queryset = BodyType.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'


class BodyTypeDeleteApiView(generics.DestroyAPIView):
    serializer_class = serializers.AdminBodyTypeListSerializer
    queryset = BodyType.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'
