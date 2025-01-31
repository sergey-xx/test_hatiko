import logging

from adrf.decorators import api_view
from asgiref.sync import sync_to_async
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend.config import PROJECT_CONFIG
from utils.imei_checker import IMEI

from .serializers import RequestCodeSerializer

logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
async def check_code(request):
    serializer = RequestCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('code')
    service_id = await sync_to_async(lambda: PROJECT_CONFIG.CHECKER_SERVICE_ID)()
    imei = IMEI(code=str(code), service_id=service_id)
    imei.validate()
    await imei.acheck()
    if imei.result:
        return Response(data=imei.result, status=imei.status_code)
    logger.error(f"IMEI check failed for code {code}: No result from service")
    return Response(
        data={'error': 'Server error'},
        status=status.HTTP_503_SERVICE_UNAVAILABLE
    )
