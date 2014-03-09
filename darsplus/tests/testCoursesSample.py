"""
Test suite for Courses database in models.py
Does NOT test with actual data in the Courses table. Manually create a smaller one for easier testing. For a test suite with the actual data, see testCoursesActual.py 
Tests all methods defined in the class, but not the wrapper methods

To run, type "python manage.py test darsplus.tests.testCourses."
"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import Courses

class TestCoursesSample(TestCase):
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
    
    
