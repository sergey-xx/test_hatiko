import json

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from asgiref.sync import sync_to_async
from django.conf import settings

from backend.config import PROJECT_CONFIG, TEXT_CONFIG
from bot.auth import permission
from users.models import TgUser
from utils.imei_checker import IMEI
from utils.utils import prettify_text

ENV = settings.ENV
router = Router(name=__name__)


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.clear()
    white_list = await sync_to_async(lambda: PROJECT_CONFIG.WHITE_LIST_IDS)()
    is_active = message.from_user.id in white_list
    tg_user = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()
    if tg_user and tg_user.is_active:
        text = await sync_to_async(lambda: TEXT_CONFIG.MENU_MSG)()
        await message.answer(text)
        return
    elif not tg_user:
        await TgUser.objects.acreate(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            is_active=is_active,
        )
    if is_active:
        text = await sync_to_async(lambda: TEXT_CONFIG.MENU_MSG)()
    else:
        text = await sync_to_async(lambda: TEXT_CONFIG.HI_MSG)()
    await message.answer(text)


@router.message(F.text)
@permission
async def check(message: Message, state: FSMContext):
    service_id = await sync_to_async(lambda: PROJECT_CONFIG.CHECKER_SERVICE_ID)()
    imei = IMEI(message.text, service_id=service_id)
    is_valid, text = imei.validate()
    if not is_valid:
        await message.answer(text=text)
        return
    await imei.acheck()
    if imei.image_url:
        text = prettify_text(imei.text)
        await message.answer_photo(imei.image_url, text, parse_mode='HTML')
        return
    await message.answer(imei.text)
