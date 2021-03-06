"""
Test suite for Colleges database in models.py
Tests all methods defined in the class, but not the wrapper methods

"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import Colleges, getCollegesToMajors, majorToCollege

class TestColleges(TestCase):

    def testMajorToCollege(self):
        """ Ensure major maps to correct college """
        response = Colleges.majorToCollege('Computer Science')
        self.assertEqual(response, 'College of Letters and Science')
        response = Colleges.majorToCollege('Economics')
        self.assertEqual(response, 'College of Letters and Science')
        response = Colleges.majorToCollege('Electrical Engineering and Computer Sciences')
        self.assertEquals(response, 'College of Engineering')

    def testGetCollegesToMajors(self):
        """
        Should create a dictioanry with keys as colleges and value as lists of majors in that college
        """
        response = getCollegesToMajors()
        self.assertEquals(6, len(response))
