from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Account


class UserAdminConfig(UserAdmin):
    ordering = ("-created_at",)
    search_fields = ("name", "email")
    list_filter = ("name", "email", "is_active", "is_member", "is_staff")
    list_display = ("name", "email", "is_active", "is_member", "is_staff")

    fieldsets = (
        (None, {"fields": ("name", "email")}),
        (_("Membership"), {"fields": ("is_active", "is_member")}),
        (_("Permissions"), {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "email", "password1", "password2"),
            },
        ),
    )


# Register your models here.
admin.site.register(Account, UserAdminConfig)
