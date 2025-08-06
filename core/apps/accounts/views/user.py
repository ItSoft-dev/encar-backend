from rest_framework import generics, status, permissions
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from core.apps.accounts.serializers import user as serializers
from core.apps.accounts.models import User
from core.apps.accounts.permissions.custom import IsAuthenticatedUser


class RegisterApiView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            return Response({'refresh': str(token), 'access': str(token.access_token)}, status=201)
        return Response(serializer.errors, 400)


class UserProfileApiView(generics.GenericAPIView):
    serializer_class = serializers.UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedUser]

    def get(self, request):
        user = request.user
        print(user.is_authenticated)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=200)


class UserProfileUpdateApiView(generics.GenericAPIView):
    serializer_class = serializers.UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedUser]

    def put(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "profile updated!"}, status=200)
        return Response(serializer.errors, status=400)

    
class WhoAmI(generics.GenericAPIView):
    serializer_class = None
    queryset = None
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(
            {
                'username': request.user.username,
                'id': request.user.id
            }
        )