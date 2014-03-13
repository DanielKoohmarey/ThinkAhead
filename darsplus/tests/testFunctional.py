from django.test import TestCase
#from darsplus.models import UserModel as User
from django.test.client import Client
import json
client=Client()

class TestUserCase(TestCase):
        
    def testHomePage(self):
        """ Expect login page exists at url /home/ """
        response = client.get('/home/')
        self.assertEqual(response.status_code, 200)
        
    def testRegisterPage(self):
        """ Expect login page exists at url /register/ """
        response = client.get('/register/')
        self.assertEqual(response.status_code, 200)
        
    def testDashboardPage(self):
        """ Expect login page exists at url /dashboard/ """
        response = client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def testLoginNoUser(self):
        """ Expect ERR_BAD_USERNAME, """
        response = client.post('/register',json.dumps({'user':'','password':'pass'}),content_type="application/json")
        response = json.loads(response.content)        
        self.assertEqual(response['errors'],'Invalid Username or Password.')
    
    def testAddLongPass(self):
        """ Expect ERR_BAD_PASSWORD """
        response = client.post('/register',json.dumps({'user':'test','password':'c'*139}),content_type="application/json")
        response = json.loads(response.content)        
        self.assertEqual(response['errors'],'Invalid Username or Password')
