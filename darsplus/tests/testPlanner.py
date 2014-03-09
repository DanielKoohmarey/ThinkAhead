"""
Test suite for Planner database in models.py
Tests all methods defined in the class, but not the wrapper methods

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

