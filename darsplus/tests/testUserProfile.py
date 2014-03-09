"""
Test suite for UserProfile database in models.py
Tests all methods defined in the class, but not the wrapper methods
Assumes that ID increments from 0

To run, type "python manage.py test darsplus.tests.testUserProfile"
"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import UserProfile

class TestUserProfile(TestCase):
        
    def testAddSimple(self):
        """
        Tests that you can add 1 user
        """
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", "2014")
        self.assertEquals(SUCCESS, response)        
        self.assertEquals(1, UserProfile.objects.all().count())

    def testFields(self):
        """
        Tests that fields are stored correctly
        """
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", 2014)
        user = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals("eevee", user.username)
        self.assertEquals("Computer Science", user.major)
        self.assertEquals("Fall", user.graduationSemester)
        self.assertEquals(2014, user.graduationYear)

    def testAddDuplicateUser(self):
        """
        Tests that you cannot add two users with the same username
        """
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                              "Fall", 2014)
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                              "Fall", 2014)
        self.assertEquals(ERR_USER_EXISTS, response)        
        self.assertEquals(1, UserProfile.objects.count())
    
    def testAddMultipleUsers(self):
        """
        Tests that you can add an arbitary number of users
        """
        for i in range(1,10):
            response = UserProfile.addUserProfile("John Smith "+str(i), "Computer Science", "Fall", 2014)
            self.assertEquals(SUCCESS, response)
            self.assertEquals(i, UserProfile.objects.count())
    
    def testAddCaseSensitive(self):
        """
        Tests that adding username is case sensitive
        """
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", 2014)
        self.assertEquals(SUCCESS, response)
        self.assertEquals(1, UserProfile.objects.count())

        response = UserProfile.addUserProfile("Eevee","Computer Science",
                                                     "Fall", 2014)
        self.assertEquals(SUCCESS, response)
        self.assertEquals(2, UserProfile.objects.count())


    def testEmptyCoursesTaken(self):
        """
        Tests that course taken defaults to [] (empty)
        """
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", 2014)
        self.assertEquals([], UserProfile.getCoursesTaken("eevee"))

    def testAddCourseTaken(self):
        response = UserProfile.addUserProfile("eevee", "Computer Science",
                                              "Fall", 2014)
        self.assertEquals([], UserProfile.getCoursesTaken("eevee"))
        

    def testNoUnitsCompleted(self):
        """
        Tests that unitsCompleted deftaults to 0
        """
        response = UserProfile.addUserProfile("eevee","Computer Science",
                                                     "Fall", 2014)
        user = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals(0, user.unitsCompleted)

    def testUniquePlannerID(self):
        """
        Tests that IDS are unique (for an arbitary number of userProfile registration
        """
        IDs = []
        for i in range(1,10):
            username = "John Smith " + str(i)
            response = UserProfile.addUserProfile(username, "Computer Science", "Fall", 2014)
            user = UserProfile.objects.filter(username=username)[0]
            id = user.plannerID
            self.assertEquals(True, id not in IDs)
            IDs += [id]

    def testIncrementPlannerID(self):
        """
        This test may not be valid anymore if we change how we represent,
        and increment our plannerID
        
        May also need to convert Strings to Integers
        """
        for i in range(0,10):
            username = "John Smith " + str(i)
            response = UserProfile.addUserProfile(username, "Computer Science", "Fall", 2014)
            user = UserProfile.objects.filter(username=username)[0]
            id = user.plannerID
            self.assertEquals(i, id)

