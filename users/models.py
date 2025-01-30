from django.db import models


class TgUser(models.Model):
    """Класс Пользователей ТГ."""

    telegram_id = models.PositiveBigIntegerField(
        unique=True,
        verbose_name='Идентификатор Telegram',
    )
    username = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Юзернейм телеграм'
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='Имя',
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    is_active = models.BooleanField(default=False, verbose_name='Доступ разрешен')

    class Meta:
        verbose_name = 'Пользователь Telegram'
        verbose_name_plural = 'Пользователи Telegram'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}/{self.telegram_id}'
