from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView  # , TokenObtainPairView
from .views import JWTLoginApi, MemberRegistrationApi, GetAuthenticatedUserApi


urlpatterns = [
    path("auth/register/", MemberRegistrationApi.as_view(), name="api_register"),
    path("auth/login/", JWTLoginApi.as_view(), name="api_login"),
    path("auth/me/", GetAuthenticatedUserApi.as_view(), name="api_me"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="api_token_refresh"),
]
