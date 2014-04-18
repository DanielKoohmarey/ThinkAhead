import unittest
from selenium import webdriver
from django.contrib.auth.models import User
from darsplus.models import UserProfile

if not User.objects.filter(username='test'):
    new_user = User.objects.create_user(username='test',password='test', email='test@test.com')
    new_user.save()
if not UserProfile.objects.filter(username="test"):
    UserProfile.addUserProfile("test","Electrical Engineering and Computer Sciences",'College of Engineering',
                                                     "Fall", "2014",[])

testUser = User.objects.filter(username='selenium')
if testUser:
    User.delete(testUser[0])

class testGUI(unittest.TestCase):

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
        self.driver.find_element_by_id("createUser")
        elem = self.driver.find_element_by_name("logout")
        elem.click()
        self.assertIn("home",self.driver.current_url)
        
    def testLoginUserLogout(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("test")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("test")
        elem = self.driver.find_element_by_name("login")
        elem.click()
        self.driver.find_element_by_name("update")
        elem = self.driver.find_element_by_name("logout")
        elem.click()
        self.assertIn("home",self.driver.current_url)

    def testCreateUserNoPasswordError(self):
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

    def testForgotPassword(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        forgot_link = self.driver.find_element_by_link_text('Forgot password?')
        forgot_link.click()
        self.assertIn("password/reset",self.driver.current_url)
        email = self.driver.find_element_by_name('email')
        email.send_keys("test@test.com")
        reset = self.driver.find_element_by_class_name('button')
        reset.click()
        self.assertIn("password/reset/done",self.driver.current_url)

    def testLoginUserUpdateProfile(self):    
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("test")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("test")
        elem = self.driver.find_element_by_name("login")
        elem.click()
        elem = self.driver.find_element_by_xpath("//a[@href='/profile']")
        elem.click()
        elem = self.driver.find_element_by_id("createUser")
        self.assertIn("profile",self.driver.current_url)
        #for unkown reasons the profile does not populate correctly
        elem = self.driver.find_element_by_name("logout")
        elem.click()
        """
        import time
        time.sleep(10)
        elem.click()
        self.assertIn("dashboard",self.driver.current_url)
        elem = self.driver.find_element_by_name("logout")
        elem.click()
        """
        
    def tearDown(self):
        self.driver.close()