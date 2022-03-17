from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class JWTAuthTest(APITestCase):
    model = get_user_model()

    def test_login(self):
        self.model.objects.create_user(
            name="John Doe",
            email="johndoe@example.com",
            password="password")

        res = self.client.post(
            "/api/auth/login/",
            data={"email": "johndoe@example.com", "password": "password"},
            format="json")
        self.assertEqual(res.status_code, 200)

        res_data = res.json()
        self.assertTrue(res_data.get("access"))
        self.assertTrue(res_data.get("refresh"))

        user_data = res_data.get("data")
        self.assertIsInstance(user_data.get("id"), int)
        self.assertEqual(user_data.get("name"), "John Doe")
        self.assertEqual(user_data.get("email"), "johndoe@example.com")

    def test_get_authenticated_user_data(self):
        user = self.model.objects.create_user(
            name="John Doe",
            email="johndoe@example.com",
            password="password")

        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)

        res = self.client.get(
            "/api/auth/me/", format="json", HTTP_AUTHORIZATION="Bearer " + token)

        self.assertEqual(res.status_code, 200)

        user_data = res.json().get("data")
        self.assertIsInstance(user_data.get("id"), int)
        self.assertEqual(user_data.get("name"), "John Doe")
        self.assertEqual(user_data.get("email"), "johndoe@example.com")
