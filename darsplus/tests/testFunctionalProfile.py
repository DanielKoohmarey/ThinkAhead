from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from darsplus.models import *
from darsplus.utils import *
import json
client=Client()
managementForm = {'form-TOTAL_FORMS': u'1','form-INITIAL_FORMS': u'0','form-MAX_NUM_FORMS': u''} # Default Dictionary for management form validation. has ONE form by default

class TestProfileUpdate(TestCase):
    def setUp(self):
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        request = {'major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'email':'johnsmith@berkeley.edu', 'form-0-name':['COMPSCI 61A'],}
        request.update(managementForm)
        response = client.post('/registration/', request)


    def testUpdateProfile(self):
        # Ensures that the profile page allows the profile to be updated
        request = {'major':['Nuclear Engineering'],'college':['College of Engineering'],
                   'semester':['Spring'], 'year':[2017],'email':'johnsmith@berkeley.edu'}
        request.update(managementForm)
        response = client.post('/profile/', request)
        
        username = User.objects.filter(username='john')[0].username
        profile = getUserProfile(username)
        self.assertEquals('Nuclear Engineering', profile.major)
        self.assertEquals(2017, profile.graduationYear)
        self.assertEquals('Spring', profile.graduationSemester)

    def testMultipleCourse(self):
        # Ensures that the profile page allows you to add multiple courses
        request = {'email':'johnsmith@berkeley.edu','major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':['COMPSCI.61A'],'form-1-name':['ELENG.42'], 'form-2-name':['BIOLOGY.1A']}
        request.update(managementForm)
        request['form-TOTAL_FORMS']=3
        response = client.post('/profile/', request)
        
        courses = ['COMPSCI.61A', 'ELENG.42', 'BIOLOGY.1A']
        profile = getUserProfile('john')
        for course in courses:
            self.assertIn(course, profile.coursesTaken)
        self.assertEquals(4+3+3, profile.unitsCompleted)

    def testRemoveCourses(self):
        # Asserts that you can remove all courses taken
        request = {'email':'johnsmith@berkeley.edu','major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'form-0-name':[]}
        request.update(managementForm)
        request['form-TOTAL_FORMS']=0
        response = client.post('/profile/', request)

        profile = getUserProfile('john')
        self.assertEquals([],profile.coursesTaken)
        self.assertEquals(0, profile.unitsCompleted)
            
    def testAutoPopulate(self):
        # Ensures that the profile page opens with previous profile prepopulated
        # Currently does not work with major and college
        response = client.get('/profile/', managementForm)
        elements = ['johnsmith@berkeley.edu','College of Engineering', 'Summer', str(2015), 'COMPSCI 61A']
        for element in elements:
            self.assertIn(element, response.content)
        

    
