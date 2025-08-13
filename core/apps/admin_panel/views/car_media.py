from django.shortcuts import get_object_or_404

from rest_framework import generics, views, parsers
from rest_framework.response import Response

from core.apps.admin_panel.serializers import car_media as serializers
from core.apps.admin_panel.permissions.admin_permission import AdminPermission
from core.apps.cars.models import CarMedia, Car


class AdminCarMediaCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminCarMediaCreateSerializer
    permission_classes = [AdminPermission]
    queryset = CarMedia.objects.all()
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class AdminCarMediaListApiView(views.APIView):
    permission_classes = [AdminPermission]
    
    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        medias = CarMedia.objects.filter(car=car)
        serializer = serializers.AdminCarMediaListSerializer(medias, many=True)
        return Response(serializer.data, status=200)
    

class AdminCarMediaUpdateApiView(generics.UpdateAPIView):
    serializer_classr = serializers.AdminCarMediaUpdateSerializer
    queryset = CarMedia.objects.all()
    lookup_field = 'id'
    permission_classes = [AdminPermission]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class AdminCarMediaDeleteApiView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = None
    permission_classes = [AdminPermission]
    queryset = CarMedia.objects.all()


