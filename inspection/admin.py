from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from inspection.models import Feature, Result


class ResultAdmin(admin.ModelAdmin):
    list_display = ('result',)

admin.site.register(Result, ResultAdmin)


class FeatureAdmin(admin.ModelAdmin):
    fields = ('description', ('limit_high','limit_low'))
    list_display = ('description',)
    #list_filter = ('report',)
    #search_fields = ('report',)

admin.site.register(Feature, FeatureAdmin)
