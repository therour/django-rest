from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .serializers import JWTAuthSerializer
from .views import get_authenticated_user


class JWTAuthView(TokenObtainPairView):
    serializer_class = JWTAuthSerializer


urlpatterns = [
    path("auth/login/", JWTAuthView.as_view(), name="api_login"),
    path("auth/me/", get_authenticated_user, name="api_me"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="api_token_refresh"),
]
