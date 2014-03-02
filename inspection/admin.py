from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from inspection.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product',)
    prepopulated_fields = {'slug': ('product',)}

admin.site.register(Product, ProductAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature',)

admin.site.register(Feature, FeatureAdmin)


class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch',)
    prepopulated_fields = {'slug': ('batch',)}

admin.site.register(Batch, BatchAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('report',)

admin.site.register(Report, ReportAdmin)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('result',)

admin.site.register(Result, ResultAdmin)
