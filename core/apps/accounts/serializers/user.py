from django.db import transaction

from rest_framework import serializers

from core.apps.accounts.models import User


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists")
        return value
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Two password must be same")
        return data
    
    def create(self, validated_data):
        with transaction.atomic():
            email = validated_data.get('email')
            full_name = email.split('@')[0] if email else ''
            user = User.objects.create(
                email=validated_data.get('email'),
                role='user',
                full_name=full_name
            )
            user.set_password(validated_data.get('password'))
            user.save()
            return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'full_name', 'phone', 'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone = validated_data.get('phone', instance.phone)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance