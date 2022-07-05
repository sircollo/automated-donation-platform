from django.apps import AppConfig


class AdpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adp'

    def ready(self):
        import adp.signals