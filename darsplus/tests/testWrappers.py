"""
Test suite for wrapper functions in models.py
Currently does not test majorToCollege due to no loadCollege defined

To run, type "python manage.py test darsplus.tests.testWrapper"
"""

from django.test import TestCase
from darsplus.models import *
from darsplus.utils import *

class TestCourses(TestCase):
    fixtures = ['courses.json', 'colleges.json']
    def setUp(self):
        """ Load courses and create user profiles for testing """
        response = addUserProfile('magikarp', 'EECS', SUMMER_SEMESTER, 2017)
        self.assertEquals(SUCCESS, response)
        numAccounts = UserProfile.objects.all().count()
        self.assertEquals(1, numAccounts)

    def testGetUserProfile(self):
        """ Ensure user profile can be retrieved correctly """
        user = UserProfile.getUserProfile("magikarp")
        self.assertTrue(user)
        
    def testAddUserProfileWrapper(self):
        """ Ensure addUserProfile creates profile correctly """
        response = addUserProfile('eevee', 'COMPSCI', FALL_SEMESTER, 2015)
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='eevee')[0]
        self.assertEquals('eevee', account.username)
        self.assertEquals('COMPSCI', account.major)
        self.assertEquals(FALL_SEMESTER, account.graduationSemester)
        self.assertEquals(2015, account.graduationYear)

    def testChangeGraduationSemesterWrapper(self):
        """ Ensure changeGraduationSemester changes user profile semester correctly """
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = changeGraduationSemester('magikarp', SPRING_SEMESTER)
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertEquals(SPRING_SEMESTER, account.graduationSemester)

    def testChangeGraduationYearWrapper(self):
        """ Ensure changeGraduationYear changes user profile graduation year correctly """
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = changeGraduationYear('magikarp', 2013)
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertEquals(2013, account.graduationYear)

    def testChangeMajorWrapper(self):
        """ Ensure changeMajor changes user profile major correctly """
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = changeMajor('magikarp', 'Economics')
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertEquals('Economics', account.major)

    def testGetCoursesTakenWrapper(self):
        """ Ensure getCoursestaken returns user profile courses taken correctly """
        response = getCoursesTaken('magikarp')
        self.assertEquals([], response)

    def testGetUnitsCompletedWrapper(self):
        """ Ensure getUnitsCompleted returns user profile units completed correctly """
        response = getUnitsCompleted('magikarp')
        self.assertEquals(0, response)

    def testAddCourseTakenWrapper(self):
        """ Ensure addCourseTaken updates user profile courses taken correctly """
        response = addCourseTaken('magikarp', 'COMPSCI 169')
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertIn('COMPSCI 169', account.coursesTaken)
        self.assertEquals(4, account.unitsCompleted)

    def testAddListCoursesTaken(self):
        """ Ensure addListCourseTaken updates user profile courses taken correctly """
        courseList = ['COMPSCI 169', 'COMPSCI 160', 'COMPSCI 61A']
        response = addListCoursesTaken('magikarp', courseList)
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertEquals(3, len(account.coursesTaken))
        for course in courseList:
            self.assertIn(course, account.coursesTaken)
        self.assertEquals(12, account.unitsCompleted)

    def testRemoveCourseTakenWrapper(self):
        """ Ensure removeCourseTaken updates user profile courses taken correctly """
        response = addCourseTaken('magikarp', 'COMPSCI 169')
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = removeCourseTaken('magikarp', 'COMPSCI 169')
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertNotIn('COMPSCI 169', account.coursesTaken)
        self.assertEquals(0, account.unitsCompleted)

    def testRemoveListCoursesTaken(self):
        """ Ensure removeListCourseTaken updates user profile courses taken correctly """
        courseList = ['COMPSCI 169', 'COMPSCI 160', 'COMPSCI 61A']
        subList = ['COMPSCI 169', 'COMPSCI 160']
        response = addListCoursesTaken('magikarp', courseList)
        response = removeListCoursesTaken('magikarp', subList)
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertIn('COMPSCI 61A', account.coursesTaken)
        self.assertNotIn('COMPSCI 169', account.coursesTaken)
        self.assertNotIn('COMPSCI 160', account.coursesTaken)
        self.assertEquals(4, account.unitsCompleted)

    def testPlannerWrapper(self):
        """ Ensure Planner wrapper function calls succeed """
        account = UserProfile.objects.filter(username='magikarp')[0]
        ID = account.plannerID
        response = addCourseToPlanner(ID, 8, 'COMPSCI 169') # 8 is an arbitary semester number
        self.assertEquals(SUCCESS, response)
        units = totalUnitsPlanner(ID, 8)
        self.assertEquals(4, units)
        response = removeCourseFromPlanner(ID, 8, 'COMPSCI 169')
        self.assertEquals(SUCCESS, response)
        units = totalUnitsPlanner(ID, 8)
        self.assertEquals(0, units)

    def testGetCourseUnitsWrapper(self):
        """ Ensure getCoursesUnits returns course units correctly """
        units = getCourseUnits('COMPSCI 169')
        self.assertEquals(4, units)
        units = getCourseUnits('COMPSCI 150')
        self.assertEquals(5, units)


