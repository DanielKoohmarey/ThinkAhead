from django.test import TestCase
from django.test.client import Client
from darsplus.models import *
from darsplus.utils import *
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
        response = client.post('/register/',json.dumps({'user':'','password':'pass'}),content_type="application/json")
        response = json.loads(response.content)        
        self.assertEqual(response['errors'],'Invalid Username or Password.')
    
    def testAddLongPass(self):
        """ Expect ERR_BAD_PASSWORD """
        response = client.post('/register',json.dumps({'user':'test','password':'c'*139}),content_type="application/json")
        response = json.loads(response.content)        
        self.assertEqual(response['errors'],'Invalid Username or Password')

    def testDuplicateLogin(self):
        """ Adding a second username should error """
        response = client.post('/register',json.dumps({'user':'test','password':'c'*139}),content_type="application/json")
        response = client.post('/register',json.dumps({'user':'test','password':'c'*139}),content_type="application/json")
        response = json.loads(response.content)        
        self.assertIn("Username is already taken", response)

    def testDasboardLoggedIn(self):
        c = Client()
        response = c.post('/register',json.dumps({'user':'test','password':'pass'}),content_type="application/json")
        response = c.login(username='test', password='pass')
        self.assertTrue(response)
        response = c.post('/dashboard', json.dumps({'username':'test', 'password':'pass'}))
        self.assertNotEquals(False, response)
        
    def testDasboardBadLogin(self):
        c = Client()
        response = c.post('/register',json.dumps({'user':'test','password':'pass'}),content_type="application/json")
        response = c.login(username='test', password='fakepass')
        self.assertFalse(response)


    def testUserProfile(self):
        """ Tests that upon user creatoin, the corresponding entry in UserProfile are added """
        response = client.post('/register',json.dumps({'username':'john','college': 'College of Engineering', 'major':'Chemistry','year':2014,'semester':'Fall'}),content_type="application/json")
        self.assertEquals(1, UserProfile.objects.all().count())
        courseInfo = UserProfile.getCourseInfo('john')
        self.assertEquals('Chemistry', courseInfo.major)
        self.assertEquals(2014, courseInfo.graduationYear)
        self.assertEquals('Fall', courseInfo.graduationSemester)

    def testPlanner(self):
        """ Tests that upon user creatoin, the corresponding entry in Planner are added """
        response = client.post('/register',json.dumps({'username':'john','college': 'College of Engineering', 'major':'Chemistry','year':2014,'semester':'Fall'}),content_type="application/json")
        self.assertEquals(1, Planner.objects.all().count())


    """
    def testChange(self):
        # Tests that upon user creation, you can alter the database
        response = client.post('/register',json.dumps({'username':'john','college': 'College of Engineering', 'major':'Chemistry','year':2014,'semester':'Fall'}),content_type="application/json")
        self.assertEquals(1, UserProfile.objects.all().count())
        response = changeGraduationSemester('john','Summer')
        self.assertEquals(SUCCESS, response)
        response = changeGraduationYear('john',2016)
        self.assertEquals(SUCCESS, response)
        response = changeMajor('john','Economics')
        self.assertEquals(SUCCESS, response)                
        courseInfo = UserProfile.getCourseInfo('john')
        self.assertEquals('Summer', courseInfo.graduationSemester)
        self.assertEquals(2016, courseInfo.graduationYear)
        self.assertEquals('Economics', courseInfo.major) 
    """
