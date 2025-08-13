from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import generics, views

from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.admin_panel.serializers import car_multimedia as serializers
from core.apps.cars.models import Car, CarMultimedia



class AdminCarMultimediaCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminCarMultimediaSerializer
    queryset = CarMultimedia.objects.all()
    permission_classes = [AdminPermission]


class AdminCarMultimediaApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        multimedia = CarMultimedia.objects.filter(car=car)
        serializer = serializers.AdminCarMultimediaSerializer(multimedia, many=True)
        return Response(serializer.data, status=200)
    

class AdminCarMultimediaUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminCarMultimediaSerializer
    queryset = CarMultimedia.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'
    

class AdminCarMultimediaDeleteApiView(generics.RetrieveAPIView):
    serializer_class = serializers.AdminCarMultimediaSerializer
    queryset = CarMultimedia.objects.all()
    lookup_field = 'id'
    permission_classes = [AdminPermission]

