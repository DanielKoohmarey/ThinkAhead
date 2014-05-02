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
        self.drivers = [webdriver.Firefox()]#, webdriver.Chrome(), webdriver.Ie(), webdriver.Safari()]
    
    def testCreateUserLogout(self):
        for driver in self.drivers:
            driver.get("http://127.0.0.1:8000/")
            self.assertIn("Think Ahead",driver.title)
            elem = driver.find_element_by_name("username")
            elem.send_keys("selenium")
            elem = driver.find_element_by_name("password")
            elem.send_keys("pass")
            elem = driver.find_element_by_name("add")
            elem.click()
            driver.find_element_by_id("createUser")
            elem = driver.find_element_by_name("logout")
            elem.click()
            self.assertIn("home",driver.current_url)
        
    def testLoginUserLogout(self):
        for driver in self.drivers:
            driver.get("http://127.0.0.1:8000/")
            self.assertIn("Think Ahead",driver.title)
            elem = driver.find_element_by_name("username")
            elem.send_keys("test")
            elem = driver.find_element_by_name("password")
            elem.send_keys("test")
            elem = driver.find_element_by_name("login")
            elem.click()
            elem = driver.find_element_by_name("logout")
            elem.click()
            self.assertIn("home",driver.current_url)

    def testCreateUserNoPasswordError(self):
        for driver in self.drivers:
            driver.get("http://127.0.0.1:8000/")
            self.assertIn("Think Ahead",driver.title)
            elem = driver.find_element_by_name("username")
            elem.send_keys("selenium")
            elem = driver.find_element_by_name("add")
            elem.click()
            self.assertTrue(driver.find_element_by_class_name("errorlist"))

    def testCreateUserNoUsernameError(self):
        for driver in self.drivers:
            driver.get("http://127.0.0.1:8000/")
            self.assertIn("Think Ahead",driver.title)
            elem = driver.find_element_by_name("password")
            elem.send_keys("pass")
            elem = driver.find_element_by_name("add")
            elem.click()
            self.assertTrue(driver.find_element_by_class_name("errorlist"))
    
    def testLoginNoPasswordError(self):
        for driver in self.drivers:
            driver.get("http://127.0.0.1:8000/")
            self.assertIn("Think Ahead",driver.title)
            elem = driver.find_element_by_name("username")
            elem.send_keys("userFail1")
            elem = driver.find_element_by_name("login")
            elem.click()
            self.assertTrue(driver.find_element_by_class_name("errorlist"))

    def testLoginNoUsernameError(self):
        for driver in self.drivers:
            driver.get("http://127.0.0.1:8000/")
            self.assertIn("Think Ahead",driver.title)
            elem = driver.find_element_by_name("password")
            elem.send_keys("pass")
            elem = driver.find_element_by_name("login")
            elem.click()
            self.assertTrue(driver.find_element_by_class_name("errorlist"))

    def testForgotPassword(self):
        for driver in self.drivers:
            driver.get("http://127.0.0.1:8000/")
            self.assertIn("Think Ahead",driver.title)
            forgot_link = driver.find_element_by_link_text('Forgot password?')
            forgot_link.click()
            self.assertIn("password/reset",driver.current_url)
            email = driver.find_element_by_name('email')
            email.send_keys("test@test.com")
            reset = driver.find_element_by_class_name('button')
            reset.click()
            self.assertIn("password/reset/done",driver.current_url)

    def testLoginUserUpdateProfile(self):    
        for driver in self.drivers:
            driver.get("http://127.0.0.1:8000/")
            self.assertIn("Think Ahead",driver.title)
            elem = driver.find_element_by_name("username")
            elem.send_keys("test")
            elem = driver.find_element_by_name("password")
            elem.send_keys("test")
            elem = driver.find_element_by_name("login")
            elem.click()
            elem = driver.find_element_by_xpath("//a[@href='/profile']")
            elem.click()
            self.assertIn("profile",driver.current_url)
            elem = driver.find_element_by_name("email")
            elem.send_keys("\b"*len("test@test.gmail.com"))
            elem.send_keys("newemail@test.gmail.com")
            elem = driver.find_element_by_id("createUser")
            elem.click()
            self.assertIn("dashboard",driver.current_url)
            elem = driver.find_element_by_id("profileNotification")
            self.assertTrue(elem.is_displayed())
            elem.click()
            elem = driver.find_element_by_name("logout")
            elem.click()

    def testLoginUserVisitProfile(self):    
        for driver in self.drivers:
            driver.get("http://127.0.0.1:8000/")
            self.assertIn("Think Ahead",driver.title)
            elem = driver.find_element_by_name("username")
            elem.send_keys("test")
            elem = driver.find_element_by_name("password")
            elem.send_keys("test")
            elem = driver.find_element_by_name("login")
            elem.click()
            elem = driver.find_element_by_xpath("//a[@href='/profile']")
            elem.click()
            self.assertIn("profile",driver.current_url)
            elem = driver.find_element_by_class_name("logoHead")
            elem.click()
            self.assertIn("dashboard",driver.current_url)
            elem = driver.find_element_by_id("profileNotification")
            self.assertFalse(elem.is_displayed())
            elem = driver.find_element_by_name("logout")
            elem.click()
        
    def tearDown(self):
        for driver in self.drivers:
            driver.close()
