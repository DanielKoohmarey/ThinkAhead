import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from darsplus.models import UserProfile

if not User.objects.filter(username='test'):
    new_user = User.objects.create_user(username='test',password='test', email='test@test.com')
    new_user.save()
if not UserProfile.objects.filter(username="test"):
    UserProfile.addUserProfile("test","Electrical Engineering and Computer Sciences",'College of Engineering',
                                                     "Fall", "2014",[])

testUsers = ['selenium', 'seleniumR']
for name in testUsers:
    testUser = User.objects.filter(username=str(name))
    if testUser:
        User.delete(testUser[0])
    profile = UserProfile.objects.filter(username=str(name))
    if profile:
        profile[0].delete()

class testGUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def testCreateUserRegister(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("seleniumR")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("pass")
        elem = self.driver.find_element_by_name("add")
        elem.click()
        elem = self.driver.find_element_by_name("email")
        elem.send_keys("test@test.com")
        college = self.driver.find_element_by_name("college")
        college.click()
        elem = self.driver.find_element_by_xpath('/html/body/div/div/form/div[3]/select/option[5]')
        elem.click()
        college.send_keys(Keys.RETURN)
        major = self.driver.find_element_by_name("major")
        major.click()
        elem = self.driver.find_element_by_xpath('/html/body/div/div/form/div[3]/select[2]/option[4]')
        elem.click()
        major.send_keys(Keys.RETURN)        
        elem = self.driver.find_element_by_name("form-0-name")
        elem.send_keys("CS 70")
        elem = self.driver.find_element_by_id("createUser")
        elem.click()
        elem = self.driver.find_element_by_id("simplemodal-data")
        self.assertTrue(elem.is_displayed())
        self.assertIn("dashboard",self.driver.current_url)
        elem = self.driver.find_element_by_name("logout")
        elem.click()
     
     #The validation function prevents logging out only in tests, not local
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
        """
        elem = self.driver.find_element_by_name("logout")
        elem.click()
        """
        self.driver.get("http://127.0.0.1:8000/logout/")
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
        elem = self.driver.find_element_by_name("profile")
        elem.click()
        self.assertIn("profile",self.driver.current_url)
        elem = self.driver.find_element_by_name("email")
        elem.send_keys("\b"*len("test@test.gmail.com"))
        elem.send_keys("newemail@test.gmail.com")
        elem = self.driver.find_element_by_id("createUser")
        elem.click()
        self.assertIn("dashboard",self.driver.current_url)
        elem = self.driver.find_element_by_id("simplemodal-data")
        self.assertTrue(elem.is_displayed())
        elem.click()
        elem = self.driver.find_element_by_name("logout")
        elem.click()

    def testLoginUserVisitProfile(self):    
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("Think Ahead",self.driver.title)
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("test")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("test")
        elem = self.driver.find_element_by_name("login")
        elem.click()
        elem = self.driver.find_element_by_name("profile")
        elem.click()
        self.assertIn("profile",self.driver.current_url)
        elem = self.driver.find_element_by_class_name("logoHead")
        elem.click()
        self.assertIn("dashboard",self.driver.current_url)
        try:
            elem = self.driver.find_element_by_id("simplemodal-data")
            self.assertFalse(True)
        except:
            pass
        elem = self.driver.find_element_by_name("logout")
        elem.click()
    
    def tearDown(self):
        self.driver.close()