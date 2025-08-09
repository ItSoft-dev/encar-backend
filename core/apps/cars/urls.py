from django.urls import path

from core.apps.cars.views import feature as feature_views
from core.apps.cars.views import car as car_views
from core.apps.cars.views import like as like_views


urlpatterns = [
    path('brand/list/', feature_views.BrandListApiView.as_view()),
    path('transmission/list/', feature_views.TransmissionListApiView.as_view()),
    path('body_type/list/', feature_views.BodyTypeListApiView.as_view()),
    path('fuel_type/list/', feature_views.FuelTypeListApiView.as_view()),
    path('color/list/', feature_views.ColorListApiView.as_view()),

    path('car/list/', car_views.CarListApiView.as_view()),
    path('car/<uuid:id>/similar/', car_views.CarSimilarApiView.as_view()),
    path('car/<uuid:id>/', car_views.CarDetailApiView.as_view()),

    path('like/<uuid:car_id>/', like_views.LikeApiView.as_view()),
    path('like/cars/', like_views.LikedCarListApiView.as_view()),

    path('comparison/<uuid:car_id>/', like_views.ComparisonApiView.as_view()),
    path('comparison/list/', like_views.ComparisonListApiView.as_view()),
    path('region/list/', car_views.RegionListApiView.as_view()),
]