"""
Test suite for Courses database in models.py
Tests all methods defined in the class, but not the wrapper methods
Tests mainly getCourseUnits and loadCourses but for more comprehensive test in loadCourses, check testLoadCourses.py

To run, type "python manage.py test thinkahead/thinkahead/tests"
"""

from django.test import TestCase
from darsplus.models import Courses
from darsplus.utils import *

class TestCourses(TestCase):

    def testGetCourseUnits(self):
        units = Courses.getCourseUnits("COMPSCI.61B")
        self.assertEquals(4, units)
        units = Courses.getCourseUnits("COMPSCI.61AS")
        self.assertEquals(4, units)
        units = Courses.getCourseUnits("ELENG.42")
        self.assertEquals(3, units)

    """
    def testLoadCourses(self):
        response = Courses.loadCourses()
        self.assertEquals(SUCCESS, response)
        course = Courses.getCourseInfo("COMPSCI.61A")
        self.assertEquals(course.courseName, "The Structure and Interpretation of Computer Programs")
    """
