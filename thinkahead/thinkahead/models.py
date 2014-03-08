"""
Classes to represent Databases for our application

The "class Meta" clause under each classes allow us to move this python file anywhere and let Django knows that it is part of the application. Do NOT remove this
"""
from django.db import models
from djorm_pgarray.fields import ArrayField #Postgres package that enables ArrayField
from utils import * 

# Create your models here.

class UserLoginInformation(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)
    class Meta:
        app_label = 'thinkahead'
    
    @staticmethod
    def addUser(username, email, password):
        """
        This functions check that user does not exists, the username is not empty, the e-mail is valid

        * On success returns SUCCESS and adds entry to the appropriate Database
        * On failure, the result is an error code (< 0) from the list: 
        [ERR_USER_EXISTS, ERR_EMAIL_EXISTS, ERR_BAD_USERNAME, ERR_BAD_PASSWORD, ERR_BAD_EMAIL]
        """
        if not validUsername(username):
            return ERR_BAD_USERNAME
        if not validPassword(password):
            return ERR_BAD_PASSWORD
        if not validEMail(email):
            return ERR_BAD_EMAIL
        if userExists(username):
            return ERR_USER_EXISTS
        if emailExists(email):
            return ERR_EMAIL_EXISTS


        newUser = UserLoginInformation(username=username,email=email, password=password)
        newUser.save()
        return SUCCESS
    
    @staticmethod
    def login(user, password):
        pass

    @staticmethod
    def logout(user):
        pass


class UserProfile(models.Model):
    username = models.CharField(max_length=256)
    major = models.CharField(max_length=128)
    graduationSemester = models.CharField(max_length=8)
    graduationYear = models.IntegerField()
    coursesTaken = ArrayField(dbtype="varchar(255)")
    plannerID = models.IntegerField()
    unitsCompleted = models.IntegerField()
    class Meta:
        app_label = 'thinkahead'

    @staticmethod
    def addUserProfile(username, major, graduationSemester, graduationYear):
        """
        Checks if a username does not exist

        * On success return SUCCESS with the corresponding fields filled in the DB.
        coursesTaken and unitsCompleted default to [] and 0 respectively
        creates a planner that corresponds with this user
        * If username already exists, return ERR_USER_EXISTS
        """
        if userExists(username):
            return ERR_USER_EXISTS
        plannerID = Planner.addPlanner()
        newUser = UserProfile(username=username, major=major, graduationSemester=graduationSemester, 
                              graduationYear=graduationYear, coursesTaken=[], plannerID=plannerID, unitsCompleted=0)
        newUser.save()
        return SUCCESS

    @staticmethod
    def addCourseTaken(username, coursename):
        """
        Adds corresponding course into list of courses taken by user. If course already in list, nothing happens
        Change units completed appropriately

        * return SUCCESS
        * If username is not registered, return ERR_NO_RECORD_FOUND
        """
        matches = UserPofile.objects.filter(username=username)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        if coursename not in account.coursesTaken: 
            account.coursesTaken = account.coursesTaken + [coursename]
            account.unitsCompleted += getCourseUnits(coursename)
            account.save()
        return SUCCESS

    @staticmethod
    def removeCourseTaken(username, coursename):
        """
        Removes corresponding course from list of courses taken by user. If course is not in list, nothing happens
        Change units completed appropriately

        * If successful, return SUCCESS 
        * If username is not registered, return ERR_NO_RECORD_FOUND
        """
        matches = UserProfile.objects.filter(username=username)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        if coursename in account.coursesTaken: 
            account.coursesTaken.remove(coursename)
            account.unitsCompleted -= getCourseUnits(coursename)
            account.save()
        return SUCCESS
    
    @staticmethod
    def changeGraduationSemester(username, semester):
        """
        Changes the entry for graduation semester of the corresponding username
        semester should be either [SPRING_SEMESTER,SUMMER_SEMESTER,FALL_SEMESTER]
        
        * If successful, return SUCCESS
        * If username is not registered, return ERR_NO_RECORD_FOUND
        """
        matches = UserProfile.objects.filter(username=username)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        account.graduationSemester = semester
        account.save()
        return SUCCESS


    @staticmethod
    def changeGraduationYear(username, year):
        """
        Changes the entry for graduation year of the corresponding username
        
        * If successful, return SUCCESS
        * If username is not registered, return ERR_NO_RECORD_FOUND
        """
        matches = UserProfile.objects.filter(username=username)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        account.graduationYear = year
        account.save()
        return SUCCESS

    @staticmethod
    def changeMajor(username, newMajor):
        """
        Changes the entry for major  of the corresponding username
        
        * If successful, return SUCCESS
        * If username is not registered, return ERR_NO_RECORD_FOUND
        """
        matches = UserProfile.objects.filter(username=username)
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        account.major = newMajor
        account.save()
        return SUCCESS
        

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
    class Meta:
        app_label = 'thinkahead'

    @staticmethod
    def addPlanner():
        """
        Initializes a new planner and add it to the database.
        plannerID is determined by how many elements are there in the database upon creation
        
        * Returns the ID of the new planner
        * Initializes all semesters' list of courses to []
        """
        count = Planner.objects.all().count()
        planner = Planner(plannerID=count, semester1=[], semester2=[], semester3=[],
                          semester4=[], semester5=[], semester6=[],
                          semester7=[], semester8=[], semester9=[],
                          semester10=[], semester11=[], semester12=[],
                          semester13=[], semester14=[], semester15=[])
        planner.save()
        return count

    @staticmethod
    def addCourseToPlanner(plannerID, index, coursename):
        """
        Adds a new course to the planner's index-th semester. 
        index should be between 1 and 15 inclusive.
        If the course already is in the list, no change
        
        * Return SUCCESS if successfully added
        * If plannerID does not exist, return ERR_NO_RECORD_FOUND
        """
        matches = Planner.objects.filter(plannerID=plannerID)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        semester = 'semester'+str(index)
        courseList = getattr(account, semester) # Gets the list of courses for corresponding semester
        if coursename not in courseList:
            setattr(account, semester, courseList + [coursename])
        return SUCCESS           
        

    @staticmethod
    def removeCourseFromPlanner(plannerID, index, coursename):
        """
        Adds a new course to the planner's index-th semester. 
        index should be between 1 and 15 inclusive.
        If the course already is not in the list, no change
        
        * Return SUCCESS if successfully added
        * If plannerID does not exist, return ERR_NO_RECORD_FOUND
        """
        matches = Planner.objects.filter(plannerID=plannerID)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        semester = 'semester'+str(index)
        courseList = getattr(account, semester) # Gets the list of courses for corresponding semester
        if coursename in courseList:
            courseList.remove(coursename)
        return SUCCESS           

    @staticmethod
    def totalUnitsPlanner(plannerID, index):
        """
        Calculates total number of points in a given semester
        index should be between 1 and 15 inclusive

        * Return total number of units in the semester
        * If plannerID does not exist, return ERR_NO_RECORD_FOUND
        """
        matches = Planner.objects.filter(plannerID=plannerID)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        semester = 'semester'+str(index)
        courseList = getattr(account, semester)

        unitCount = 0
        for i in range(0, len(courseList)):
            unitCount += getCourseUnits(courseList[i])
        return unitCount

