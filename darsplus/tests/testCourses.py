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

    def setUp(self):
        self.algorithm = Courses.objects.create(courseCode = "COMPSCI 61B", courseName = "Algorithms and Data Structures",
                               courseDescription = "Super Special Awesome", courseLevel = LOWER_DIVISION,
                               minUnit = 4, maxUnit = 4, department = "Computer Science")
        self.sicp = Courses.objects.create(courseCode = "COMPSCI 61AS", courseName = "Structures and Interpretation of Computer Programming",
                               courseDescription = "Special Awesome", courseLevel = LOWER_DIVISION,
                               minUnit = 1, maxUnit = 4, department = "Computer Science")
        self.econ = Courses.objects.create(courseCode = "ECON C110", courseName = "Game Theory in the Social Sciences", courseDescription = "Game theory stuff", courseLevel = UPPER_DIVISION,
                               minUnit = 3, maxUnit = 3, department = "Economics")
    def testGetCourseUnits(self):
        units = Courses.getCourseUnits("COMPSCI 61B")
        self.assertEquals(4, units)
        units = Courses.getCourseUnits("COMPSCI 61AS")
        self.assertEquals(4, units)
        units = Courses.getCourseUnits("ECON C110")
        self.assertEquals(3, units)

    def testLoadCourses(self):
        response = Courses.loadCourses()
        self.assertEquals(SUCCESS, response)
        course = Courses.getcourseInfo("COMPSCI 61A")
        self.assertEquals(course.courseName, "Structure and Interpretation of Computer Programs")
