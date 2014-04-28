"""
Test suite for wrapper functions in models.py

To run, type "python manage.py test darsplus.tests.testAbbreviations"
"""

from django.test import TestCase
from darsplus.views import *

class TestWrappers(TestCase):

    def testStandardizeCourse(self):
        """ Ensure course name can be converted to database format """
        courses = ['cs169', 'cs 169', 'CS169', 'CS 169', 'cs.169', 'COMPSCI.169','COMPSCI.169']
        dbCourse = 'COMPSCI.169'
        for course in courses:
            self.assertEqual(dbCourse, standardizeCourse(course))
            
        courses = ['ee122', 'ee 122', 'EE122', 'EE 122']
        dbCourse = 'ELENG.122'
        for course in courses:
            self.assertEqual(dbCourse, standardizeCourse(course))           
        
    def testDbToReadable(self):
        """ Ensure database names can be converted to human readable """
        dbCourses = ['COMPSCI.169', 'ELENG.122', 'ECON.100A']
        courses = ['CS 169', 'EE 122', 'ECON 100A']
        for course in range(len(dbCourses)):
            self.assertEqual(courses[course],dbToReadable(dbCourses[course]))