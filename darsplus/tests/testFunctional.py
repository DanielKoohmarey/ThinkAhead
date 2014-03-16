from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from darsplus.models import *
from darsplus.utils import *
import json
client=Client()

class TestUserCase(TestCase):
        
    def testHomePage(self):
        """ Expect login page exists at url /home/ """
        response = client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def testCreateUser(self):
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        self.assertEqual(302, response.status_code)
        self.assertIn('/registration/', response.url)
        self.assertEquals(1,User.objects.filter(username='john').count())

    
    def testRegisterPage(self):
        """ Expect login page exists at url /registration/. Redicrects to home if not logged in """
        response = client.get('/registration/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/home/', response.url)
        
    def testDashboardPage(self):
        """ Expect login page exists at url /dashboard/. Redirects to home if not logged in """
        response = client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/home', response.url)

    def testRegisterRedirect(self):
        # Exepct registration without authenticated login to redirect 
        response = client.post('/registration/',{'user':'john','password':'pass'})
        self.assertEqual(302, response.status_code)
        self.assertIn('/home', response.url)

    def testCreateNoUser(self):
        # Expect Invalid username to be blank
        response = client.post('',{'username':'', 'password':'pass','add':"Create User"})
        self.assertIn('This field is required.',response.context['errors']['username'])
    
    def testAddLongPass(self):
        # Expect forms' default error message when field is too long
        response = client.post('',{'username':'', 'password':'c'*129,'add':"Create User"})       
        self.assertIn('Ensure this value has at most 128 characters (it has 129).', response.context['errors']['password'])

    def testDuplicateLogin(self):
        # Adding a second username should error
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        self.assertEquals("Username is already taken.", response.context['errors'])


    def testLogin(self):
        """ Logins in a user correctly """
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        response = client.post('',{'username':'john', 'password':'pass', 'login':'Login'})
        self.assertEquals(302, response.status_code)
        self.assertIn('/dashboard/', response.url)
        user = User.objects.filter(username='john')[0]
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_authenticated())
        

    def testInvalidLogin(self):
        """ If password does not match, return error message  """
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        response = client.post('',{'username':'john', 'password':'otherpass', 'login':'Login'})
        self.assertEquals(200, response.status_code)
        user = User.objects.filter(username='john')[0]
        self.assertIn('Invalid Username/Password. Please try again', response.context['errors'])
    
    """
    def testDasboardLoggedIn(self):
        client = Client()
        response = client.post('',{'username':'smith', 'password':'pass','add':"Create User"})
        #response = client.post('',{'username':'smith', 'password':'pass', 'login':'Login'})
        response = client.login(username='smith', password='pass')
        print ">>>>>>>>>>>>>>>>>>"
        print response
        user = User.objects.filter(username='smith')[0]
        print user.is_active
        print user.is_authenticated()
        print client
        print (dir (client))
        response = client.post('/dashboard',{})
        print "<<<<<<<<<<<<<<<"
        self.assertTrue(response)
        self.assertEquals(302, response.status_code)
        response = client.post('/dashboard', json.dumps({'username':'test', 'password':'pass'}))
        self.assertNotEquals(False, response)

    def testDasboardBadLogin(self):
        c = Client()
        response = c.post('/register',json.dumps({'user':'test','password':'pass'}),content_type="application/json")
        response = c.login(username='test', password='fakepass')
        self.assertFalse(response)


    def testUserProfile(self):
        #Tests that upon user creatoin, the corresponding entry in UserProfile are added
        response = client.post('/register',json.dumps({'username':'john','college': 'College of Engineering', 'major':'Chemistry','year':2014,'semester':'Fall'}),content_type="application/json")
        self.assertEquals(1, UserProfile.objects.all().count())
        courseInfo = UserProfile.getCourseInfo('john')
        self.assertEquals('Chemistry', courseInfo.major)
        self.assertEquals(2014, courseInfo.graduationYear)
        self.assertEquals('Fall', courseInfo.graduationSemester)

    def testPlanner(self):
        # Tests that upon user creatoin, the corresponding entry in Planner are added 
        response = client.post('/register',json.dumps({'username':'john','college': 'College of Engineering', 'major':'Chemistry','year':2014,'semester':'Fall'}),content_type="application/json")
        self.assertEquals(1, Planner.objects.all().count())
   

   
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
