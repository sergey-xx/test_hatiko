from django.contrib import admin

from .models import TgUser


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = (
        'telegram_id',
        'username',
        'first_name',
        'last_name',
        'is_active',
        'created_at',
    )
