"""
Classes to represent Databases for our application

"""
from django.db import models
from djorm_pgarray.fields import ArrayField #Postgres package that enables ArrayField
# http://www.craigkerstiens.com/2012/11/06/django-and-arrays/ for reference 
from utils import * 
from statics import * 

# Create your models here

class UserProfile(models.Model):
    username = models.CharField(max_length=256)
    major = models.CharField(max_length=128)
    graduationSemester = models.CharField(max_length=8)
    graduationYear = models.IntegerField()
    coursesTaken = ArrayField(dbtype="varchar(255)")
    plannerID = models.IntegerField()
    unitsCompleted = models.FloatField()

    @staticmethod
    def getUserProfile(username):
        """
        Checks if user already exists in UserLoginInformation DB. Is case sensitive

        @param userame is a string
        @return UserProfile
        """
        try:
            profile = UserProfile.objects.get(username=username)
            return profile
        except UserProfile.DoesNotExist:
            return None

    @staticmethod
    def addUserProfile(username, major, graduationSemester, graduationYear, coursesTaken):
        """
        Checks if a username does not exist

        * On success return SUCCESS with the corresponding fields filled in the DB.
        coursesTaken and unitsCompleted default to [] and 0 respectively
        creates a planner that corresponds with this user
        * If username already exists, return ERR_USER_EXISTS
        """
        if getUserProfile(username):
            return ERR_USER_EXISTS
        plannerID = Planner.addPlanner()
        newUser = UserProfile(username=username, major=major, graduationSemester=graduationSemester, 
                              graduationYear=graduationYear, coursesTaken=coursesTaken, plannerID=plannerID, unitsCompleted=0)
        newUser.save()
        return SUCCESS

    @staticmethod
    def getCoursesTaken(username):
        """
        returns list of courses (as strings) of courses already taken by username
        if username does not exist, return ERR_NO_RECORD_FOUND
        """
        matches = UserProfile.objects.filter(username=username)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        return account.coursesTaken
        
    @staticmethod
    def getUnitsCompleted(username):
        """
        return number of units taken by username
        * If username does not exist, return ERR_NO_RECORD_FOUND
        """
        matches = UserProfile.objects.filter(username=username)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        return account.unitsCompleted

    @staticmethod
    def addCourseTaken(username, coursename):
        """
        Adds corresponding course into list of courses taken by user. 
        Change units completed appropriately

        * return SUCCESS
        * If username is not registered, return ERR_NO_RECORD_FOUND
        * If course already in list, return ERR_RECORD_EXISTS
        """
        matches = UserProfile.objects.filter(username=username)
        numMatches = matches.count()
        if numMatches == 0:
            return ERR_NO_RECORD_FOUND
        account = matches[0]
        if coursename not in account.coursesTaken: 
            account.coursesTaken = account.coursesTaken + [coursename]
            account.unitsCompleted += getCourseUnits(coursename)
            account.save()
        else:
            return ERR_RECORD_EXISTS
        return SUCCESS

    @staticmethod
    def removeCourseTaken(username, coursename):
        """
        Removes corresponding course from list of courses taken by user. 
        Change units completed appropriately

        * If successful, return SUCCESS 
        * If username is not registered, return ERR_NO_RECORD_FOUND
        * If course is not in list, return ERR_NO_RECORD_FOUND
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
        else:
            return ERR_NO_RECORD_FOUND
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
        numMatches = matches.count()
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
        
        * Return SUCCESS if successfully added
        * If plannerID does not exist, return ERR_NO_RECORD_FOUND
        * If the course already is in the list, return ERR_RECORD_EXISTS

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
            account.save()
        else:
            return ERR_RECORD_EXISTS
        return SUCCESS           
        

    @staticmethod
    def removeCourseFromPlanner(plannerID, index, coursename):
        """
        Adds a new course to the planner's index-th semester. 
        index should be between 1 and 15 inclusive.
        
        * Return SUCCESS if successfully added
        * If plannerID does not exist, return ERR_NO_RECORD_FOUND
        * If the course already is not in the list, return ERR_NO_RECORD_FOUND

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
            account.save()
        else:
            return ERR_NO_RECORD_FOUND
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
        unitCount = 0.0
        for i in range(0, len(courseList)):
            units = float(Courses.getCourseUnits(courseList[i]))
            unitCount =  unitCount + units
        return unitCount


