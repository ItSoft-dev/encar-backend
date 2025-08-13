from django.urls import path, include

from core.apps.admin_panel.views import user as user_views
from core.apps.admin_panel.views import brand as brand_views
from core.apps.admin_panel.views import model as model_views
from core.apps.admin_panel.views import generation as generation_views
from core.apps.admin_panel.views import color as color_views
from core.apps.admin_panel.views import body_type as body_type_views
from core.apps.admin_panel.views import fuel_type as fuel_type_views
from core.apps.admin_panel.views import transmission as transmission_views


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
]