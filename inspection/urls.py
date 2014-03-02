from django.conf.urls import patterns, url

from inspection.views import *


urlpatterns = patterns('inspection.views',

    url(r'^$', InspectionIndex.as_view(), name='index'),
    url(r'product/$', ProductList.as_view(), name='product-list'),
    url(r'product/(?P<slug>\w+)/$', ProductDetail.as_view(), name='product-detail'),
    url(r'batch/$', BatchList.as_view(), name='batch-list'),
    url(r'batch/(?P<slug>\d+)/$', BatchDetail.as_view(), name='batch-detail'),
    url(r'report/(?P<slug>\d+)/$', ReportList.as_view(), name='report-list'),

)
