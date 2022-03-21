import os
import datetime

from core.settings.base import REST_FRAMEWORK


DEBUG = os.getenv("APP_DEBUG", "False").upper() == "TRUE"
SECRET_KEY = os.getenv("APP_SECRET")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

CORS_ALLOWED_ORIGINS = []

REST_FRAMEWORK.update({
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
})

# Simple JWT Auth
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=int(os.getenv("ACCESS_TOKEN_LIFETIME", "7"))),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=int(os.getenv("REFRESH_TOKEN_LIFETIME", "9"))),
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "TIME_ZONE": os.getenv("DB_TZ")
    }
}
