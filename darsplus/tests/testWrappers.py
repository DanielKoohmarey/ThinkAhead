"""
Test suite for wrapper functions in models.py
Currently does not test majorToCollege due to no loadCollege defined

To run, type "python manage.py test darsplus.tests.testWrapper"
"""

from django.test import TestCase
from darsplus.models import *
from darsplus.utils import *

class TestCourses(TestCase):

    def setUp(self):
        response = Courses.loadCourses()
        self.assertEquals(SUCCESS, response)
        response = addUserProfile('magikarp', 'EECS', SUMMER_SEMESTER, 2017)
        self.assertEquals(SUCCESS, response)
        numAccounts = UserProfile.objects.all().count()
        self.assertEquals(1, numAccounts)

    def testAddUserProfileWrapper(self):
        response = addUserProfile('eevee', 'COMPSCI', FALL_SEMESTER, 2015)
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='eevee')[0]
        self.assertEquals('eevee', account.username)
        self.assertEquals('COMPSCI', account.major)
        self.assertEquals(FALL_SEMESTER, account.graduationSemester)
        self.assertEquals(2015, account.graduationYear)

    def testChangeGraduationSemesterWrapper(self):
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = changeGraduationSemester('magikarp', SPRING_SEMESTER)
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertEquals(SPRING_SEMESTER, account.graduationSemester)

    def testChangeGraduationYearWrapper(self):
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = changeGraduationYear('magikarp', 2013)
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertEquals(2013, account.graduationYear)

    def testChangeMajorWrapper(self):
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = changeMajor('magikarp', 'Economics')
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertEquals('Economics', account.major)

    def testGetCoursesTakenWrapper(self):
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = getCoursesTaken('magikarp')
        self.assertEquals([], response)

    def testGetUnitsCompletedWrapper(self):
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = getUnitsCompleted('magikarp')
        self.assertEquals(0, response)

    def testAddCourseTakenWrapper(self):
        response = addCourseTaken('magikarp', 'COMPSCI 169')
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertIn('COMPSCI 169', account.coursesTaken)
        self.assertEquals(4, account.unitsCompleted)

    def testAddListCoursesTaken(self):
        courseList = ['COMPSCI 169', 'COMPSCI 160', 'COMPSCI 61A']
        response = addListCoursesTaken('magikarp', courseList)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertEquals(3, len(account.coursesTaken))
        for course in courseList:
            self.assertIn(course, account.coursesTaken)
        self.assertEquals(12, account.unitsCompleted)

    def testRemoveCourseTakenWrapper(self):
        response = addCourseTaken('magikarp', 'COMPSCI 169')
        account = UserProfile.objects.filter(username='magikarp')[0]
        response = removeCourseTaken('magikarp', 'COMPSCI 169')
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertNotIn('COMPSCI 169', account.coursesTaken)
        self.assertEquals(0, account.unitsCompleted)

    def testRemoveListCoursesTaken(self):
        courseList = ['COMPSCI 169', 'COMPSCI 160', 'COMPSCI 61A']
        subList = ['COMPSCI 169', 'COMPSCI 160']
        response = addListCoursesTaken('magikarp', courseList)
        response = removeListCoursesTaken('magikarp', subList)
        account = UserProfile.objects.filter(username='magikarp')[0]
        self.assertIn('COMPSCI 61A', account.coursesTaken)
        self.assertNotIn('COMPSCI 169', account.coursesTaken)
        self.assertNotIn('COMPSCI 160', account.coursesTaken)
        self.assertEquals(4, account.unitsCompleted)

    def testPlannerWrapper(self):
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

    def testGetCourseUnits(self):
        units = getCourseUnits('COMPSCI 169')
        self.assertEquals(4, units)
        units = getCourseUnits('COMPSCI 150')
        self.assertEquals(5, units)


