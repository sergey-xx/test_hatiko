from django.apps import AppConfig


class AdminPanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_panel'
    verbose_name = 'Административная панель'

    def ready(self) -> None:
        from backend import config
        return super().ready()
