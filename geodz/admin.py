from django.contrib import admin
from models import Municipality, Province


class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)

admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Province, ProvinceAdmin)