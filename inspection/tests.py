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
        self.assertContains(product_list, 'No products currently available')

    def test_product_list_displays_part_names(self):
        Product.objects.create(product='Part', revision='A', slug='part')
        product_list = self.client.get(reverse('inspection:product-list'))
        self.assertContains(product_list, 'Part')


class BatchList(TestCase):
    """" """
    def setUp(self):
        Product.objects.create(product='Part_name', revision='A', slug='part')

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
