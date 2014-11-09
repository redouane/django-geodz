from django.conf import settings

# django 1.7 app conf
default_app_config = 'geodz.apps.GeodzConfig'

# only works pre 1.7
if 'geoposition' not in settings.INSTALLED_APPS:
    settings.INSTALLED_APPS += ('geoposition',)