class Courses(models.Model):
    courseCode = models.CharField(max_length=64)
    courseName = models.CharField(max_length=256)
    courseDescription = models.CharField(max_length=128)
    courseLevel = models.CharField(max_length=64)
    minUnit = models.FloatField()
    maxUnit = models.FloatField()
    department = models.CharField(max_length=128)

    @staticmethod
    def getCourseInfo(courseCode):
        matches = Courses.objects.filter(courseCode=courseCode)
        course = matches[0]
        return course


    @staticmethod
    def getCourseUnits(courseCode):
        """
        * Return number of units for a given course
        * If it is a variable unit course, tentatively return maxUnit
        * If record is not found, return ERR_NO_RECORD_FOUND
        """
        matches = Courses.objects.filter(courseCode=courseCode)
        if (matches.count() == 0):
            return ERR_NO_RECORD_FOUND
        course = matches[0]
        return course.maxUnit
    '''
    #No longer need this method if using fixtures, keeping temporarily incase fixtures error
    @staticmethod
    def loadCourses():
        """ Run this once to populate the database with Courses """
        import pickle
        departments = pickle.load( open("courses.p", "rb") )
        for department in departments.keys():
            for course in departments[department].keys():
                courseInfo = departments[department][course]
                units = courseInfo[1]
                if 'or' in units: # Some specified their units as '3 or 4'
                    units = units.split( " or ")
                else:
                    units = units.split(" - ")

                if len(units) == 1:
                    units = units[0],units[0]
                #units = [int(unit) for unit in units] # There are courses with .5 units. I changed the field corresponding to units to Decimals
                courses = course.split("/") # Some are in "HISTART C196W/HISTORY C196W/MEDIAST C196W/"
                for similarCourse in courses:
                    newCourse = Courses(courseCode = similarCourse, courseName = courseInfo[0],
                                        courseDescription = courseInfo[4], courseLevel = courseInfo[3],
                                        minUnit = units[0], maxUnit = units[1], department = department)
                    newCourse.save()
        return SUCCESS
    '''
class Colleges(models.Model):
    major = models.CharField(max_length=128)
    college = models.CharField(max_length=128)
       

    @staticmethod
    def majorToCollege(major):
        """
        * Return college(s) of the corresponding major (in String)
        * If major does not exist, return ERR_RECORD_NOT_FOUND        
        """
        matches = Colleges.objects.filter(major=major)
        numMatches = matches.count()
        if (numMatches == 0):
            return ERR_NO_RECORD_FOUND
        elif (numMatches == 1):
            college = matches[0]
            return college.college
        else:
            return map(lambda major: major.college, matches)
 
    @staticmethod
    def allColleges():
        """
        Returns a list of all unique college names
        """
        matches = Colleges.objects.distinct('college')
        return [match.college for match in matches]
 
    @staticmethod
    def getMajorsInCollege(college):
        """
        Returns a list of majors (in strings) that are inside college
        """
        matches = Colleges.objects.filter(college=college)
        majorList = map(lambda match: match.major, matches)
        return majorList



"""
The functions below are wrappers for the functions above so that others don't need to refer to the Databases directly
"""

def emailExists(email):
    """
    Checks if an email is already registered under another user

    @param email is a string
    @return Boolean
    """
    matches = UserLoginInformation.objects.filter(email=email)
    numMatches = matches.count()
    if numMatches > 0:
        return True
    else:
        return False

"""
def addUser(user, email, password):
    return UserLoginInformation.add(user, email, password)

def login(user, password):
    return UserLoginInformation.login(user, password)

def logout(user):
    return UserLoginInformation.logout(user)
"""
def addUserProfile(username, major, graduationSemester, graduationYear, coursesTaken):
    return UserProfile.addUserProfile(username, major, graduationSemester, graduationYear, coursesTaken)

def getUserProfile(username):
    return UserProfile.getUserProfile(username)

def changeGraduationSemester(username, semester):
    return UserProfile.changeGraduationSemester(username, semester)

def changeGraduationYear(username, year):
    return UserProfile.changeGraduationYear(username, year)

def changeMajor(username, newMajor):
    return UserProfile.changeMajor(username, newMajor)

def getCoursesTaken(username):
    return UserProfile.getCoursesTaken(username)

def getUnitsCompleted(username):
    return UserProfile.getUnitsCompleted(username)

def addCourseTaken(username, coursename):
    return UserProfile.addCourseTaken(username, coursename)

def addListCoursesTaken(username, courseList):
    """
    Adds every course in courseList to list of user's courses taken
    """
    for i in range(0, len(courseList)):
        response = addCourseTaken(username, courseList[i])
        if response != SUCCESS:
            return response
    return SUCCESS

def removeCourseTaken(username, coursename):
    return UserProfile.removeCourseTaken(username, coursename)

def removeListCoursesTaken(username, courseList):
    """
    Remove every course in courseList to list of user's courses taken
    """
    for i in range(0, len(courseList)):
        response = removeCourseTaken(username, courseList[i])
        if response != SUCCESS:
            return response
    return SUCCESS

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


def getCollegesToMajors():
    """
    Returns a dictionary with a key college name, and value list of majors

    Example Output (shortened):
    {
		"Engineering College": ["EECS", "MechE"],
		"L&S": ["CS", "English"],
     }
    """
    colleges = Colleges.allColleges()
    output = {}
    for college in colleges:
        output[college] = Colleges.getMajorsInCollege(college)
    return output
