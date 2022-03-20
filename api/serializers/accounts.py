from rest_framework import serializers

from accounts.models import MemberProfile, Account
from .locations import LocationSerializer


class MemberProfileSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = MemberProfile
        fields = ["phone_number", "location", "address"]


class AuthUserSerializer(serializers.ModelSerializer):
    profile = MemberProfileSerializer(read_only=True)

    class Meta:
        model = Account
        fields = ["id", "name", 'email', 'is_member', "is_active", "created_at", "profile"]
