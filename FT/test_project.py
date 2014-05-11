from unittest import skip

from selenium.webdriver.common.keys import Keys

from FT.helpers import MyTestCase

#@skip
class DjangoAdminTests(MyTestCase):
    """ """
    def test_admin_site_login_app_links_and_logout(self):
        # go to admin site
        self.driver.get('%s%s'% (self.live_server_url, '/admin/'))
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('My Project', body.text)
        # log in
        username_field = self.driver.find_element_by_name('username')
        username_field.send_keys("kb")
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys("kb")
        password_field.send_keys(Keys.RETURN)
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        # find admin links to current apps
        content = self.driver.find_element_by_id('content-main')
        self.assertIn('Features', content.text)
        # log out
        self.driver.find_element_by_link_text('Log out').click()
        self.assertEqual(self.driver.current_url, self.live_server_url + '/admin/logout/')

#@skip
class ProjectHomepage(MyTestCase):
    """ """
    def test_django_project_index_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('My Company', body.text)

    def test_visit_inspection_home_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click link to inspection
        self.driver.find_element_by_link_text('Inspection').click()
        self.driver.find_element_by_link_text("What's New").click()
        self.assertEqual(self.driver.current_url, self.live_server_url + '/qc/')
        # view inspection home page
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Inspection news...', body.text)

    def test_visit_inspection_product_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click link to inspection part #s
        self.driver.find_element_by_link_text('Inspection').click()
        self.driver.find_element_by_link_text('Part #').click()
        self.assertEqual(self.driver.current_url, self.live_server_url + '/qc/product/')
        # view inspection part #s page
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Product...', body.text)

    def test_visit_inspection_batch_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click link to inspection batch
        self.driver.find_element_by_link_text('Inspection').click()
        self.driver.find_element_by_link_text('Batch #').click()
        self.assertEqual(self.driver.current_url, self.live_server_url + '/qc/batch/')
        # view inspection batch page
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Batch...', body.text)
