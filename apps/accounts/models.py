from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.geolocation.models import GeoLocation


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, name, email, password, **extra_fields):
        if not name:
            raise ValueError(_("name must bet set"))
        if not email:
            raise ValueError(_("email must bet set"))
        if not password:
            raise ValueError(_("email must bet set"))

        email = self.normalize_email(email)
        user = self.model(name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        return self._create_user(name, email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("name"), max_length=255)
    email = models.EmailField(_("email"), unique=True)
    is_member = models.BooleanField(_("member status"), default=False)
    is_active = models.BooleanField(_("active"), default=False)
    is_staff = models.BooleanField(_("staff status"), default=False)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    objects = AccountManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return f"{self.name} ({self.email})"


class MemberProfile(models.Model):
    account = models.OneToOneField(Account, related_name="profile", on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(_("phone number"), max_length=20)
    address = models.CharField(_("address"), max_length=255)
    location = models.ForeignKey(GeoLocation, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f"{self.account} - Profile"
