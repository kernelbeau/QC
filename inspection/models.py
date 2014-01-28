from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
import datetime


class Feature(models.Model):
    ATTRIBUTE = 'A'; DIMENSION = 'D'
    TYPE = ((ATTRIBUTE, 'Atribute'), (DIMENSION, 'Dimension'),)
    description = models.CharField(_('description'), max_length=128, null=True, blank=True)
    feature_type = models.CharField(max_length=2, choices=TYPE, default=DIMENSION)
    limit_high = models.FloatField(_('limit high'),max_length=8, null=True, blank=True)
    limit_low = models.FloatField(_('limit low'),max_length=8, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.description)

    class Meta:
        db_table = 'inspection_features'
        verbose_name = _('feature')
        verbose_name_plural = _('features')

    @permalink
    def get_absolute_url(self):
        return reverse('feature-detail', kwargs={
            'description': self.description,
            'pk': self.pk,})


class Result(models.Model):
    feature = models.ForeignKey('Feature')
    result = models.CharField(_('result'), max_length=8)

    def __unicode__(self):
        return u'%s' % (self.result)

    class Meta:
        db_table = 'inspection_results'
        verbose_name = _('result')
        verbose_name_plural = _('results')

    @permalink
    def get_absolute_url(self):
        return reverse('feature-result', kwargs={
            'result': self.result,
            'pk': self.pk,})
