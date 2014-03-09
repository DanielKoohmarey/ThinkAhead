"""
Test suite for UserProfile database in models.py
Tests all methods defined in the class, but not the wrapper methods
Assumes that ID increments from 0

To run, type "python manage.py test darsplus.tests.testUserProfile"
"""

from django.test import TestCase
from darsplus.utils import * 
from darsplus.models import UserProfile
from darsplus.models import Courses

class TestUserProfile(TestCase):
    """
    def setUp(self):
        response = Courses.loadCourses()
        self.assertEquals(SUCCESS, response)
    """
 
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


    """
    def testAddCourseTaken(self):
    
        response = UserProfile.addUserProfile("eevee", "Computer Science",
                                              "Fall", 2014)
        account = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals([], UserProfile.getCoursesTaken("eevee"))
        response = UserProfile.addCourseTaken("eevee", "COMPSCI 169")
        self.assertEquals(SUCCESS, response)
        self.assertEquals(['COMPSCI 169'], UserProfile.getCoursesTaken("eevee"))
        self.assertEquals(4, account.unitsCompleted)

        #Should not be able to add the same course twice
        response = UserProfile.addCourseTaken("eevee", "COMPSCI 169")
        self.assertEquals(ERR_RECORD_EXISTS, response)
        self.assertEquals(['COMPSCI 169'], UserProfile.getCoursesTaken("eevee"))
        self.assertEquals(4, account.unitsCompleted)
        
        #Should still be able to add other courses
        response = UserProfile.addCourseTaken("eevee", "COMPSCI 161")
        self.assertEquals(8, account.unitsCompleted)
        self.assertEquals(['COMPSCI 169', 'COMPSCI 161'], account.coursesTaken)

    def testRemoveCourseTaken(username, coursename):
        response = UserProfile.addUserProfile("eevee", "Computer Science",
                                              "Fall", 2014)
        account = UserProfile.objects.filter(username="eevee")[0]
        response = UserProfile.addCourseTaken("eevee", "COMPSCI 169")
        response = UserProfile.addCourseTaken("eevee", "COMPSCI 161")
        self.assertEquals(8, account.unitsCompleted)
        self.assertEquals(['COMPSCI 169', 'COMPSCI 161'], account.coursesTaken)
        # Can remove a course if it exists, updating unitsCompleted
        response = UserProfile.removeCourseTaken('eevee', 'COMPSCI 161')
        self.assertEquals(SUCCESS, response)
        self.assertEquals(['COMPSCI 169'], account.coursesTaken)
        self.assertEquals(4, account.unitsCompleted)

        # Returns an error if the course does not exist in the list
        response = UserProfile.removeCourseTaken('eevee', 'COMPSCI 161')
        self.assertEquals(ERR_NO_RECORD_FOUND, response)
        self.assertEquals(['COMPSCI 169'], account.coursesTaken)
        self.assertEquals(4, account.unitsCompleted)       
        
        
        
    """
    def testChangeGraduationSemester(self):
        response = UserProfile.addUserProfile("eevee", "Computer Science",
                                              "Fall", 2014)
        account = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals("Fall", account.graduationSemester)
        response = UserProfile.changeGraduationSemester('eevee', 'Spring')
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals('Spring', account.graduationSemester)       

    def testChangeGraduationYear(self):
        response = UserProfile.addUserProfile("eevee", "Computer Science",
                                              "Fall", 2014)
        account = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals(2014, account.graduationYear)
        response = UserProfile.changeGraduationYear('eevee', 2015)
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals(2015, account.graduationYear)       

    def testChangeMajor(self):
        response = UserProfile.addUserProfile("eevee", "Computer Science",
                                              "Fall", 2014)
        account = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals(2014, account.graduationYear)
        response = UserProfile.changeMajor('eevee', 'Economics')
        self.assertEquals(SUCCESS, response)
        account = UserProfile.objects.filter(username="eevee")[0]
        self.assertEquals('Economics', account.major)       

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

