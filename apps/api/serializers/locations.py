from rest_framework import serializers

from apps.geolocation.models import GeoLocation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocation
        fields = ["id", "name", "parent"]

    def get_fields(self):
        fields = super().get_fields()
        fields["parent"] = LocationSerializer(read_only=True)
        return fields
