"""
Test suite for Colleges database in models.py
Tests all methods defined in the class, but not the wrapper methods

"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import Colleges

class TestColleges(TestCase):

    def setUp(self):
        self.college = Colleges.objects.create(major = "Computer Science", college = "Letters and Science")

    def testMajorToCollege(self):
        response = Colleges.majorToCollege("Computer Science")
        self.assertEqual(response, "Letters and Science")
