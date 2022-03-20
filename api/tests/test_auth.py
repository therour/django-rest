from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

# from geo_id.models import GeoLocation, GeoType
# from accounts.models import MemberProfile
from model_factory.factories import MemberUserFactory, UserFactory


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

    def _assert_user_response(self, user_data, expected, is_member=None):
        is_member = expected.is_member if is_member is None else is_member
        self.assertGreaterEqual(user_data.items(), {
            "id": expected.id,
            "name": expected.name,
            "email": expected.email,
            "is_member": is_member,
            "is_active": True,
            "created_at": expected.created_at.strftime("%Y-%m-%dT%H:%M:%S%z"),
        }.items())
        if is_member:
            self.assertGreaterEqual(user_data.get("profile").items(), {
                "phone_number": expected.profile.phone_number,
                "address": expected.profile.address,
            }.items())
            self.assertTrue(user_data.get("profile").get("location"))
