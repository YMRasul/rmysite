from django.apps import AppConfig


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'   # TODO начиная с версии 4.0
    name = 'app1'

    # Если  в mywork.settings.py
    # INSTALLED_APPS = [
    #                   'app1.apps.App1Config',
    # то 'verbose_name' работает, если просто
    # INSTALLED_APPS = [
    #                   'app1,
    # в админ панеле 'verbose_name' не действует
    verbose_name='Фотографии однакурсников'
