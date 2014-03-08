"""
Test suite for UserProfile database in models.py
Tests all methods defined in the class, but not the wrapper methods

To run, type "python manage.py test thinkahead/thinkahead/tests"
"""

from django.test import TestCase
from thinkahead.thinkahead.models import UserProfile
from thinkahead.thinkahead.utils import *

class TestAddUserProfile(TestCase):
    def testAddSimple(self):
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", "2014")
        self.assertEquals(SUCCESS, response)
        """
        self.assertEquals(1, UserProfile.objects.all().count())
        """
    """
    def testFields(self):
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", "2014")
        user = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals("eevee", user.username)
        self.assertEquals("Computer Science", user.major)
        self.assertEquals("Fall", user.graduationSemester)
        self.assertEquals("2014", user.graduationYear)

    def testAddDuplicateUser(self):
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                              "Fall", "2014")
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                              "Fall", "2014")
        self.assertEquals(ERR_USER_EXISTS, response)        
        self.assertEquals(1, UserProfile.objects.count())
    
    def testAddMultipleUsers(self):
        for i in range(1,10):
            response = UserProfile.addUserProfile("John Smith "+str(i), "Computer Science", "Fall", "2014")
            self.assertEquals(SUCCESS, response)
            self.assertEquals(i, UserProfile.objects.count())
    
    def testAddCaseSensitive(self):
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", "2014")
        self.assertEquals(SUCCESS, response)
        self.assertEquals(1, UserProfile.objects.count())

        response = UserProfile.addUserProfile("Eevee","Computer Science",
                                                     "Fall", "2014")
        self.assertEquals(SUCCESS, response)
        self.assertEquals(2, UserProfile.objects.count())

    def testCoursesTaken(self):
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", "2014")
        user = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals([], user.coursesTaken)

    def testUnitsCompleted(self):
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", "2014")
        user = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals(0, user.unitsCompleted)

    def testUniquePlannerID(self):
        IDs = []
        for i in range(1,10):
            username = "John Smith " + str(i)
            response = UserProfile.addUserProfile(username, "Computer Science", "Fall", "2014")
            user = UserProfile.objects.filter(username=username)[0]
            id = user.plannerID
            self.assertEquals(True, id not in IDs)
            IDs += [id]

    def testIncrementPlannerID(self):
        #This test may not be valid anymore if we change how we represent,
        #and increment our plannerID
        
        #May also need to convert Strings to Integers
        for i in range(0,10):
            username = "John Smith " + str(i)
            response = UserProfile.addUserProfile(username, "Computer Science", "Fall", "2014")
            user = UserProfile.objects.filter(username=username)[0]
            id = user.plannerID
            self.assertEquals(i, id)
    """
