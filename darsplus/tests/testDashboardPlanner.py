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

    def testBadYear(self):
        self.assertEquals(ERR_INVALID_DATE, diffDates('Fall', 2017, 'Fall', 2016)) # Old year is in the future
        self.assertEquals(ERR_INVALID_DATE, diffDates('Winter', 2015, 'Fall', 2016)) # Winters don't exist
        self.assertEquals(ERR_INVALID_DATE, diffDates('Fall', 2015, 'Winter', 2016))
        self.assertEquals(ERR_INVALID_DATE, diffDates('Fall', 2015, 'Winter', 2016))

    def testEqualYear(self):
        self.assertEquals(0, diffDates('Spring', 2016, 'Spring', 2016)) # Old year is in the future
        self.assertEquals(1, diffDates('Spring', 2016, 'Summer', 2016)) # Old year is in the future
        self.assertEquals(2, diffDates('Spring', 2016, 'Fall', 2016)) # Old year is in the future

        self.assertEquals(ERR_INVALID_DATE, diffDates('Summer', 2016, 'Spring', 2016))
        self.assertEquals(0, diffDates('Summer', 2016, 'Summer', 2016))
        self.assertEquals(1, diffDates('Summer', 2016, 'Fall', 2016)) 

        self.assertEquals(ERR_INVALID_DATE, diffDates('Summer', 2016, 'Spring', 2016))
        self.assertEquals(0, diffDates('Summer', 2016, 'Summer', 2016))
        self.assertEquals(1, diffDates('Summer', 2016, 'Fall', 2016)) 
