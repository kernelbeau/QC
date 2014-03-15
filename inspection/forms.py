from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from inspection.models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product


class FeatureForm(ModelForm):
    class Meta:
        model = Feature


class BatchForm(ModelForm):
    class Meta:
        model = Batch


class ReportForm(ModelForm):
    class Meta:
        model = Report
        #exclude = ['batch', 'slug']


class ResultForm(ModelForm):
    class Meta:
        model = Result


#class FeatureForm(ModelForm):
    #""" """
    #READONLY_FIELDS = (
        #'description',
        #'limit_high',
        #'limit_low',
        #)

    #class Meta:
        #model = Feature
        #exclude = ('report',)

    #def __init__(self, readonly=False, *args, **kwargs):
        #super(FeatureForm, self).__init__(*args, **kwargs)
        #instance = getattr(self, 'instance', None)
        #if readonly:
            #for field in READONLY_FIELDS:
                #self.fields[field].widget.attrs['readonly'] = True

    #def clean_actual_size(self):
        #return self.instance.actual_size

    #def clean_description(self):
        #return self.instance.description

    #def clean_limit_high(self):
        #return self.instance.limit_high

    #def clean_limit_low(self):
        #return self.instance.limit_low

#FeatureFormSet = inlineformset_factory(Report, Feature, form=FeatureForm)


#class ReportForm(ModelForm):
    #""" """
    #class Meta:
        #model = Report
        #exclude = ('slug',)

    #def __init__(self, readonly=False, *args, **kwargs):
        #super(ReportForm, self).__init__(*args, **kwargs)

    #def clean_job_number(self):
        #return self.instance.job-number
