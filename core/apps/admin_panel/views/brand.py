from time import time

from django.shortcuts import get_object_or_404

from rest_framework import views, generics, parsers
from rest_framework.response import Response

from core.apps.admin_panel.serializers import brand as serializers
from core.apps.cars.models import Brand
from core.apps.admin_panel.permissions.admin_permission import AdminPermission

class AdminBrandListApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request):
        queryset = Brand.objects.all()  # pagination bilan sinab ko‘ring
        serializer = serializers.AdminBrandSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class AdminBrandCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminBrandCreateSerializer
    queryset = Brand.objects.all()
    permission_classes = [AdminPermission]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class AdminBrandUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminBrandUpdateSerializer
    queryset = Brand.objects.all()
    lookup_field = 'id'
    permission_classes = [AdminPermission]
    parser_classes = []


class AdminBrandDeleteApiView(views.APIView):
    permission_classes = [AdminPermission]

    def delete(self, request, id):
        brand = get_object_or_404(Brand, id=id)
        brand.delete()
        return Response({'success': True}, status=204)