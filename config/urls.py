from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(
        [
            path('auth/', include('core.apps.accounts.urls')),
            path('cars/', include('core.apps.cars.urls')),
            path('common/', include('core.apps.common.urls')),
            path('admin/', include('core.apps.admin_panel.urls')),
        ]
    )),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Media and Static Files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
