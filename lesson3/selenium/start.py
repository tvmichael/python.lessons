import selenium
from selenium.webdriver.common.by import By
print('64 - Selenium version: %s' % selenium.__version__)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Opera()
        self.browser.get('http://meduch.esy.es/')
        self.addCleanup(self.browser.quit)

    #def testPageTitle(self):
        #self.browser.get('http://www.google.com')
        #self.assertIn('Google', self.browser.title)

    #def test_PythonPage(self):
        #self.browser.get("http://www.python.org")
        #assert "Welcome to Python.org" in self.browser.title
        #elem = self.browser.find_element_by_name("q")
        #elem.clear()
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        #assert "No results found." not in self.page_source

    def test_M_title(self):
        #self.browser.get('http://meduch.esy.es/')
        assert "TAV Example" in self.browser.title

    def test_M_jumbotron(self):
        element = self.browser.find_element_by_class_name("jumbotron")
        #continue_link = self.browser.find_element_by_link_text('Open HTML examples ...')
        assert element, "jumbotron"

    def test_M_openB(self):
        continue_link = self.browser.find_element_by_link_text('Open HTML examples ...')
        assert continue_link, "jumbotron"


if __name__ == '__main__':
    unittest.main(verbosity=2)
