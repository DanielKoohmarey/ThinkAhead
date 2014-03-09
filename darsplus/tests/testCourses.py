"""
Test suite for Courses database in models.py
Tests all methods defined in the class, but not the wrapper methods

To run, type "python manage.py test thinkahead/thinkahead/tests"
"""

from django.test import TestCase
from thinkahead.thinkahead.models import Courses
from thinkahead.thinkahead.utils import *

class TestCourses(TestCase):

    def setUp(self):
        self.algorithm = Courses.objects.create(courseCode = "COMPSCI 61B", courseName = "Algorithms and Data Structures",
                               courseDescription = "Super Special Awesome", courseLevel = UNDERGRADUATE,
                               minUnit = 4, maxUnit = 4, department = "Computer Science")
        self.sicp = Courses.objects.create(courseCode = "COMPSCI 61AS", courseName = "Structures and Interpretation of Computer Programming",
                               courseDescription = "Special Awesome", courseLevel = UNDERGRADUATE,
                               minUnit = 1, maxUnit = 4, department = "Computer Science")
        self.econ = Courses.objects.create(courseCode = "ECON C110", courseName = "Game Theory in the Social Sciences", courseDescription = "Game theory stuff", courseLevel = UNDERGRADUATE, 
                               minUnit = 3, maxUnit = 3, department = "Economics")

    def testCoursesFields(self):
        course = Courses.getCourseInfo("COMPSCI CS169")
        self.assertEqual(course.courseCode, "COMPSCI CS169")
        self.assertEqual(course.courseName, "Software Engineering")
        self.assertEqual(course.courseDescription, "Fall, Spring")
        self.assertEqual(course.courseLevel, "Undergraduate")
        self.assertEqual(course.minUnit, 4)
        self.assertEqual(course.maxUnit, 4)
        self.assertEqual(course.department, "Computer Science")

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
