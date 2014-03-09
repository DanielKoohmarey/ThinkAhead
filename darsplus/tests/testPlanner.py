"""
Test suite for Planner database in models.py
Tests all methods defined in the class, but not the wrapper methods

<<<<<<< HEAD
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
        
=======
To run, type "python manage.py test thinkahead/thinkahead/tests"
"""

from django.test import TestCase
from thinkahead.thinkahead.models import Planner
from thinkahead.thinkahead.utils import *

class TestPlanner(TestCase):

    def setUp(self):
        Planner.addPlanner()
        Planner.addcoursetoPlanner(plannerID=0,0,"COMPSCI 169")
        Planner.addcoursetoPlanner(plannerID=0,14,"COMPSCI 161")

    def testAddPlanner(self):
        response = Planner.addPlanner()
        self.assertEquals(1, response)
        self.assertEquals(2, Planner.objects.all().count())

    def testAddCourseToPlanner(self):
        error = False
        for semester in range(14):
            response = Planner.addcoursetoPlanner(plannerID=0,semester,"COMPSCI 169")
            self.assertEquals(SUCCESS, response)
    def testAddCourseToPlannerError(self):
        response = Planner.addcoursetoPlanner(1,0, "COMPSCI 169")

    def testRemoveCourseFromPlanner(self):
        response = Planner.removeCourseFromPlanner(0,0,"COMPSCI 169")
        self.assertEquals(SUCCESS, response)
        response = Planner.removeCourseFromPlanner(0,0,"COMPSCI 169")
        self.assertEquals(ERR_NO_RECORD_FOUND, response)

    def testTotalUnitsPlanner(self):
        response = Planner.totalUnitsPlanner(0,14)
        self.assertEquals(4,response)

>>>>>>> fe197e9f157849fec2f46919724f9c380cd09487
