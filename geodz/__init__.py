from django.conf import settings

# django 1.7 app conf
default_app_config = 'geodz.apps.GeodzConfig'

if 'geoposition' not in settings.INSTALLED_APPS:
    settings.INSTALLED_APPS += ('geoposition',)