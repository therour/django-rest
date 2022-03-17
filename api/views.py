from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .serializers import AuthUserSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_authenticated_user(request):
    serializer = AuthUserSerializer(instance=request.user)
    return Response({"data": serializer.data})