class Courses(models.Model):
    courseCode = models.IntegerField()
    courseName = models.CharField(max_length=128)
    courseDescription = models.CharField(max_length=128)
    courseLevel = models.CharField(max_length=32)
    minUnit = models.IntegerField()
    maxUnit = models.IntegerField()
    department = models.CharField(max_length=128)
    class Meta:
        app_label = 'thinkahead'


    @staticmethod
    def getCourseUnits(courseName):
        """
        * Return number of units for a given course
        If it is a variable unit course, tentatively return maxUnit
        """
        matches = Courses.objects.filter(courseName=courseName)
        course = matches[0]
        return course.maxUnit
    
    @staticmethod
    def loadCourses():
        """ Run this once to populate the database with Courses """
        import pickle
        departments  = pickle.load( open("courses.p", "rb") )
        for department in courses.keys():
            for course in department.keys():
                courseInfo = department[course]
                units = units.split(" - ")
                if len(units) == 1:
                    units = units[0],units[0]
                newCourse = Course(courseCode = course, CourseName = courseInfo[0], courseDescription = courseInfo[4], courseLevel = courseInfo[3], minUnit = units[0], maxUnit = units[1], department = department)
                newCourse.save()  


class Colleges(models.Model):
    major = models.CharField(max_length=128)
    college = models.CharField(max_length=128)
    class Meta:
        app_label = 'thinkahead'

    @staticmethod
    def majorToCollege(major):
        """
        * Return college of the corresponding major
        """
        matches = Colleges.objects.filter(major=major)
        college = matches[0]
        return college
"""
The functions below are wrappers for the functions above so that others don't need to refer to the Databases directly
"""

def addUser(user, email, password):
    return UserLoginInformation.add(user, email, password)

def login(user, password):
    return UserLoginInformation.login(user, password)

def logout(user):
    return UserLoginInformation.logout(user)

def addUserProfile(username, major, graduationSemester, graduationYear):
    return UserProfile.addUserProfile(username, major, graduationSemester, graduationYear)

def changeGraduationSemester(username, semester):
    return UserProfile.changeGraduationSemester(self, username, semester)

def changeGraduationYear(username, year):
    return UserProfile.changeGraduationYear(username, year)

def changeMajor(username, newMajor):
    return UserProfile.changeMajor(username, newMajor)

def addCourseTaken(username, coursename):
    return UserProfile.addCoursesTaken(username, coursename)

def addListCoursesTaken(username, courseList):
    """
    Adds every course in courseList to list of user's courses taken
    """
    for i in range(0, len(courseList)):
        addCourseTaken(username, courseList[i])

def removeCourseTaken(username, coursename):
    return UserProfile.removeCourseTaken(username, coursename)

def removeListCoursesTaken(username, coursename):
    """
    Remove every course in courseList to list of user's courses taken
    """
    for i in range(0, len(courseList)):
        removeCourseTaken(username, courseList[i])

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


