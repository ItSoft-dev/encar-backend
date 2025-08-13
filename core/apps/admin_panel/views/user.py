from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, views
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken 

from core.apps.accounts.models import User
from core.apps.admin_panel.serializers import user as serializers


class LoginApiView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            user = get_object_or_404(User, email=email, role='admin')
            if not user.check_password(serializer.validated_data.get('password')):
                return Response({"message": "User not found"}, status=200)
            token = RefreshToken.for_user(user)
            return Response(
                {
                    'access': str(token.access_token),
                    'refresh': str(token),
                    'role': user.role,
                    'region': user.region.name if user.region else None
                }, status=200
            )
        return Response(serializer.errors, status=400)