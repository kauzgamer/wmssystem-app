from django.apps import AppConfig


class DesktopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'desktop'
    
    def ready(self):
        import desktop.signals  # noqa