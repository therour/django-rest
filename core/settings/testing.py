from datetime import timedelta
from .base import BASE_DIR, INSTALLED_APPS


INSTALLED_APPS += (
    "django_nose",
)


SECRET_KEY = "easypeasy"

# Simple JWT Auth
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=90),
}

PASSWORD_HASHERS = (
    "django.contrib.auth.hashers.MD5PasswordHasher",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = str(BASE_DIR / "reports" / "junit")
NOSE_ARGS = [
    "--verbosity=2",
    "--with-xunit",
    "--xunit-file=" + str(TEST_OUTPUT_DIR + "/xunittest.xml"),
]
