from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView


from apps.accounts.models import Account
from .serializers.accounts import AuthUserSerializer
from .serializers.auth import ApiLoginResponseSerializer, ApiRegisterSerializer, JWTAuthSerializer


class GetAuthenticatedUserApi(generics.RetrieveAPIView):
    serializer_class = AuthUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class MemberRegistrationApi(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = ApiRegisterSerializer
    permission_classes = (AllowAny,)


class JWTLoginApi(TokenObtainPairView):
    serializer_class = JWTAuthSerializer

    @extend_schema(responses={200: ApiLoginResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
