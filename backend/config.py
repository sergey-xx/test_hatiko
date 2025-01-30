import logging
from enum import Enum

from django.conf import settings
from liveconfigs.models import BaseConfig

logger = logging.getLogger()

DESCRIPTION_SUFFIX = "_DESCRIPTION"
TAGS_SUFFIX = "_TAGS"
VALIDATORS_SUFFIX = "_VALIDATORS"


class ConfigTags(str, Enum):
    urls = "Ссылки"
    payment = "Платежи"
    basic = "Основные"
    other = "Прочее"
    text = "Тексты"


class URL_CONFIG(BaseConfig):
    __topic__ = 'Настройки ссылок'

    __exported__ = [
        'DAYS',
        'FIRST_DAY_OF_WEEK',
        'TYPES_OF_LOADING',
        'USE_CALENDAR',
        'CONSOLIDATION_GROUPS',
    ]

    SITE_LINK: str = 'https://www.python.org/'
    SITE_LINK_DESCRIPTION = "Настройка ссылки на сайт"
    SITE_LINK_TAGS = [ConfigTags.urls]


class TEXT_CONFIG(BaseConfig):
    __topic__ = 'Настройки текстов'

    HI_MSG: str = 'Рады приветствовать вас! Для доступа к боту обратитесь к администратору.'
    HI_MSG_DESCRIPTION = "Приветственное сообщение"
    HI_MSG_TAGS = [ConfigTags.text]

    MENU_MSG: str = 'Отправьте IMEI, который хотите проверить.'
    MENU_MSG_DESCRIPTION = "Приветственное сообщение"
    MENU_MSG_TAGS = [ConfigTags.text]

    ERROR_MSG: str = 'Произошла ошибка. Обратитесь к администратору.'
    ERROR_MSG_DESCRIPTION = "Сообщение об ошибке сообщение"
    ERROR_MSG_TAGS = [ConfigTags.text]


class BUTT_CONFIG(BaseConfig):
    __topic__ = 'Настройки текстов кнопок'

    BACK: str = 'Назад'
    BACK_DESCRIPTION = "Текст кнопки Назад"
    BACK_TAGS = [ConfigTags.text]


class PROJECT_CONFIG(BaseConfig):
    __topic__ = 'Настройки текстов кнопок'

    CHECKER_SERVICE_ID: int = 13
    CHECKER_SERVICE_ID_DESCRIPTION = "ID сервиса по проверки IMAI"
    CHECKER_SERVICE_ID_TAGS = [ConfigTags.basic]

    WHITE_LIST_IDS: list[int] = [int(x) for x in settings.ENV.list('WHITE_LIST_IDS')]
    WHITE_LIST_IDS_DESCRIPTION = "Белый список ID Телеграм"
    WHITE_LIST_IDS_TAGS = [ConfigTags.basic]
