from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField

class Region(models.Model):

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Province(models.Model):

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'
        ordering = ['id']

    name = models.CharField(_('Name'), max_length=255)
    code = models.CharField('Code', max_length=2)
    position = GeopositionField(blank=True, null=True)

    #fk
    region = models.ForeignKey(Region, related_name='provinces',
        verbose_name=_('Region'), null=True)

    def get_gmaps_query_url(self):
        url = getattr(settings, 'GEODZ_GMAPS_QUERY_URL', 'http://maps.google.com/?q=')
        return '%s%s' % (url, self.name)

    def __unicode__(self):
        return self.name

class Municipality(models.Model):

    class Meta:
        verbose_name = _('Municipality')
        verbose_name_plural = _('Municipalities')
        ordering = ['province']

    name = models.CharField(_('Name'), max_length=255)

    #geo coords
    position = GeopositionField(blank=True, null=True)

    #fk
    province = models.ForeignKey(Province, related_name='municipalities')

    def get_gmaps_query_url(self):
        url = getattr(settings, 'GEODZ_GMAPS_QUERY_URL', 'http://maps.google.com/?q=')
        return '%s%s, %s' % (url, self.name, self.province)

    def __unicode__(self):
        return self.name