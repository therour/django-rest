from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import GeoLocation


class FilterByParent(admin.SimpleListFilter):  # pragma: no cover
    title = _("Parent")
    parameter_name = "parent"

    def lookups(self, request, model_admin):
        if not self.value() or (self.value().isnumeric() and len(self.value()) >= 4):
            return (
                ("province", _("Province")),
                ("city", _("City")),
                ("district", _("District")),
            )

        if self.value() in ("province", "city"):
            return model_admin.get_queryset(request).filter(type=self.value()).values_list("id", "name")

        return model_admin.get_queryset(request).filter(parent__id=self.value()).values_list("id", "name")

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        if self.value() == "province":
            return queryset.filter(type="province")
        if self.value() == "city":
            return queryset.filter(type="city")
        if self.value() == "district":
            return queryset.filter(type="district")
        if self.value() == "village":
            return queryset.filter(type="village")

        return queryset.filter(parent__id=self.value())


class GeoLocationAdminConfig(admin.ModelAdmin):  # pragma: no cover
    ordering = ("id",)
    list_display = ("id", "name", "type", "parent_name")
    search_fields = ("name",)
    list_filter = (FilterByParent,)
    list_select_related = ("parent",)

    @admin.display()
    def parent_name(self, obj):
        return f"{_(obj.parent.type).upper()} - {obj.parent.name}" if obj.parent else None


# Register your models here.
admin.site.register(GeoLocation, GeoLocationAdminConfig)
