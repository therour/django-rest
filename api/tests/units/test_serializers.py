from django.test import TestCase

from api.serializers.accounts import AuthUserSerializer, MemberProfileSerializer
from api.serializers.locations import LocationSerializer
from model_factory.factories import LocationFactory, MemberUserFactory, UserFactory


class LocationSerializerTest(TestCase):
    def test_location_without_parent_serializer(self):
        location = LocationFactory()
        serialized = LocationSerializer(instance=location).data

        self.assertGreaterEqual(serialized.items(), {
            "id": str(location.id),
            "name": location.name,
            "parent": None,
        }.items())

    def test_location_with_parent_serializer(self):
        parent = LocationFactory()
        location = LocationFactory(parent=parent)
        location.refresh_from_db()
        serialized = LocationSerializer(instance=location).data

        self.assertGreaterEqual(serialized.items(), {
            "id": str(location.id),
            "name": location.name,
            "parent": LocationSerializer(instance=parent).data,
        }.items())


class MemberProfileSerializerTest(TestCase):
    maxDiff = None

    def test_member_profile_serializer(self):
        user = MemberUserFactory()
        serialized = MemberProfileSerializer(instance=user.profile).data

        self.assertGreaterEqual(serialized.items(), {
            "phone_number": user.profile.phone_number,
            "address": user.profile.address,
            "location": LocationSerializer(instance=user.profile.location).data,
        }.items())


class AuthSerializerTest(TestCase):
    maxDiff = None

    def test_authenticated_member_serializer(self):
        user = MemberUserFactory()
        serialized = AuthUserSerializer(instance=user).data

        self.assertGreaterEqual(serialized.items(), {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "is_member": user.is_member,
            "is_active": user.is_active,
            "profile": MemberProfileSerializer(instance=user.profile).data,
        }.items())

    def test_authenticated_non_member_serializer(self):
        user = UserFactory()
        serialized = AuthUserSerializer(instance=user).data

        self.assertGreaterEqual(serialized.items(), {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "is_member": user.is_member,
            "is_active": user.is_active,
            "created_at": user.created_at.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "profile": None,
        }.items())
