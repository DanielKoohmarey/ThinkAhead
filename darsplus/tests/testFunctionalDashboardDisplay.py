"""
Test suite for Planner database in models.py
Tests all methods defined in the class, but not the wrapper methods

To run, type "python manage.py test darsplus.tests.testPlanner"
"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import Planner
from darsplus.models import Courses
from darsplus.views import *
from django.test.client import Client
from django.contrib.auth.models import User
client=Client()
managementForm = {'form-TOTAL_FORMS': u'1','form-INITIAL_FORMS': u'0','form-MAX_NUM_FORMS': u''} # Default Dictionary for management form validation. has ONE form by default


class TestDashboard(TestCase):        
    def setUp(self):        
        response = client.post('',{'username':'john', 'password':'pass','add':"Create User"})
        request = {'major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2015],'email':'johnsmith@berkeley.edu', 'form-0-name':['COMPSCI 61A'],}
        request.update(managementForm)
        response = client.post('/registration/', request)

        response = client.post('',{'username':'smith', 'password':'otherpass','add':"Create User"})
        request = {'major':['Bioengineering'],'college':['College of Engineering'],
                   'semester':['Summer'], 'year':[2013],'email':'johnsmith@berkeley.edu', 'form-0-name':['COMPSCI 61A'],}
        request.update(managementForm)
        response = client.post('/registration/', request)

    def testBadYear(self):
        """ Makes sure that if years' order is switched or if Semester name does not exist, fail silently. 
        """
        self.assertEquals(ERR_INVALID_DATE, diffDates('Fall', 2017, 'Fall', 2016)) # Old year is in the future
        self.assertEquals(ERR_INVALID_DATE, diffDates('Winter', 2015, 'Fall', 2016)) # Winters don't exist
        self.assertEquals(ERR_INVALID_DATE, diffDates('Fall', 2015, 'Winter', 2016))
        self.assertEquals(ERR_INVALID_DATE, diffDates('Fall', 2015, 'Winter', 2016))

    def testEqualYear(self):
        """ Tests if right number of semesters are returned. Checking for a simple case where years are equal
        """
        self.assertEquals(0, diffDates('Spring', 2016, 'Spring', 2016)) # Old year is in the future
        self.assertEquals(1, diffDates('Spring', 2016, 'Summer', 2016)) # Old year is in the future
        self.assertEquals(2, diffDates('Spring', 2016, 'Fall', 2016)) # Old year is in the future

        self.assertEquals(ERR_INVALID_DATE, diffDates('Summer', 2016, 'Spring', 2016))
        self.assertEquals(0, diffDates('Summer', 2016, 'Summer', 2016))
        self.assertEquals(1, diffDates('Summer', 2016, 'Fall', 2016)) 

        self.assertEquals(ERR_INVALID_DATE, diffDates('Fall', 2016, 'Spring', 2016))
        self.assertEquals(ERR_INVALID_DATE, diffDates('Fall', 2016, 'Summer', 2016))
        self.assertEquals(0, diffDates('Fall', 2016, 'Fall', 2016)) 

    def testEqualSemester(self):
        self.assertEquals(3,diffDates('Summer',2016,'Summer',2017))
        self.assertEquals(6,diffDates('Summer',2016,'Summer',2018))

    def testEdges(self):
        """ Tests for asymetric dates and see if right number of semestrs are calcualted
        """
        self.assertEquals(2,diffDates('Summer',2016,'Spring',2017))
        self.assertEquals(4,diffDates('Summer',2016,'Fall',2017))

        self.assertEquals(4,diffDates('Spring',2016,'Summer',2017))
        self.assertEquals(2,diffDates('Fall',2016,'Summer',2017))

        self.assertEquals(5,diffDates('Summer',2016,'Spring',2018))
        self.assertEquals(7,diffDates('Summer',2016,'Fall',2018))

        self.assertEquals(7,diffDates('Spring',2016,'Summer',2018))
        self.assertEquals(5,diffDates('Fall',2016,'Summer',2018))

        self.assertEquals(8,diffDates('Spring',2016,'Fall',2018))
        self.assertEquals(4,diffDates('Fall',2016,'Spring',2018))


    def testFunctionalDashboard(self):
        """ Tests if the right number of planners are generated
        """
        client.login(username='john', password='pass')
        response = client.get('/dashboard/',{})
        body = response.content

        # TODO Not actual date dependant
        for index in range(1,4):
            self.assertIn("planner"+str(index), body)
        self.assertNotIn("planner5", body)

    def testFunctionalDashboardExpired(self):
        """ If the graduation date has passed, don't display any planner
        """
        client.login(username='smith', password='otherpass')
        response = client.get('/dashboard/',{})
        body = response.content

        # TODO Not actual date dependant
        self.assertNotIn("planner1", body)
            
    def testExpiredRestart(self):
        """ Tests that if graduation year expired but changed, right number is generated again
        """
        request = {'major':['Nuclear Engineering'],'college':['College of Engineering'],
                   'semester':['Spring'], 'year':[2016],'email':'johnsmith@berkeley.edu'}
        request.update(managementForm)
        client.login(username='smith', password='otherpass')
        response = client.post('/profile/', request)

        response = client.get('/dashboard/',{})
        body = response.content
        # TODO Not actual date dependant
        for index in range(1,6):
            self.assertIn("planner"+str(index), body)
        self.assertNotIn("planner7", body)
