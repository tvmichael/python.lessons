import selenium
print('64 - Selenium version: %s' % selenium.__version__)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Opera()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
