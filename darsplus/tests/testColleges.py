"""
Test suite for Colleges database in models.py
Tests all methods defined in the class, but not the wrapper methods

"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import Colleges

class TestColleges(TestCase):

    def setUp(self):
        """ Create college objects with major mappings """
        self.college = Colleges.objects.create(major = 'Computer Science', college = 'Letters and Science')
        self.college = Colleges.objects.create(major = 'Economics', college = 'Letters and Science')
        self.college = Colleges.objects.create(major = 'EECS', college = 'Engineering')

    def testMajorToCollege(self):
        """ Ensure major maps to correct college """
        response = Colleges.majorToCollege('Computer Science')
        self.assertEqual(response, 'Letters and Science')
        response = Colleges.majorToCollege('Economics')
        self.assertEqual(response, 'Letters and Science')
        response = Colleges.majorToCollege('EECS')
        self.assertEquals(response, 'Engineering')
