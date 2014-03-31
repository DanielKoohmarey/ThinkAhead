from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from darsplus.models import *
from darsplus.utils import *
import json
client=Client()
managementForm = {'form-TOTAL_FORMS': u'1','form-INITIAL_FORMS': u'0','form-MAX_NUM_FORMS': u''} # Default Dictionary for management form validation. has ONE form by default

class TestUserCase(TestCase):

    @staticmethod
    def strip(str):
        return str.replace('\t','').replace('\n','')

    def testHomePage(self):
        # Expect login page exists at url /home/
        response = client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def testCreateUser(self):
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        self.assertEqual(302, response.status_code)
        self.assertIn('/registration/', response.url)
        self.assertEquals(1,User.objects.filter(username='john').count())

    
    def testRegisterPage(self):
        # Expect login page exists at url /registration/. Redicrects to home if not logged in
        response = client.get('/registration/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/home/', response.url)
        
    def testDashboardPage(self):
        # Expect login page exists at url /dashboard/. Redirects to home if not logged in
        response = client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/home/', response.url)

    def testRegisterRedirect(self):
        # Exepct registration without authenticated login to redirect 
        response = client.post('/registration/',{'user':'john','password':'pass'})
        self.assertEqual(302, response.status_code)
        self.assertIn('/home/', response.url)

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
        self.assertIn("Username is already taken.", response.context['errors']['user'])


    def testLoginNotRegistered(self):
        # If user navigates to home with get/post request when logged in, redirects to registration
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        response = client.post('',{'username':'john', 'password':'pass', 'login':'Login'})
        self.assertEquals(302, response.status_code)
        self.assertIn('/dashboard/', response.url) # Redirected to Dashboard, and then to registration
        
    def testLogin(self):   
        client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        client.get('/logout/')
        response = client.post('',{'username':'john', 'password':'pass', 'login':'Login'})
        user = User.objects.filter(username='john')[0]
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_authenticated())
        self.assertEquals(302, response.status_code)
        self.assertIn('/dashboard/', response.url)    # Redirected to Dashboard, and then to registration
        
    def testInvalidLogin(self):
        # If password does not match, return error message
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        response = client.post('',{'username':'john', 'password':'otherpass', 'login':'Login'})
        self.assertEquals(200, response.status_code)
        self.assertIn('Invalid Username/Password. Please try again.', response.context['errors']['user'])
    

    def testProfileNotLoggedIn(self):
        # If going to registration without logging in, redirect to home
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        request = {'email':'johnsmith@berkeley.edu', 'major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':['CS 61A'],}
        request.update(managementForm)
        client.logout()
        response = client.post('/registration/', request)
        self.assertEquals(302, response.status_code)
        self.assertIn('/home/', response.url)
        profiles = UserProfile.objects.filter(username='john')
        self.assertEquals(0, profiles.count())

    def testProfileRegisterSuccess(self):
        # If going to register and logged in, should add to User Profile and Planner
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        request = {'email':'johnsmith@berkeley.edu', 'major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':['CS 61A'],}
        request.update(managementForm)
        response = client.post('/registration/', request)
        self.assertEquals(302, response.status_code)
        self.assertIn('/dashboard/', response.url)
        profiles = UserProfile.objects.filter(username='john')
        self.assertEquals(1, profiles.count())
        profile = profiles[0]
        self.assertEquals('Bioengineering', profile.major)
        self.assertEquals('College of Engineering', profile.college)
        self.assertEquals('Summer', profile.graduationSemester)
        self.assertEquals(2015, profile.graduationYear)
        self.assertIn('CS.61A', profile.coursesTaken)
        plannerID = profile.plannerID
        planner = Planner.objects.filter(plannerID=plannerID)
        self.assertEquals(1, planner.count())

    def testProfileNoCourse(self):
        # Test registering with no course taken. list of courses taken should be empty
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        request = {'email':'johnsmith@berkeley.edu','major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':[],}
        request.update(managementForm)
        response = client.post('/registration/', request)
        self.assertEquals(302, response.status_code)
        self.assertIn('/dashboard/', response.url)
        profiles = UserProfile.objects.filter(username='john')
        self.assertEquals(1, profiles.count())
        profile = profiles[0]
        self.assertEquals([], profile.coursesTaken)

    def testProfileMultipleCourses(self):
        # Test registering with multiple courses taken.All of the courses taken should be added to list of courses Taken
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        request = {'email':'johnsmith@berkeley.edu','major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':['CS 61A'],'form-1-name':['EE 42'], 'form-2-name':['BIO 1A']}
        request.update(managementForm)
        request['form-TOTAL_FORMS']=3
        response = client.post('/registration/', request)
        self.assertEquals(302, response.status_code)
        self.assertIn('/dashboard/', response.url)
        profiles = UserProfile.objects.filter(username='john')
        self.assertEquals(1, profiles.count())
        profile = profiles[0]
        self.assertIn('CS.61A', profile.coursesTaken)
        self.assertIn('EE.42', profile.coursesTaken)
        self.assertIn('BIO.1A', profile.coursesTaken)


    def testDashboardNotLoggedIn(self):
        # If trying to see dashboard without logging in, redirect to home
        response = client.post('/dashboard/',{})
        self.assertEquals(302, response.status_code)
        self.assertIn('/home/', response.url)
        

    def testDasboardLoggedInNotRegister(self):
        # If trying to see dashbaord, logged in, but not registered, sent to registration page to putin user profile
        response = client.post('',{'username':'smith', 'password':'pass','add':"Create User"})
        response = client.post('/dashboard/', {})
        self.assertEquals(302, response.status_code)
        self.assertIn('/registration/', response.url)

    def testDashboardLoggedInRegistered(self):
        # If logged in and registed, display dashboard
        response = client.post('',{'username':'smith', 'password':'pass','add':"Create User"})
        request = {'email':'johnsmith@berkeley.edu','major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':['CS 61A'],}
        request.update(managementForm)
        response = client.post('/registration/', request)
        response = client.get('/dashboard/',{})
        self.assertEquals(200, response.status_code)

    def testDasboardBadLogin(self):
        # If logged in with bad combination, redirects to home when accessing dashbaord
        response = client.post('',{'username':'smith', 'password':'pass','add':"Create User"})
        request = {'email':'johnsmith@berkeley.edu','major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':['CS 61A'],}
        request.update(managementForm)
        response = client.post('/registration/', request)
        client.logout()
        c = Client()
        c.login(username='smith',password='otherpass')
        response = c.post('/dashboard/',{})
        self.assertEquals(302, response.status_code)
        self.assertIn('/home/', response.url)


    def testLogoutLoggedIn(self):
        #Ensure logging out works when a user has oreviously logged in
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        
        user = User.objects.filter(username='john')[0]
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_authenticated())

        response = client.get('/logout/')

        user = User.objects.filter(username='john')[0]
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_authenticated())
        
        self.assertRedirects(response, '/home/', status_code=302, target_status_code=200, msg_prefix='')

    def testLogoutAnonymous(self):
        c = Client()
        response = c.post('/logout/', {})
        self.assertEquals(302, response.status_code)
        self.assertIn('/home/', response.url)
        

    def testMultipleLogin(self):
        # TODO: Create 2 accounts, different registration info. able to login and see corresponding dashboard
        """
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        request = {'email':'johnsmith@berkeley.edu', 'major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':['CS 61A'],}
        request.update(managementForm)
        response = client.post('/registration/', request)
        response = client.get('/dashboard/',{})


        response = client.post('',{'username':'smith', 'password':'otherpass','add':"Create User"})
        request = {'email':'goldsmith@berkeley.edu', 'major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':['CS 61B'],}
        request.update(managementForm)
        response = client.post('/registration/', request)       
        """
        pass

    def testGenerateRequirement(self):
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        request = {'email':'johnsmith@berkeley.edu', 'major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':['COMPSCI 61A'],}
        request.update(managementForm)
        response = client.post('/registration/', request)
        response = client.get('/dashboard/',{})

        body = response.content
        
        # University Requirement
        self.assertIn('<h3 class="reqTitle">American Cultures</h3><p class="reqDescription">Description: Take at least one course labeled AC </p><p>Requirement Completed: False</p>', self.strip(body))
        
        # Major Requirement
        self.assertIn('<h3 class="reqTitle">Introduction to Applied Computing</h3><p class="reqDescription">Description: The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A </p><p>Requirement Completed: True</p>', self.strip(body)) #Has COMPSCI 61A


        pass

