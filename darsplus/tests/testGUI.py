import unittest
from selenium import webdriver

class testGUI(unittest.TestCase):
    #Must manually form django admin panel delete created selenium user after every run

    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def testCreateUserLogout(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("selenium")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("pass")
        elem = self.driver.find_element_by_name("add")
        elem.click()
        self.assertTrue(self.driver.find_element_by_id("createUser"))
        elem = self.driver.find_element_by_name("logout")
        elem.click()
        self.assertIn("home",self.driver.getCurrentURL())
    
    def tearDown(self):
        self.driver.close()