from django.db import models
from djorm_pgarray.fields import ArrayField #Postgres package that enables ArrayField
from utils import * 

# Create your models here.
class DBName(models.Model):
    pass

class UserLoginInformation(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)

    @static
    def addUser(self, user, email, password):
        """
        This functions check that user does not exists, the username is not empty, the e-mail is valid

        * On success returns SUCCESS and adds entry to the appropriate Database
        * On failure, the result is an error code (< 0) from the list: [ERR_USER_EXISTS, ERR_EMAIL_EXISTS, ERR_BAD_USERNAME, ERR_BAD_PASSWORD, ERR_BAD_EMAIL]
        """
        pass
    
    @static
    def login(self, user, password):
        pass

    @static
    def logout(self, user):



class UserProfile(models.Model):
    username = models.CharField(max_length=256)
    major = models.CharField(max_length=128)
    graduationSemester = models.CharField(max_length=8)
    graduationYear = models.IntegerField()
    coursesTaken = ArrayField(dbtype="varchar(255)")
    plannerID = models.IntegerField()
    unitsCompleted = models.IntegerField()

    @static
    def addUserProfile(self, username, major, graduationSemester, graduationYear,coursesTaken, unitsCompleted):
        """
        """
        pass

    @static
    def addCourseTaken(self, username, coursename):
        """
        Change units completed appropriately
        """
        pass    

    @static
    def removeCourseTaken(self, username, coursename):
        """
        Change units completed appropriately
        """
        pass
    
    @static
    def changeGraduationSemester(self, username, semester):
        pass

    @static
    def changeGraduationYear(self, username, year):
        pass

    @static
    def changeMajor(self, username, newMajor):
        pass


class Planner(models.Model):
    plannerID = models.IntegerField()
    semester1 = ArrayField(dbtype="varchar(255)")
    semester2 = ArrayField(dbtype="varchar(255)")
    semester3 = ArrayField(dbtype="varchar(255)")
    semester4 = ArrayField(dbtype="varchar(255)")
    semester5 = ArrayField(dbtype="varchar(255)")
    semester6 = ArrayField(dbtype="varchar(255)")
    semester7 = ArrayField(dbtype="varchar(255)")
    semester8 = ArrayField(dbtype="varchar(255)")
    semester9 = ArrayField(dbtype="varchar(255)")
    semester10 = ArrayField(dbtype="varchar(255)")
    semester11 = ArrayField(dbtype="varchar(255)")
    semester12 = ArrayField(dbtype="varchar(255)")
    semester13 = ArrayField(dbtype="varchar(255)")
    semester14 = ArrayField(dbtype="varchar(255)")
    semester15 = ArrayField(dbtype="varchar(255)")

    @static
    def addPlanner(self):
        """
        Initializes a new planner
        """
        pass

    @static
    def addCourseToPlanner(self, plannerID, index, coursename):
        pass

    @static
    def removeCourseFromPlanner(self, plannerID, index, coursename):
        pass

    @static
    def totalUnitsPlanner(self, plannerID, index):
        pass


class Courses(models.Model):
    courseCode = models.IntegerField()
    courseName = models.CharField(max_length=128)
    courseDescription = models.CharField(max_length=128)
    courseLevel = models.CharField(max_length=32)
    minUnit = models.IntegerField()
    maxUnit = models.IntegerField()
    department = models.CharField(max_length=128)

    @static
    def getCourseUnits(self, courseName):
        pass


class Colleges(models.Model):
    major = models.CharField(max_length=128)
    college = models.CharField(max_length=128)

    @static
    def majorToCollege(self, major):
        pass

"""
The functions below are wrappers for the functions above so that others don't need to refer to the Databases directly
"""

def addUser(user, email, password):
    return UserLoginInformation.add(user, email, password)

def login(user, password):
    return UserLoginInformation.login(user, password)

def logout(user):
    return UserLoginInformation.logout(user)

def addUserProfile(username, major, graduationSemester, graduationYear,coursesTaken, unitsCompleted):
    return UserProfile.addUserProfile(username, major, graduationSemester, graduationYear,coursesTaken, unitsCompleted)

def changeGraduationSemester(username, semester):
    return UserProfile.changeGraduationSemester(self, username, semester)

def changeGraduationYear(username, year):
    return UserProfile.changeGraduationYear(username, year)

def changeMajor(username, newMajor):
    return UserProfile.changeMajor(username, newMajor)

def addCourseTaken(username, coursename):
    return UserProfile.addCoursesTaken(username, coursename)

def addListCoursesTaken(username, courseList):
    pass

def removeCourseTaken(username, coursename):
    return UserProfile.removeCourseTaken(username, coursename)

def removeListCoursesTaken(username, coursename):
    pass

def addCourseToPlanner(plannerID, index, coursename):
    return Planner.addCourseToPlanner(plannerID, index, coursename)

def removeCourseFromPlanner(plannerID, index, coursename):
    return Planner.removeCourseFromPlanner(plannerID, index, coursename)

def totalUnitsPlanner(plannerID, index):
    return Planner.totalUnitsPlanner(plannerID, index)

def getCourseUnits(courseName):
    return Courses.getCourseUnits(courseName)

def majorToCollege(major):
    return Colleges.majorToCollege(major)


