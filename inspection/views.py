from django.shortcuts import render

# Create your views here.

from django.core.urlresolvers import reverse, reverse_lazy
#from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

#from human_res.forms import EmployeeAddressFormSet
from inspection.models import Feature, Result


class FeatureList(ListView):
    """list all of the inspection features"""
    model = Feature


class InspectionIndex(TemplateView):
    """display the inspection homepage"""
    template_name = 'inspection/index.html'
