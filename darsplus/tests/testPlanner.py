"""
Test suite for Planner database in models.py
Tests all methods defined in the class, but not the wrapper methods

To run, type "python manage.py test darsplus.tests.testPlanner"
"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import Planner

class TestPlanner(TestCase):        

    def testAddSimple(self):
        
        #Currently IDs increment from 0
        response = Planner.addPlanner()
        valid = response >= 0
        self.assertEquals(True, valid)
        num = Planner.objects.all().count()
        self.assertEquals(1, num)
        
    
    def testAddMultiplePlanner(self):
        allIDs = set()
        for i in range(1,1):
            newID = Planner.addPlanner()
            num = Planner.objects.all().count()        
            self.assertEquals(i, num)
            self.assertNotIn(newID, allIDs)
            allIDs.add(newID)
    
    def testAddCourse(self):
        newID = Planner.addPlanner()
        response = Planner.addCourseToPlanner(newID, 1, "DUTCH 107")
        self.assertEquals(SUCCESS, response)
        
