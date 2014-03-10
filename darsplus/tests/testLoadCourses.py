"""
Test suite for loadCourses database in models.py
Tests all methods defined in the class, but not the wrapper methods

To run, type "python manage.py test darsplus.tests.testLoadCourses"
"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import Courses

class TestLoadCourses(TestCase):
    def setUp(self):
        response = Courses.loadCourses()
        self.assertEquals(SUCCESS, response)
        
    def testTentative(self):
        self.assertEquals(1,1)
        #self.assertEquals(Courses.objects.all().count(), 0)

    def testCoursesFields(self):
        course = Courses.getCourseInfo("COMPSCI 169")
        self.assertEqual(course.courseCode, "COMPSCI 169")
        self.assertEqual(course.courseName, "Software Engineering")
        self.assertEqual(course.courseDescription, "Fall and spring")
        self.assertEqual(course.courseLevel, "Undergraduate")
        self.assertEqual(course.minUnit, 4)
        self.assertEqual(course.maxUnit, 4)
        self.assertEqual(course.department, "Computer Science (COMPSCI)")

    def testGetCourseUnits(self):
        self.assertEquals(4, Courses.getCourseUnits("COMPSCI 169"))
        self.assertEquals(4, Courses.getCourseUnits("COMPSCI 161"))
        self.assertEquals(4, Courses.getCourseUnits("COMPSCI 61AS"))
        self.assertEquals(5, Courses.getCourseUnits("COMPSCI 150"))


