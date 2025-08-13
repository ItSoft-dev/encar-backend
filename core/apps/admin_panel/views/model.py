from django.shortcuts import get_object_or_404

from rest_framework import views, generics
from rest_framework.response import Response

from core.apps.admin_panel.serializers import model as serializers
from core.apps.cars.models import Model, Brand
from core.apps.admin_panel.permissions.admin_permission import AdminPermission


class AdminModelByBrandListApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, brand_id):
        brand = get_object_or_404(Brand, id=brand_id)
        models = Model.objects.filter(brand__id=brand)
        serializer = serializers.AdminModelSerializer(models, many=True)
        return Response(serializer.data, status=200)
    

class AdminModelListApiView(views.APIView):
    permission_classes = [AdminPermission]
    
    def get(self, request):
        models = Model.objects.all()
        serializer = serializers.AdminModelSerializer(models, many=True)
        return Response(serializer.data, status=200)
    

class AdminModelCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminModelCreateSerializer
    queryset = Model.objects.all()
    permission_classes = [AdminPermission]


class AdminModelUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminModelCreateSerializer
    queryset = Model.objects.all()
    lookup_field = 'id'
    permission_classes = [AdminPermission]
    

class AdminModelDeleteApiView(generics.DestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = None
    lookup_field = 'id'
    permission_classes = [AdminPermission]
    