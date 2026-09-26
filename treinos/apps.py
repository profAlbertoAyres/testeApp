from django.apps import AppConfig


class TreinosConfig(AppConfig):
    name = 'treinos'

    def ready(self):
        import treinos.signals
