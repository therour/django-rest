from rest_framework import serializers
from accounts.models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "name", 'email', 'is_member', "is_active", "created_at")


class JWTAuthSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user_serializer = AuthUserSerializer(instance=self.user)
        data["data"] = user_serializer.data
        return data
