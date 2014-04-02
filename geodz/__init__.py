from django.conf import settings

if 'geoposition' not in settings.INSTALLED_APPS:
    settings.INSTALLED_APPS += ('geoposition',)