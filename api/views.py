from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import RequestCodeSerializer
from utils.imei_checker import IMEI
from asgiref.sync import async_to_sync

from backend.config import PROJECT_CONFIG


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def check_code(request):
    serializer = RequestCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.data.get('code')
    imei = IMEI(code=str(code), service_id=PROJECT_CONFIG.CHECKER_SERVICE_ID)
    is_valid, text = imei.validate()
    if not is_valid:
        return Response(
            data={'errors': text}, status=status.HTTP_400_BAD_REQUEST
        )
    async_to_sync(imei.acheck)()
    if imei.result:
        return Response(data=imei.result, status=imei.status)
    return Response(
        data={'error': 'Server error'},
        status=status.HTTP_503_SERVICE_UNAVAILABLE
    )
