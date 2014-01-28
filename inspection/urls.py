from django.conf.urls import patterns, url

from inspection.views import *


urlpatterns = patterns('inspection.views',

    url(r'^$', InspectionIndex.as_view(), name='index'),
    url(r'features/$', FeatureList.as_view(), name='feature-list'),
    #url(r'employee/new/$', EmployeeCreate.as_view(), name='employee-create'),
    #url(r'employee/(?P<pk>\d+)/$', EmployeeDetail.as_view(), name='employee-detail'),
    #url(r'employee/(?P<pk>\d+)/edit/$', EmployeeUpdate.as_view(), name='employee-update'),
    #url(r'employee/(?P<pk>\d+)/remove/$', EmployeeDelete.as_view(), name='employee-delete'),
    #url(r'edit/(?P<pk>\d+)/address/$', EditEmployeeAddress.as_view(), name='employee-address-edit'),

)
