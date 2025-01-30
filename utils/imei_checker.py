import logging
from typing import Self
import aiohttp

from django.conf import settings
from backend.config import PROJECT_CONFIG

API_KEY = settings.ENV.str('IMEICHECK_API_KEY')

logger = logging.getLogger(__name__)


class IMEI:

    BASE_URL = 'https://api.imeicheck.net'

    def __init__(self, code: str, service_id: int = 13) -> None:
        self.code = code
        self.service_id = service_id
        self.validated_code = None
        self.result = None

    def validate(self):
        if not self.code.isdigit():
            return False, 'IMEI must contain only digits'
        if len(self.code) != 15:
            return False, 'IMEI must be 15 digits length'
        self.validated_code = self.code
        return True, 'OK'

    async def acheck(self):
        url = f'{self.BASE_URL}/v1/checks'
        if not self.validated_code:
            raise ValueError('You need to validate code first')
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Accept-Language': 'en'
        }
        payload = {
            'deviceId': self.validated_code,
            'serviceId': self.service_id
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url,
                                    headers=headers,
                                    json=payload) as resp:
                self.status = resp.status
                if resp.status in (201, 422):
                    data = await resp.json()
                    self.result = data
                else:
                    text = await resp.text()
                    logger.error('Request to server imeicheck.net not '
                                 f'successful. Response: {resp.status} {text}')
