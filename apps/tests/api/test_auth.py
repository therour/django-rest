from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.models import Account

from ..factories import LocationFactory, MemberProfileFactory, MemberUserFactory, UserFactory


class JWTAuthTest(APITestCase):
    def test_non_member_login(self):
        user = UserFactory()

        res = self.client.post(
            "/api/auth/login/",
            data={"email": user.email, "password": "password"},
            format="json")
        self.assertEqual(res.status_code, 200)

        res_data = res.json()
        self.assertTrue(res_data.get("access"))
        self.assertTrue(res_data.get("refresh"))
        self._assert_user_response(res_data.get("user"), user)

    def test_member_login(self):
        user = MemberUserFactory()

        res = self.client.post(
            "/api/auth/login/",
            data={"email": user.email, "password": "password"},
            format="json")
        self.assertEqual(res.status_code, 200)
        res_data = res.json()
        self.assertTrue(res_data.get("access"))
        self.assertTrue(res_data.get("refresh"))
        self._assert_user_response(res_data.get("user"), user)

    def test_get_authenticated_user_data(self):
        user = MemberUserFactory()
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)

        res = self.client.get(
            "/api/auth/me/", format="json", HTTP_AUTHORIZATION="Bearer " + token)

        self.assertEqual(res.status_code, 200)
        self._assert_user_response(res.json(), user)

    def test_register_user(self):
        location = LocationFactory()
        user_stub = MemberUserFactory.stub(profile=None)
        profile_stub = MemberProfileFactory.stub(location=None, account=None)

        data = {
            "name": user_stub.name,
            "email": user_stub.email,
            "password": user_stub.password,
            "address": profile_stub.address,
            "phone_number": profile_stub.phone_number,
            "location": location.id,
        }

        res = self.client.post("/api/auth/register/", data=data, format="json")
        self.assertEqual(res.status_code, 201)

        created_user = Account.objects.get(email=user_stub.email)
        self._assert_user_response(res.json(), created_user)

    def test_register_user_fail_on_invalid_location(self):
        user_stub = MemberUserFactory.stub(profile=None)
        profile_stub = MemberProfileFactory.stub(location=None, account=None)

        data = {
            "name": user_stub.name,
            "email": user_stub.email,
            "password": user_stub.password,
            "address": profile_stub.address,
            "phone_number": profile_stub.phone_number,
            "location": "shouldnotexists",
        }

        res = self.client.post("/api/auth/register/", data=data, format="json")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json().get("location"), ["Invalid location"])

        with self.assertRaises(Account.DoesNotExist):
            Account.objects.get(email=user_stub.email)

    def _assert_user_response(self, user_data, expected, is_member=None):
        is_member = expected.is_member if is_member is None else is_member
        self.assertGreaterEqual(user_data.items(), {
            "id": expected.id,
            "name": expected.name,
            "email": expected.email,
            "is_member": is_member,
            "is_active": expected.is_active,
            "created_at": expected.created_at.strftime("%Y-%m-%dT%H:%M:%S%z"),
        }.items())
        if is_member:
            self.assertGreaterEqual(user_data.get("profile").items(), {
                "phone_number": expected.profile.phone_number,
                "address": expected.profile.address,
            }.items())
            self.assertTrue(user_data.get("profile").get("location"))
