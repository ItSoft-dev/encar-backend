from django.shortcuts import get_object_or_404

from rest_framework import generics, views
from rest_framework.response import Response

from core.apps.admin_panel.serializers import generation as serializers
from core.apps.cars.models import Generation, Model
from core.apps.admin_panel.permissions.admin_permission import AdminPermission


class AdminGenerationListApiView(generics.ListAPIView):
    serializer_class = serializers.AdminGenerationSerializer
    queryset = Generation.objects.all()
    permission_classes = [AdminPermission]


class AdminGenerationListByModelApiView(views.APIView):
    permission_classes = [AdminPermission]

    def get(self, request, model_id):
        model = get_object_or_404(Model, id=model_id)
        generations = Generation.objects.filter(model=model)
        serializer = serializers.AdminGenerationSerializer(generations, many=True)
        return Response(serializer.data, status=200)
    

class AdminGenerationCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.AdminGenerationCreateUpdateSerializer
    queryset = Generation.objects.all()
    permission_classes = [AdminPermission]


class AdminGenerationUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.AdminGenerationCreateUpdateSerializer
    queryset = Generation.objects.all()
    permission_classes = [AdminPermission]
    lookup_field = 'id'


class AdminGenerationDeleteApiView(generics.DestroyAPIView):
    serializer_class = None
    queryset = Generation.objects.all()
    lookup_field = 'id'
    permission_classes = [AdminPermission]
