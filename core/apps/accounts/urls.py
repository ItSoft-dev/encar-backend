from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.apps.accounts.views import user as user_views


urlpatterns = [
    path('register/', user_views.RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('profile/', user_views.UserProfileApiView.as_view()),
    path('profile/update/', user_views.UserProfileUpdateApiView.as_view()),
]