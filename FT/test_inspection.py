from unittest import skip

from selenium.webdriver.common.keys import Keys

from FT.helpers import MyTestCase

#@skip
class InspectionHomepage(MyTestCase):
    """ """
    def test_visit_inspection_home_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click links to inspection
        self.driver.find_element_by_link_text("Inspection").click()
        self.driver.find_element_by_link_text("What's New").click()
        # view inspection home page
        self.assertEqual(self.driver.current_url, self.live_server_url + '/qc/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Inspection news...', body.text)

#@skip
class InspectionProduct(MyTestCase):
    """ """
    def test_visit_inspection_product_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click links to inspection
        self.driver.find_element_by_link_text("Inspection").click()
        self.driver.find_element_by_link_text("Part #").click()
        # view inspection products page
        self.assertEqual(self.driver.current_url, self.live_server_url + '/qc/product/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Product...', body.text)

    def test_view_product_batch_list_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click links to product-batch
        self.driver.find_element_by_link_text("Inspection").click()
        self.driver.find_element_by_link_text("Part #").click()
        self.driver.find_element_by_link_text("3").click()
        # view product-batch page
        self.assertEqual(self.driver.current_url, self.live_server_url + '/qc/product/cover/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('3, Cover...', body.text)

    def test_view_product_batch_report_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click links to product-batch-report
        self.driver.find_element_by_link_text("Inspection").click()
        self.driver.find_element_by_link_text("Part #").click()
        self.driver.find_element_by_link_text("3").click()
        self.driver.find_element_by_link_text("1001").click()
        # view product-batch-report page
        self.assertEqual(self.driver.current_url, self.live_server_url + '/qc/report/1001/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Report...', body.text)

#@skip
class InspectionBatch(MyTestCase):
    """ """
    def test_visit_inspection_batch_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click links to batch #
        self.driver.find_element_by_link_text("Inspection").click()
        self.driver.find_element_by_link_text("Batch #").click()
        # view inspection batch list
        self.assertEqual(self.driver.current_url, self.live_server_url + '/qc/batch/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Batch...', body.text)

    def test_view_batch_detail_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click links to batch-report page
        self.driver.find_element_by_link_text("Inspection").click()
        self.driver.find_element_by_link_text("Batch #").click()
        self.driver.find_element_by_link_text("1001").click()
        # view batch-report page
        self.assertEqual(self.driver.current_url, self.live_server_url + '/qc/report/1001/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Report...', body.text)
