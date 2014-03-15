from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from inspection.forms import *
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


class ReportCreate(CreateView):
    """add a new employee object then redirect to the list page"""
    form_class = ReportForm
    model = Report
    success_url = reverse_lazy('inspection:report-list')

    def get_context_data(self, **kwargs):
        context = super(ReportCreate, self).get_context_data(**kwargs)
        context['action'] = reverse('inspection:report-create')
        print "context:", context
        print "kwargs:", kwargs
        return context


#class InspectionViewForm(FormView):
    #""" """
    #form_class = FeatureFormSet
    #get_success_url = "/"
    #template_name = "inspection/form.html"

    #def get_initial(self):
        #queryset = self.get_queryset()
        #initial_data = []
        #for item in queryset:
            #initial_data.append({
                #'description': item.description,
                #'limit_high': item.limit_high,
                #'limit_low': item.limit_low,
                #'actual_size': item.actual_size,
            #})
        #return initial_data

    #def get_queryset(self):
        #self.report = get_object_or_404(Report, slug=self.kwargs['slug'])
        #return Feature.objects.filter(report=self.report)

    #def get_context_data(self, **kwargs):
        #context = super(InspectionViewForm, self).get_context_data(**kwargs)
        #context['report'] = self.kwargs['slug']
        #return context

    #def get(self, request, *args, **kwargs):
        #form_class = self.get_form_class()
        #form = self.get_form(form_class)
        #formset = FeatureFormSet(initial=self.get_initial())
        #return self.render_to_response(self.get_context_data(form=form, formset=formset))

    #def post(self, request, *args, **kwargs):
        #self.object = None
        #form_class = self.get_form_class()
        #form = self.get_form(form_class)
        #formset = FeatureFormSet(request.POST)
        #form_valid = formset.is_valid()
        #if form_valid and formset_valid:
            #pass
        #else:
            #return self.form_invalid(form, formset)
