"""
Test suite for Planner database in models.py
Tests all methods defined in the class, but not the wrapper methods

To run, type "python manage.py test darsplus.tests.testPlanner"
"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import Planner
from darsplus.models import Courses
from decimal import *

class TestPlanner(TestCase):        

    def setUp(self):
        """ Create planner objects to test planner functions """
        userID = Planner.addPlanner()
        Planner.addCourseToPlanner(userID, 1,"COMPSCI.169")
        Planner.addCourseToPlanner(userID, 15,"COMPSCI.161")

    def testAddPlanner(self):
        """ Ensure a planner can be added """
        response = Planner.addPlanner()
        self.assertEquals(SUCCESS, response)
        self.assertEquals(2, Planner.objects.all().count())

    def testAddMultiplePlanner(self):
        """ Ensure multiple planners can be added """
        offset = Planner.objects.all().count()
        allIDs = set()
        for i in range(1,2):
            newID = Planner.addPlanner()
            num = Planner.objects.all().count()        
            self.assertEquals(i+offset, num)
            self.assertNotIn(newID, allIDs)
            allIDs.add(newID)

    def testAddCourseToPlanner(self):
        """ Ensure courses can be added to semesters"""
        newID = Planner.addPlanner()
        for semester in range(1,15):
            response = Planner.addCourseToPlanner(newID,semester,"COMPSCI.169")
            self.assertEquals(SUCCESS, response)
        for semester in range(1,15):
            response = Planner.totalUnitsPlanner(newID, semester)
            self.assertEquals(4, response)

    def testAddCourseToPlannerError(self):
        """ Ensure adding duplicate course returns error """
        response = Planner.addCourseToPlanner(0,1, "COMPSCI.169")
        self.assertEquals(ERR_RECORD_EXISTS,response)

    def testRemoveCourseFromPlanner(self):
        """ Ensure courses can be removed from the planner """
        planner = Planner.objects.filter(plannerID = 0)[0]
        plannerID = planner.plannerID
        response = Planner.removeCourseFromPlanner(plannerID,1,"COMPSCI.169")
        self.assertEquals(SUCCESS, response)
        response = Planner.removeCourseFromPlanner(plannerID,1,"COMPSCI.169")
        self.assertEquals(ERR_NO_RECORD_FOUND, response)

    def testTotalUnitsPlannerSimple(self):
        """ Ensure totalUnits calculates total units correctly for single course """
        response = Planner.totalUnitsPlanner(0,15)
        self.assertEquals(4,response)

    def testTotalUnitsPlanner(self):
        """ Ensure totalUnits calculates total units correctly for multiple courses """
        newID = Planner.addPlanner()
        semester = 7 #arbitary semester number 
        courseList = ['COMPSCI.61AS', 'COMPSCI.169', 'COMPSCI.150', 'COMPSCI.195']
        for course in courseList:
            Planner.addCourseToPlanner(newID, semester, course)
        self.assertEquals(14.0, Planner.totalUnitsPlanner(newID, semester))

    def testSetPlannerNew(self):
        """ Tests that you can set on a blank planner
        """
        planner = Planner.objects.filter(plannerID = 0)[0]
        plannerID = planner.plannerID
        response = Planner.setPlanner(plannerID, 2, ['COMPSCI.61A','COMPSCI.61B'])
        self.assertEquals(SUCCESS, response)

        planner = Planner.objects.filter(plannerID = 0)[0]
        planner2 = planner.semester2
        self.assertIn('COMPSCI.61A', planner2)
        self.assertIn('COMPSCI.61B', planner2)
        self.assertEquals(4,  Planner.totalUnitsPlanner(0,1))
    
    def testSetPlannerFail(self):
        """ Tests that you don't call setPlanner with invalid index
        """
        planner = Planner.objects.filter(plannerID = 0)[0]
        plannerID = planner.plannerID
        response = Planner.setPlanner(plannerID, 0, ['COMPSCI.61A','COMPSCI.61B'])
        self.assertEquals(ERR_NO_RECORD_FOUND, response)
        response = Planner.setPlanner(plannerID, 16, ['COMPSCI.61A','COMPSCI.61B'])
        self.assertEquals(ERR_NO_RECORD_FOUND, response)

    def testSetPlannerOverwrite(self):
        """ Tests that if you set a planner on something that has a planner, you overwrite it.
        Note that the planner has 169 in semester1 and 161 in semester15
        """
        planner = Planner.objects.filter(plannerID = 0)[0]
        plannerID = planner.plannerID
        response = Planner.setPlanner(plannerID, 1, ['COMPSCI.61AS'])
        planner = Planner.objects.filter(plannerID = 0)[0]
        self.assertIn('COMPSCI.61AS', planner.semester1)
        self.assertEquals(1, len(planner.semester1))

        response = Planner.setPlanner(plannerID, 15, ['COMPSCI.61B','COMPSCI.161'])
        planner = Planner.objects.filter(plannerID = 0)[0]
        self.assertIn('COMPSCI.61B', planner.semester15)
        self.assertIn('COMPSCI.161', planner.semester15)
        self.assertEquals(2, len(planner.semester15))
        
