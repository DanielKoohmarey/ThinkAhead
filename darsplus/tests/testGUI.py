"""
from django.test import TestCase
from xpresser import Xpresser
xp = Xpresser()
xp.load_images('darsplus/tests/gui')
import time

class TestGUI(TestCase):

    def testCreateUser(self):
        xp.click("firefox")
        time.sleep(5)
        xp.click("urlBar")
        xp.type("http://127.0.0.1:8000/home/")
        xp.click("refresh")
        xp.click("username")
        xp.type("guitest")
        xp.click("password")
        xp.type("test")
        xp.click("createUser")
        time.sleep(1)
        error = False
        try:
            xp.find("registration")
        except:
            error = True
        self.assertFalse(error)
"""   
        
        
    