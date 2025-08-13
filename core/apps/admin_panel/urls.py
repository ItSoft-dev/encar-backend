from django.urls import path, include

from core.apps.admin_panel.views import user as user_views
from core.apps.admin_panel.views import brand as brand_views
from core.apps.admin_panel.views import model as model_views
from core.apps.admin_panel.views import generation as generation_views
from core.apps.admin_panel.views import color as color_views
from core.apps.admin_panel.views import body_type as body_type_views
from core.apps.admin_panel.views import fuel_type as fuel_type_views
from core.apps.admin_panel.views import transmission as transmission_views
from core.apps.admin_panel.views import car as car_views
from core.apps.admin_panel.views import car_media as car_media_views
from core.apps.admin_panel.views import car_interyer as car_interyer_views
from core.apps.admin_panel.views import car_seat as car_seat_views
from core.apps.admin_panel.views import car_safety as car_safety_views
from core.apps.admin_panel.views import car_multimedia as car_multimedia_views
from core.apps.admin_panel.views import car_pricing as car_pricing_views


urlpatterns = [
    path('user/', include(
        [
            path('login/', user_views.LoginApiView.as_view()),
        ]
    )),
    path('brand/', include(
        [
            path('list/', brand_views.AdminBrandListApiView.as_view()),
            path('create/', brand_views.AdminBrandCreateApiView.as_view()),
            path('<uuid:id>/update/', brand_views.AdminBrandUpdateApiView.as_view()),
            path('<uuid:id>/delete/', brand_views.AdminBrandDeleteApiView.as_view()),
        ]
    )),
    path('model/', include(
        [
            path('<uuid:brand_id>/list/', model_views.AdminModelByBrandListApiView.as_view()),
            path('list/', model_views.AdminModelListApiView.as_view()),
            path('create/', model_views.AdminModelCreateApiView.as_view()),
            path('<uuid:id>/update/', model_views.AdminModelUpdateApiView.as_view()),
            path('<uuid:id>/delete/', model_views.AdminModelDeleteApiView.as_view()),
        ]
    )),
    path('generation/', include(
        [
            path('<uuid:model_id>/list/', generation_views.AdminGenerationListByModelApiView.as_view()),
            path('list/', generation_views.AdminGenerationListApiView.as_view()),
            path('create/', generation_views.AdminGenerationCreateApiView.as_view()),
            path('<uuid:id>/update/', generation_views.AdminGenerationUpdateApiView.as_view()),
            path('<uuid:id>/delete/', generation_views.AdminGenerationDeleteApiView.as_view()),
        ]
    )),
    path('color/', include(
        [
            path('list/', color_views.AdminColorListApiView.as_view()),
        ]
    )),
    path('body_type/', include(
        [
            path('list/', body_type_views.BodyTypeListApiView.as_view()),
        ]
    )),
    path('fuel_type/', include(
        [
            path('list/', fuel_type_views.FuelTypeListApiView.as_view()),
        ]
    )),
    path('transmission/', include(
        [
            path('list/', transmission_views.TransmissionListApiView.as_view()),
        ]
    )),
    path('car/', include(
        [
            path('list/', car_views.AdminCarListApiView.as_view()),
            path('create/', car_views.AdminCarCreateApiView.as_view()),
            path('<uuid:id>/delete/', car_views.AdminCarDeleteApiView.as_view()),
            path('<uuid:id>/', car_views.AdminCarDetailApiView.as_view()),
            path('<uuid:id>/update/', car_views.AdminCarUpdateApiView.as_view()),
        ]
    )),
    path('car_media/', include(
        [
            path('<uuid:car_id>/list/', car_media_views.AdminCarMediaListApiView.as_view()),
            path('create/', car_media_views.AdminCarMediaCreateApiView.as_view()),
            path('<uuid:id>/delete/', car_media_views.AdminCarMediaDeleteApiView.as_view()),
            path('<uuid:id>/update/', car_media_views.AdminCarMediaUpdateApiView.as_view()),
        ]
    )),
    path('car_interyer/', include(
        [
            path('<uuid:car_id>/list/', car_interyer_views.CarInteryerApiView.as_view()),
            path('<uuid:id>/delete/', car_interyer_views.CarInteryerDeleteApiView.as_view()),
            path('<uuid:id>/update/', car_interyer_views.CarInteryerUpdateApiView.as_view()),
            path('create/', car_interyer_views.CarInteryerCreateApiView.as_view()),
        ]
    )),
    path('car_seats/', include(
        [
            path('create/', car_seat_views.CarSeatCreateApiView.as_view()),
            path('<uuid:car_id>/list/', car_seat_views.CarSeatListApiView.as_view()),
            path('<uuid:id>/delete/', car_seat_views.CarSeatDeleteApiView.as_view()),
            path('<uuid:id>/update/', car_seat_views.CarSeatUpdateApiView.as_view()),
        ]
    )),
    path('car_safety/', include(
        [
            path('create/', car_safety_views.AdminCarSafetyCreateApiView.as_view()),
            path('<uuid:car_id>/list/', car_safety_views.AdminCarSafetyApiView.as_view()),
            path('<uuid:id>/delete/', car_safety_views.AdminCarSafetyDeleteApiView.as_view()),
            path('<uuid:id>/update/', car_safety_views.AdminCarSafetyUpdateApiView.as_view()),
        ]
    )),
    path('car_multimedia/', include(
        [
            path('create/', car_multimedia_views.AdminCarMultimediaCreateApiView.as_view()),
            path('<uuid:car_id>/list/', car_multimedia_views.AdminCarMultimediaApiView.as_view()),
            path('<uuid:id>/delete/', car_multimedia_views.AdminCarMultimediaDeleteApiView.as_view()),
            path('<uuid:id>/update/', car_multimedia_views.AdminCarMultimediaUpdateApiView.as_view()),
        ]
    )),
    path('car_pricing/', include(
        [
            path('create/', car_pricing_views.AdminCarPricingCreateApiView.as_view()),
            path('<uuid:car_id>/list/', car_pricing_views.AdminCarPricingApiView.as_view()),
            path('<uuid:id>/delete/', car_pricing_views.AdminCarPricingDeleteApiView.as_view()),
            path('<uuid:id>/update/', car_pricing_views.AdminCarPricingUpdateApiView.as_view()),
        ]
    ))
]