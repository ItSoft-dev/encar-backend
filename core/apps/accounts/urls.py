from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.apps.accounts.views import user as user_views
from core.apps.accounts.views.forgot_password import ForgotPasswordView, ResetPasswordView


urlpatterns = [
    path('register/', user_views.RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('profile/', user_views.UserProfileApiView.as_view()),
    path('profile/update/', user_views.UserProfileUpdateApiView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]