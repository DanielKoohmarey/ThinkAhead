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
        Courses.loadCourses()

    def testCoursesFields(self):
        course = Courses.getCourseInfo("(COMPSCI) CS169")
        self.assertEqual(course.courseCode, "(COMPSCI) CS169")
        self.assertEqual(course.courseName, "Software Engineering")
        self.assertEqual(course.courseDescription, "Fall, Spring")
        self.assertEqual(course.courseLevel, "Undergraduate")
        self.assertEqual(course.minUnit, 4)
        self.assertEqual(course.maxUnit, 4)
        self.assertEqual(course.department, "Computer Science")

    def testGetCourseUnits(self):
        units = Course.getCourseUnits("(COMPSCI) 169")
        self.assertEqual(units, 4)

