from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from django.core.mail import send_mail

from rest_framework import serializers

from core.apps.accounts.models import User
from core.apps.shared.models import SiteConfig

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Bunday email topilmadi")
        return value

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        uidb64 = user.pk
        token = PasswordResetTokenGenerator().make_token(user)
        reset_link = f"{settings.FRONTEND_URL}/{uidb64}/{token}/"
        config = SiteConfig.objects.first()
        send_mail(
            "Сброс пароля",
            f"Чтобы сбросить пароль, перейдите по этой ссылке:\n{reset_link}",
            config.email_host,
            [email],
            fail_silently=False,
            auth_user=config.email_host,
            auth_password=config.email_host_password,
        )
        return reset_link


class ResetPasswordSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    
    def validate(self, data):
        try:
            uid = data['uidb64']
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            raise serializers.ValidationError("Noto‘g‘ri link")

        if not PasswordResetTokenGenerator().check_token(user, data['token']):
            raise serializers.ValidationError("Token noto‘g‘ri yoki muddati tugagan")

        data['user'] = user
        return data

    def save(self):
        user = self.validated_data['user']
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
