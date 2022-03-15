from django.test import TestCase
from django.contrib.auth import get_user_model


class AccountTests(TestCase):
    model = get_user_model()

    def test_new_superuser(self):
        user = self.model.objects.create_superuser(
            name="John Doe",
            email="johndoe@example.com",
            password="password",
        )
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "johndoe@example.com")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertEqual(str(user), "John Doe (johndoe@example.com)")

    def test_failing_new_superuser(self):
        with self.assertRaises(ValueError):
            self.model.objects.create_superuser(
                name="John Doe",
                email="johndoe@example.com",
                password="password",
                is_superuser=False)

        with self.assertRaises(ValueError):
            self.model.objects.create_superuser(
                name="John Doe",
                email="johndoe@example.com",
                password="password",
                is_staff=False)

    def test_new_user(self):
        user = self.model.objects.create_user(
            name="John Doe",
            email="johndoe@example.com",
            password="password")

        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "johndoe@example.com")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertEqual(str(user), "John Doe (johndoe@example.com)")

    def test_failing_new_user(self):
        with self.assertRaises(ValueError):
            self.model.objects.create_user(
                name=None,
                email="johndoe@example.com",
                password="asdf1234")
        with self.assertRaises(ValueError):
            self.model.objects.create_user(
                name="John Doe",
                email=None,
                password="asdf1234")
        with self.assertRaises(ValueError):
            self.model.objects.create_user(
                name="John Doe",
                email="johndoe@example.com",
                password=None)
