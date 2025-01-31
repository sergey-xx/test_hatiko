import logging
from typing import Optional
import aiohttp

from django.conf import settings

API_KEY = settings.ENV.str('IMEICHECK_API_KEY')

logger = logging.getLogger(__name__)


class IMEI:
    """
    IMEI validator and checker.

    Before using acheck(),
    Sould be validated by validate()
    """

    BASE_URL = 'https://api.imeicheck.net'

    def __init__(self, code: str, service_id: int = 13) -> None:
        self.code: str = code
        self.service_id: int = service_id
        self.validated_code: Optional[str] = None
        self.result: Optional[dict] = None
        self.status_code: Optional[int] = None
        self.status: Optional[str] = None
        self.image_url: Optional[str] = None

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
                self.status_code = resp.status
                if resp.status in (201,):
                    self.result = await resp.json()
                    self.status = self.result.get('status') if self.result else None
                    self.image_url = (
                        self.result.get('properties').pop('image', None)
                        if (self.result and self.result.get('properties'))
                        else None
                    )
                else:
                    logger.error('Request to server imeicheck.net not '
                                 f'successful. Response: {resp.status} {await resp.text()}')

    @property
    def text(self):
        if self.status_code == 429:
            return 'Слишком много запросов. Попробуйте повторить запрос позже.'
        elif self.status in ('unsuccessful',):
            return 'Система не нашла информацию для идентификации устройства.'
        elif self.status in ('failed',):
            return 'Ошибка сервера. Попробуйте повторить запрос позже.'
        if not self.result:
            return 'Ошибка. Попробуйте позже или обратитесь к Администратору.'
        elif self.status_code == 201 and self.result['properties']:
            return '\n'.join([f'<b>{key}</b>: {value}' for key, value in self.result['properties'].items()])
        return 'Ошибка. Попробуйте позже или обратитесь к Администратору.'
