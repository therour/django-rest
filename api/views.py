from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from drf_spectacular.utils import extend_schema

from .serializers.accounts import AuthUserSerializer


@extend_schema(
    responses={200: AuthUserSerializer}
)
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_authenticated_user(request):
    serializer = AuthUserSerializer(instance=request.user)
    return Response(serializer.data)
