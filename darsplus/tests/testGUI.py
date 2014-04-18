import unittest
from selenium import webdriver

class testGUI(unittest.TestCase):
    #Must manually from django admin panel delete created selenium user after every run

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
        self.assertIn("home",self.driver.current_url)

    def testCreateUserNoPasswordError(self):
        print "HI"
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("selenium")
        elem = self.driver.find_element_by_name("add")
        elem.click()
        self.assertTrue(self.driver.find_element_by_class_name("errorlist"))

    def testCreateUserNoUsernameError(self):

        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("pass")
        elem = self.driver.find_element_by_name("add")
        elem.click()
        self.assertTrue(self.driver.find_element_by_class_name("errorlist"))

    def testUserLogin(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("selenium2")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("pass")
        elem = self.driver.find_element_by_name("add")
        elem.click()
        elem = self.driver.find_element_by_name("logout")
        elem.click()

        elem = self.driver.find_element_by_name("username")
        elem.send_keys("selenium2")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("pass")
        elem = self.driver.find_element_by_name("login")
        elem.click()
        self.assertTrue(self.driver.find_element_by_id("createUser"))
        self.assertIn("registration",self.driver.current_url)
    
    def testLoginNoPasswordError(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("userFail1")
        elem = self.driver.find_element_by_name("login")
        elem.click()
        self.assertTrue(self.driver.find_element_by_class_name("errorlist"))

    def testLoginNoUsernameError(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("pass")
        elem = self.driver.find_element_by_name("login")
        elem.click()
        self.assertTrue(self.driver.find_element_by_class_name("errorlist"))

    """
    What is the correct url? o_0
    def testForgotPassword(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        forgot_link = self.driver.find_element_by_link_text('Forgot password?')
        self.assertIn("password/reset",self.driver.current_url)
    """ 
  
    
    def tearDown(self):
        self.driver.close()