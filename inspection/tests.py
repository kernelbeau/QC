from django.core.urlresolvers import reverse
#from django.http import HttpRequest
from django.test import TestCase
from django.test.client import Client

from inspection.models import *


class ProductList(TestCase):
    """" """
    def test_display_inspection_product_page(self):
        product_list = self.client.get(reverse('inspection:product-list'))
        self.assertEqual(product_list.status_code, 200)

    def test_empty_product_list_displays_message(self):
        product_list = self.client.get(reverse('inspection:product-list'))
        self.assertContains(product_list, 'No product currently available')

    def test_product_list_displays_part_names(self):
        Product.objects.create(number='101', product='Part', revision='A', slug='part')
        product_list = self.client.get(reverse('inspection:product-list'))
        self.assertContains(product_list, 'Part')


class BatchList(TestCase):
    """" """
    def setUp(self):
        Product.objects.create(number='101', product='Part_name', revision='A', slug='part')

    def test_display_inspection_batch_page(self):
        batch_list = self.client.get(reverse('inspection:batch-list'))
        self.assertEqual(batch_list.status_code, 200)

    def test_empty_batch_list_displays_message(self):
        batch_list = self.client.get(reverse('inspection:batch-list'))
        self.assertContains(batch_list, 'Nothing currently released')

    def test_batch_list_displays_part_names(self):
        product = Product.objects.get(product='Part_name')
        Batch.objects.create(batch='1001', product=product, quantity=100, slug='1001')
        batch_list = self.client.get(reverse('inspection:batch-list'))
        self.assertContains(batch_list, 'Part_name')

    def test_display_batch_detail(self):
        product = Product.objects.get(product='Part_name')
        Batch.objects.create(batch='1001', product=product, quantity=100, slug='1001')


        #employee = Employee.objects.get(name_last='Last_one')
        #edit_employee = self.client.get(reverse('human_res:employee-update',
            #kwargs={'pk': employee.id}))


#class EmployeeDetailTest(TestCase):
    #""" """
    #def setUp(self):
        #Employee.objects.create(name_first='First_one', name_last='Last_one')
        #Address.objects.create(address='111 One_address', city='One_city', state='TN', zip_code='12345', employee=Employee.objects.get(pk=1))
        #Email.objects.create(email='one@example.com', employee=Employee.objects.get(pk=1))

    #def test_display_employee_detail_page(self):
        #employee = Employee.objects.get(name_last='Last_one')
        #employee_detail = self.client.get(reverse('human_res:employee-detail',
            #kwargs={'pk': employee.id}))
        #self.assertEqual(employee_detail.status_code, 200)

    #def test_employee_detail_displays_data(self):
        #employee = Employee.objects.get(name_last='Last_one')
        #employee_detail = self.client.get(reverse('human_res:employee-detail',
            #kwargs={'pk': employee.id}))
        #self.assertContains(employee_detail, 'Last_one')
        #self.assertContains(employee_detail, '111 One_address')
        #self.assertContains(employee_detail, 'one@example.com')
