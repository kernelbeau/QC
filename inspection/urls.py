from django.conf.urls import patterns, url

from inspection.views import *


urlpatterns = patterns('inspection.views',

    url(r'^$', InspectionIndex.as_view(), name='index'),
    url(r'product/$', ProductList.as_view(), name='product-list'),
    url(r'product/(?P<product>.+)/$', ProductBatchList.as_view(), name='product-batch'),
    url(r'batch/$', BatchList.as_view(), name='batch-list'),
    url(r'report/(?P<batch>.+)/$', ReportList.as_view(), name='report-list'),
    url(r'(?P<batch>.+)/(?P<report>.+)$', ReportDetail.as_view(), name='report-detail'),

)
