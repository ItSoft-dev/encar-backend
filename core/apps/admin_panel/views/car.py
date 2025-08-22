from rest_framework import generics, views, parsers
from rest_framework.response import Response

from core.apps.admin_panel.serializers import car as serializers
from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.cars.models import Car
from core.apps.shared.pagination.custom import CustomPageNumberPagination


class AdminCarListApiView(generics.ListAPIView):
    serializer_class = serializers.AdminCarListSerializer
    permission_classes = [AdminPermission]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Car.objects.filter(region=self.request.user.region).select_related(
        'color', 'brand', 'body_type', 'fuel_type', 'transmission'
    )


class AdminCarCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminCarCreateSerializer
    queryset = Car.objects.all()
    permission_classes = [AdminPermission]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        user = self.request.user
        if user.is_authenticated:
            context['region'] = getattr(user, 'region', None)
        else:
            context['region'] = None
        return context
    

class AdminCarDeleteApiView(generics.DestroyAPIView):
    serializer_class = None
    queryset = Car.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'


class AdminCarDetailApiView(generics.RetrieveAPIView):
    serializer_class = serializers.AdminCarDetailSerializer
    queryset = Car.objects.select_related(
        'color', 'body_type', 'fuel_type', 'transmission', 'brand', 'model', 'generation'
    )
    permission_classes = [AdminPermission]
    lookup_field = 'id'


class AdminCarUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminCarDetailSerializer
    permission_classes = [AdminPermission]
    lookup_field = 'id'

    def get_queryset(self):
        return Car.objects.filter(region=self.request.user.region)