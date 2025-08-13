from django.shortcuts import get_object_or_404

from rest_framework import views, generics
from rest_framework.response import Response

from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import car_pricing as serializers
from core.apps.cars.models import Car, CarPricing


class AdminCarPricingCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminCarPricingSerializer
    queryset = CarPricing.objects.all()
    permission_classes = [AdminPermission]


class AdminCarPricingApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        pricing = CarPricing.objects.filter(car=car)
        serializer = serializers.AdminCarPricingSerializer(pricing, many=True)
        return Response(serializer.data, status=200)
    

class AdminCarPricingUpdateApiView(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = CarPricing.objects.all()
    serializer_class = serializers.AdminCarPricingSerializer
    lookup_field = 'id'



class AdminCarPricingDeleteApiView(generics.DestroyAPIView):
    permission_classes = [AdminPermission]
    queryset = CarPricing.objects.all()
    lookup_field = 'id'

    