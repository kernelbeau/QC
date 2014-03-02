from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from inspection.models import *


class InspectionIndex(TemplateView):
    """display the inspection homepage"""
    template_name = 'inspection/index.html'


class ProductList(ListView):
    """list of products"""
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['batch'] = Batch.objects.all()
        return context


class ProductDetail(ListView):
    """ """
    template_name = 'inspection/product_detail.html'

    def get_queryset(self):
        self.product = get_object_or_404(Product, slug=self.kwargs['slug'])
        return Batch.objects.filter(product=self.product)

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['product'] = self.product
        return context


class BatchList(ListView):
    """list of batch orders"""
    model = Batch

    def get_context_data(self, **kwargs):
        context = super(BatchList, self).get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        return context


class BatchDetail(ListView):
    """ """
    model = Batch
    template_name = 'inspection/batch_detail.html'


class ReportList(ListView):
    """ """
    def get_queryset(self):
        self.batch = get_object_or_404(Batch, slug=self.kwargs['slug'])
        return Report.objects.filter(batch=self.batch)


#class ReportCreate(CreateView):
    #"""add inspection results then redirect to the list page"""
    #model = Result
    #success_url = reverse_lazy('inspection:feature-list')

    #def get_context_data(self, **kwargs):
        #context = super(ReportCreate, self).get_context_data(**kwargs)
        #context['action'] = reverse('inspection:report-create')
        #return context


#class ReportUpdate(UpdateView):
    #"""edit a result object then redirect to the list page"""
    #model = Result
    #success_url = reverse_lazy('inspection:feature-list')

    #def get_context_data(self, **kwargs):
        #context = super(ReportUpdate, self).get_context_data(**kwargs)
        #context['action'] = reverse('inspection:report-update', kwargs={'pk': self.get_object().id})
        #return context


#class FeatureList(ListView):
    #"""list all of the inspection features"""
    #model = Feature
