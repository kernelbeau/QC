from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    """ """
    product = models.CharField(_('product'), max_length=16)
    revision = models.CharField(_('revision'), max_length=2, null=True, blank=True)
    slug = models.SlugField(_('slug'), unique=True,)

    def __unicode__(self):
        return u'%s' % (self.product)

    class Meta:
        db_table = 'qc_product'
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk, 'slug': self.slug})


class Feature(models.Model):
    """ """
    ATTRIBUTE = 'A'; DIMENSION = 'D'
    FEATURE_TYPE = ((ATTRIBUTE, 'Atribute'), (DIMENSION, 'Dimension'),)
    feature = models.CharField(_('feature'), max_length=128, null=True, blank=True)
    feature_type = models.CharField(max_length=2, choices=FEATURE_TYPE, default=DIMENSION)
    limit_high = models.FloatField(_('limit high'),max_length=8, null=True, blank=True)
    limit_low = models.FloatField(_('limit low'),max_length=8, null=True, blank=True)
    product = models.ForeignKey('Product')

    def __unicode__(self):
        return u'%s' % (self.feature)

    class Meta:
        db_table = 'qc_feature'
        verbose_name = _('feature')
        verbose_name_plural = _('features')

    def get_absolute_url(self):
        return reverse('feature-detail', kwargs={'pk': self.pk, 'slug': self.slug})


class Batch(models.Model):
    """ """
    batch = models.CharField(_('batch'), max_length=8)
    product = models.ForeignKey('Product')
    quantity = models.CharField(_('quantity'), max_length=4)
    slug = models.SlugField(_('slug'), unique=True,)

    def __unicode__(self):
        return u'%s' % (self.batch)

    class Meta:
        db_table = 'qc_batch'
        verbose_name = _('batches')
        verbose_name_plural = _('batch')


class Report(models.Model):
    """ """
    batch = models.ForeignKey('Batch')
    report = models.CharField(_('report'), max_length=8)
    slug = models.SlugField(_('slug'), unique=True,)

    def __unicode__(self):
        return u'%s' % (self.report)

    class Meta:
        db_table = 'qc_report'
        verbose_name = _('report')
        verbose_name_plural = _('reports')

    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'pk': self.pk, 'slug': self.slug})


class Result(models.Model):
    """ """
    feature = models.ForeignKey('Feature')
    inspector = models.CharField(_('inspector'), max_length=32)
    report = models.ForeignKey('Report')
    result = models.CharField(_('result'), max_length=8)

    def __unicode__(self):
        return u'%s' % (self.result)

    class Meta:
        db_table = 'qc_result'
        verbose_name = _('result')
        verbose_name_plural = _('results')
