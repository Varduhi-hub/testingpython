import unittest
from selenium import webdriver
driver = webdriver.Chrome()

class Searchfield(unittest.TestCase):
    base_url="https://www.apple.com/"
    search_term="iphone xr"

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitily_wait(10)

    def test_load_home_page(self):
        driver=self.driver
        driver.get(self.base_url)
        self.assertIn("apple",driver.title)

    def test_search_for_a_term(self):
        self.driver.get(self.base_url)

        searchfield=self.driver.find_element_by_id("ac-gn-searchform-wrapper")
        searchfield.clear()
        searchfield.send_keys(self.search_term)
        searchfield.send_keys(Keys.RETURN)
        self.assertIn(self.search_term,self.driver.title)

    def tearDown(self):
        self.driver.close()