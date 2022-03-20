from django.test import TestCase

from .models import GeoLocation


class GeoLocationModelTest(TestCase):
    def test_geo_location_model_to_string(self):
        location = GeoLocation(name="Test Location")
        self.assertEqual(str(location), "Test Location")
