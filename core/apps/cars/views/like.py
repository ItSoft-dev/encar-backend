from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from core.apps.cars.models import Like, Comparison, Car
from core.apps.cars.serializers.car import CarListSerializer
from core.apps.shared.pagination.custom import CustomPageNumberPagination

class LikeApiView(generics.GenericAPIView):
    serializer_class = None
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, car_id):
        print("Headers", request.headers)
        car = get_object_or_404(Car, id=car_id)
        like, created = Like.objects.get_or_create(car=car, user=request.user)
        if not created:
            like.delete()
            return Response({'message': 'unliked'}, status=200)
        return Response({'message': 'liked'}, status=200)

class LikedCarListApiView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Car.objects.filter(
        likes__user=self.request.user
        ).select_related(
            'fuel_type', 'color'
        ).prefetch_related(
            'car_medias', 'likes', 'comparisons'
        ).distinct()


class ComparisonApiView(generics.GenericAPIView):
    serializer_class = None
    queryset = Comparison.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        comparison, created = Comparison.objects.get_or_create(user=request.user)

        if car in comparison.cars.all():
            comparison.cars.remove(car)
            return Response({"in_comparison": True})
        comparison.cars.add(car)
        return Response({"in_comparison": False})


class ComparisonListApiView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Comparison.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Car.objects.filter(comparisons__user=self.request.user).select_related(
            'fuel_type', 'color',
        ).prefetch_related('car_medias', 'likes', 'comparisons').distinct()
