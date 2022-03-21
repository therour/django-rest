from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.accounts.models import Account, MemberProfile
from apps.geolocation.models import GeoLocation
from .accounts import AuthUserSerializer, MemberProfileSerializer


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


class ApiRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=Account.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    address = serializers.CharField(write_only=True, required=True, max_length=255)
    location = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(
        write_only=True,
        required=True,
        max_length=20,
        validators=[UniqueValidator(queryset=MemberProfile.objects.all())],
    )
    profile = MemberProfileSerializer(read_only=True)

    class Meta:
        model = Account
        fields = (
            "id",
            "name",
            "email",
            "password",
            "is_member",
            "is_active",
            "created_at",
            "address",
            "phone_number",
            "location",
            "profile",
        )
        extra_kwargs = {
            "name": {"required": True},
            "id": {"read_only": True},
            "is_member": {"read_only": True},
            "is_active": {"read_only": True},
            "created_at": {"read_only": True},
        }

    def validate_location(self, value):
        try:
            return GeoLocation.objects.get(pk=value)
        except GeoLocation.DoesNotExist:
            raise serializers.ValidationError("Invalid location")

    def create(self, validated_data):
        with transaction.atomic():
            user = Account.objects.create_user(
                name=validated_data["name"],
                email=validated_data["email"],
                password=validated_data["password"],
                is_member=True,
                is_active=False,
            )

            MemberProfile(
                account=user,
                address=validated_data["address"],
                phone_number=validated_data["phone_number"],
                location=validated_data["location"],
            ).save()

            return user
