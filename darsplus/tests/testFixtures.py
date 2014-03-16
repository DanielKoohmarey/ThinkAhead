"""
Test suite for Fixtures. Tests if the auto-populating fixture for the DB works
Not comprehensive and tests arbitary courses

To run, type "python manage.py test darsplus.tests.testFixtures"
"""

from django.test import TestCase
from darsplus.models import Courses, Colleges
from darsplus.utils import *

class TestFixtures(TestCase):
    fixtures = ['courses.json', 'colleges.json']

    def testCollegeToMajorSingle(self):
        """ Ensures that you can get the college of a major that has 1 college"""
        college = Colleges.majorToCollege('French')
        self.assertEquals('College of Letters and Science', college)
    
    def testCollegeToMajorMultiple(self):
        """ Ensures that you get a list of all the colleges that has that major"""
        colleges = Colleges.majorToCollege('Environmental Economics and Policy')
        self.assertEquals(2, len(colleges))
        self.assertIn('College of Natural Resources', colleges)
        self.assertIn('College of Letters and Science', colleges)
        
    def testCollegeToMajorNotExist(self):
        """ Ensures that if the major does not exist, return corresponding error message """
        college = Colleges.majorToCollege('League of Legends')
        self.assertEquals(ERR_NO_RECORD_FOUND, college)

    def testMajorsInCollege(self):
        """ Ensures that given a college, we can get list of majors inside that college """
        majors = Colleges.getMajorsInCollege('College of Chemistry')
        chemistry = ['Chemistry B.A.', 'Chemistry B.S.', 'Chemical Biology', 'Chemical Engineering',
                     'Chemical Engineering/Materials Science and Engineering',
                     'Chemical Engineering/Nuclear Engineering']
        self.assertEquals(len(chemistry), len(majors))
        for major in chemistry:
            self.assertIn(major, majors)
        
        majors = Colleges.getMajorsInCollege('College of Environmental Design')
        envdesign = ['Architecture', 'Landscape Architecture', 
                     'Sustainable Environmental Design',
                     'Urban Studies']
        self.assertEquals(len(envdesign), len(majors))
        for major in envdesign:
            self.assertIn(major, majors)

    def testCourseInfoSimple(self):
        """ Ensures that getCourseInfo gets the right info from the fixture """
        course = Courses.getCourseInfo('COMPSCI.169')
        self.assertEquals('Software Engineering', course.courseName)
        self.assertEquals('Fall and spring', course.courseDescription)
        self.assertEquals('Undergraduate', course.courseLevel)
        self.assertEquals(4, course.minUnit)
        self.assertEquals(4, course.maxUnit)
        self.assertEquals('Computer Science (COMPSCI)', course.department)

    def testCourseUnits(self):
        """
        Tests that courseUnits function with edge cases
        * non-integer number of units
        * variable nunber of untis
        """
        units = Courses.getCourseUnits('ELENG.42')
        self.assertEquals(3.0, units)
        
        units = Courses.getCourseUnits('PHYSED.3')
        self.assertEquals(0.5, units)

        units = Courses.getCourseUnits('COMPSCI.61AS')
        self.assertEquals(4, units)
    
        
        
