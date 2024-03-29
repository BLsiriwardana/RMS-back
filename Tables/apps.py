from django.apps import AppConfig


class TablesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Tables'

class IPConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'IPaddress'

