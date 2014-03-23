from django.db import models
from django.conf import settings

class Province(models.Model):
    ### wilaya ###

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'
        ordering = ['id']

    name = models.CharField('Name', max_length=255)
    code = models.CharField('Code', max_length=2)

    #geo coords
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)


    def get_gmaps_query_url(self):
        url = getattr(settings, 'GEODZ_GMAPS_QUERY_URL', 'http://maps.google.com/?q=')
        return '%s%s' % (url, self.name)

    def __unicode__(self):
        return self.name

class Municipality(models.Model):
    ### commune ###

    class Meta:
        verbose_name = 'Municipality'
        verbose_name_plural = 'Municipalities'
        ordering = ['province']

    name = models.CharField('Name', max_length=255)

    #geo coords
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    #fk
    province = models.ForeignKey(Province, related_name='municipalities')

    def get_gmaps_query_url(self):
        url = getattr(settings, 'GEODZ_GMAPS_QUERY_URL', 'http://maps.google.com/?q=')
        return '%s%s, %s' % (url, self.name, self.province)

    def __unicode__(self):
        return self.name