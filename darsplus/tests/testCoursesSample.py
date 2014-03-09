"""
Test suite for Courses database in models.py
Does NOT test with actual data in the Courses table. Manually create a smaller one for easier testing. For a test suite with the actual data, see testCoursesActual.py 
Tests all methods defined in the class, but not the wrapper methods

To run, type "python manage.py test darsplus/tests/testCourses.py"
"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import * 

class TestCoursesSample(TestCase):
    def setUp(self):
        Courses.objects.create(courseCode = "COMPSCI 61B", courseName = "Algorithms and Data Structures",
                               courseDescription = "Super Special Awesome", courseLevel = UNDERGRADUATE,
                               minUnit = 4, maxUnit = 4, department = "Computer Science")
        Courses.objects.create(courseCode = "COMPSCI 61AS", courseName = "Structures and Interpretation of Computer Programming",
                               courseDescripition = "Special Awesome", courseLevel = UNDERGRADUATE,
                               minUnit = 1, maxUnit = 4, department = "Computer Science")
        Courses.objects.create(courseCode = "ECON C110", courseName = "Game Theory in the Social Sciences", courseDescription = "Game theory stuff", courseLevel = UNDERGRADUATE, 
                               minUnit = 3, maxUnit = 3, department = "Economics")
        
        
    def testGetCourseUnits(self):
        units = Planner.getCourseUnits("CS61B")
        self.assertEquals(4, units)
        units = Planner.getCourseUnits("CS61 AS")
        self.assertEquals(4, units)
        units = Planner.getCourseUnits("ECON C110")
        self.assertEquals(3, units)
    
    
