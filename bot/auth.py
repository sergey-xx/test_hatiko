import logging
from users.models import TgUser

logger = logging.getLogger(__name__)


def permission(coro):
    async def wrap(message, state, **kwargs):
        telegram_id = kwargs['event_from_user'].id
        if await TgUser.objects.filter(telegram_id=telegram_id, is_active=True).aexists():
            return await coro(message, state)
        logging.info(f'Пользователь с {telegram_id} пытает воспользоваться ботом')
        return
    return wrap
