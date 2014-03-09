"""
Test suite for Planner database in models.py
Tests all methods defined in the class, but not the wrapper methods

To run, type "python manage.py test darsplus.tests.testPlanner"
"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import Planner

class TestPlanner(TestCase):        

    def setUp(self):
        Planner.addPlanner()
        Planner.addCourseToPlanner(0,1,"COMPSCI 169")
        Planner.addCourseToPlanner(0,15,"COMPSCI 161")

    def testAddPlanner(self):
        response = Planner.addPlanner()
        self.assertEquals(SUCCESS, response)
        self.assertEquals(2, Planner.objects.all().count())

    def testAddMultiplePlanner(self):
        #TODO: Need to change since planners added in setup
        offset = Planner.objects.all().count()
        allIDs = set()
        for i in range(1,1):
            newID = Planner.addPlanner()
            num = Planner.objects.all().count()        
            self.assertEquals(i+offset, num)
            self.assertNotIn(newID, allIDs)
            allIDs.add(newID)

    def testAddCourseToPlanner(self):
        error = False
        for semester in range(1,15):
            response = Planner.addCourseToPlanner(0,semester,"COMPSCI 169")
            self.assertEquals(SUCCESS, response)

    def testAddCourseToPlannerError(self):
        response = Planner.addCourseToPlanner(1,1, "COMPSCI 169")

    def testRemoveCourseFromPlanner(self):
        response = Planner.removeCourseFromPlanner(0,1,"COMPSCI 169")
        self.assertEquals(SUCCESS, response)
        response = Planner.removeCourseFromPlanner(0,1,"COMPSCI 169")
        self.assertEquals(ERR_NO_RECORD_FOUND, response)

    def testTotalUnitsPlanner(self):
        response = Planner.totalUnitsPlanner(0,15)
        self.assertEquals(4,response)
