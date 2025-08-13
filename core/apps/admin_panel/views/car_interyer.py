from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import generics, views

from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import car_interyer as serializers
from core.apps.cars.models import Car, CarInteryer


class CarInteryerCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminCarInteryerCreateSerializer
    queryset = CarInteryer.objects.all()
    permission_classes = [AdminPermission]


class CarInteryerApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        interyer = CarInteryer.objects.filter(car=car)
        serializer = serializers.AdminCarInterterSerializer(interyer, many=True)
        return Response(serializer.data, status=200)
    

class CarInteryerDeleteApiView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = CarInteryer.objects.all()
    serializer_class = None
    permission_classes = [AdminPermission]


class CarInteryerUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminCarInterterSerializer
    queryset = CarInteryer.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'