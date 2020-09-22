from django.apps import AppConfig


class EquitycoreConfig(AppConfig):
    name = 'equitycore'

    def ready(self):
        from equitycore import signals

        pass
