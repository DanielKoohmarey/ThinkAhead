from django.db import models
from djorm_pgarray.fields import ArrayField #Postgres package that enables ArrayField


# Create your models here.
class DBName(models.Model):
    pass

class UserLoginInformation(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)

class UserProfile(models.Model):
    username = models.CharField(max_length=256)
    major = models.CharField(max_length=128)
    graduationSemester = models.CharField(max_length=8)
    graduationYear = models.IntegerField()
    coursesTaken = ArrayField(dbtype="varchar(255)")
    plannerID = models.IntegerField()
    unitsCompleted = models.IntegerField()
    
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

class Courses(models.Model):
    courseCode = models.IntegerField()
    courseName = models.CharField(max_length=128)
    courseDescription = models.CharField(max_length=128)
    courseLevel = models.CharField(max_length=32)
    minUnit = models.IntegerField()
    maxUnit = models.IntegerField()
    department = models.CharField(max_length=128)

class Colleges(models.Model):
    major = models.CharField(max_length=128)
    college = models.CharField(max_length=128)
