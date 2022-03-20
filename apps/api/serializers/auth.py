from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .accounts import AuthUserSerializer


class JWTAuthSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user_serializer = AuthUserSerializer(instance=self.user)
        data["user"] = user_serializer.data
        return data


class ApiLoginResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    user = AuthUserSerializer()

    def create(self, validated_data):
        raise NotImplementedError()  # pragma: no cover

    def update(self, instance, validated_data):
        raise NotImplementedError()  # pragma: no cover
