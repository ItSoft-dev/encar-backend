from django.urls import path

from core.apps.cars.views import feature as feature_views
from core.apps.cars.views import car as car_views


urlpatterns = [
    path('brand/list/', feature_views.BrandListApiView.as_view()),
    path('transmission/list/', feature_views.TransmissionListApiView.as_view()),
    path('body_type/list/', feature_views.BodyTypeListApiView.as_view()),
    path('fuel_type/list/', feature_views.FuelTypeListApiView.as_view()),
    path('color/list/', feature_views.ColorListApiView.as_view()),

    path('car/list/', car_views.CarListApiView.as_view()),
    path('car/<uuid:id>/', car_views.CarDetailApiView.as_view()),
]