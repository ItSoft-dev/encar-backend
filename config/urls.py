from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config.conf.drf_yasg import schema_view

from core.apps.accounts.views.user import WhoAmI

schema_view = get_schema_view(
   openapi.Info(
      title="EnCar API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="xoliqberdiyevbehruz12@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(
        [
            path('auth/', include('core.apps.accounts.urls')),
            path('cars/', include('core.apps.cars.urls')),
        ]
    )),
    path('who_am_i/', WhoAmI.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# Media and Static Files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)