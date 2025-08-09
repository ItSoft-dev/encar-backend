from rest_framework import generics, status
from rest_framework.response import Response
from core.apps.accounts.serializers.forgot_password import ForgotPasswordSerializer, ResetPasswordSerializer


class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        link = serializer.save()
        return Response({"message": "Reset link emailingizga yuborildi", "link": link}, status=status.HTTP_200_OK)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Parol muvaffaqiyatli o'zgartirildi"}, status=status.HTTP_200_OK)
