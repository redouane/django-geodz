from django.db import models

class Province(models.Model):
    ### wilaya ###

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'

    name = models.CharField('Nom', max_length=255)
    code = models.CharField('Code', max_length=2)

    #geo coords
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Municipality(models.Model):
    ### commune ###

    class Meta:
        verbose_name = 'Commune'
        verbose_name_plural = 'Communes'

    name = models.CharField('Nom', max_length=255)

    #geo coords
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    #fk
    province = models.ForeignKey(Province, related_name='municipalities')

    def __unicode__(self):
        return self.name