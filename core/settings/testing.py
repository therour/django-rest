from datetime import timedelta


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
