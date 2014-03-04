from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from inspection.models import *


class InspectionIndex(TemplateView):
    """display the inspection homepage"""
    template_name = 'inspection/index.html'


class ProductList(ListView):
    """list of all products"""
    model = Product


class ProductBatchList(ListView):
    """display batch orders by product"""
    template_name = 'inspection/product_batch.html'

    def get_queryset(self):
        self.product = get_object_or_404(Product, slug=self.kwargs['product'])
        return Batch.objects.filter(product=self.product)

    def get_context_data(self, **kwargs):
        context = super(ProductBatchList, self).get_context_data(**kwargs)
        context['product'] = self.product
        return context


class BatchList(ListView):
    """list of all batch orders released"""
    model = Batch


class ReportList(ListView):
    """display reports associated with batch"""
    def get_queryset(self):
        self.batch = get_object_or_404(Batch, slug=self.kwargs['batch'])
        return Report.objects.filter(batch=self.batch)


class ReportDetail(ListView):
    """display inspection report"""
    template_name = 'inspection/report_detail.html'

    def get_queryset(self):
        self.report = get_object_or_404(Report, slug=self.kwargs['report'])
        return Result.objects.filter(report=self.report)

    def get_context_data(self, **kwargs):
        context = super(ReportDetail, self).get_context_data(**kwargs)
        context['batch'] = Batch.objects.get(slug=self.report.batch.slug)
        context['product'] = Product.objects.get(slug=self.report.batch.product.slug)
        context['report'] = self.report
        return context
