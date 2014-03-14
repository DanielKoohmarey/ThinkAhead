from django.shortcuts import render
from darsplus.statics import SUCCESS
from darsplus.forms import LoginForm, GradForm, MajorForm, CourseFormSet
from darsplus.models import addUserProfile, getUserProfile, getCoursesTaken, getUnitsCompleted, majorToCollege
from darsplus.requirementscode import remainingRequirements
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json

collegeToMajors = {'Engineering': ['EECS','BIOENG','CIVENG', 'COENG', 'ENENG', 'ENGMS', 'ENGP', 'MATSCI','NUCENG','EECSMATSCI', 'EECSNUCENG', 'MATMECENG', 'MATNUCENG', 'MECNUCENG']} #TODO: College database needs to be populated, perhaps convert names to these abreviations
majorJSON = json.dumps(collegeToMajors) 
def splash(request):
    """ Load the splashpage, or appropriate page depending on user status """
    dashboardContext = dashboardData(request)
    if dashboardContext:
        return render(request, 'dashboard.html', RequestContext(request,dashboardContext)) 
    elif request.user.is_anonymous():
        return render(request, 'splash.html', {'form':LoginForm()})
    elif request.user.isauthenticated():
        return render(request, 'register.html', {'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON})
    return render(request, 'splash.html', {'form':LoginForm()})

def userLogin(request):
    """ View called via post request from button on splashpage, attempt to login and load page 
        depending on registration status """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #Ensure login fields are filled out
        if form.errors:
            return render(request, 'splash.html',RequestContext(request,{'errors':form.errors}))
        
        else:            
            currentUser = authenticate(username=form.username,password=form.password) #form.username and form.password?
            #If user info is correct, retrieve login count
            if currentUser:
                login(request,currentUser)
            else:
                return render(request, 'splash.html',RequestContext(request,{'errors':"Invalid Username/Password. Please try again."}))            

def userRegistration(request):
    """ View called via create user button from splashpage, attempts to create user with post data
    Upon sucesful creation redirects to registration page, else returns to splash page"""
    if request.user.is_anonymous() or not request.user.isauthenticated():
        return render(request, 'splash.html', {'form':LoginForm()})
   
    form = LoginForm(request.POST)
    
    #Check user/password and ensure meets requirements
    if form.errors:
        return render(request, 'splash.html', RequestContext(request,{'errors':form.errors}))
        
    #Checks whether user already exists    
    if getUserProfile(form.username):
        return render(request, 'register.html',RequestContext(request,{'errors':"Username is already taken."}))
    username,password = form.username, form.password
    new_user = User.objects.create_user(username=username,password=password)
    new_user.save()
    new_user = authenticate(username=username,password=password) #django requires authentification before logging in
    login(request,new_user)
    return render(request, 'register.html', RequestContext(request,{}))    

def userLogout(request):
    """ Logs out current user session if one exists, return to splashpage"""
    if request.user.is_anonymous():
        return render(request, 'splash.html', {'form':LoginForm()})        
    elif request.user.isauthenticated() and 'logout' in request.POST:
        #User was logged in and the logout button was pressed
        logout(request)
    else:
        return render(request, 'splash.html', {'form':LoginForm()})

def dashboard(request):
    """ Button from registration page sends a post request to /dashboard. View takes in post data, populates user profile associated with user, then loads dashboard if no errors on registration page """
    dashboardContext = dashboardData(request)    
    if request.user.is_anonymous() or not request.user.isauthenticated():
        return render(request, 'splash.html',{'form':LoginForm()})
    elif not dashboardContext:
        #Attempt to create user profile with data
        if request.method == 'POST':
            gradInfo = GradForm(request.POST)
            majorInfo = MajorForm(request.POST)
            courseInfo = CourseFormSet(request.POST)
            errors = {}
            if gradInfo.errors or majorInfo.errors or CourseFormSet.errors:
                errors.update(gradInfo.errors)
                errors.update(majorInfo.errors)
                errors.update(courseInfo.errors)
                return render(request, 'register.html',RequestContext(request,{'errors':errors})) 
            major = majorInfo.major
            graduationSemester = gradInfo.graduationSemester 
            graduationYear = gradInfo.graduationYear  
            coursesTaken = []
            for form in courseInfo:
                course = form.cleaned_data.get('name')
                coursesTaken.append(course)
            newProfile = addUserProfile(request.user.username, major, graduationSemester, graduationYear, coursesTaken)
            if newProfile == SUCCESS:
                return render(request, 'dashboard.html',RequestContext(request,dashboardContext))
            else:
                return render(request, 'register.html',RequestContext(request,{'errors':"Error adding user profile to database. Please try again later."}))
        else:        
            return render(request, 'register.html',RequestContext(request,{}))
    else:
        return render(request, 'dashboard.html',RequestContext(request,dashboardContext))
        
def checkRegistration(request):
    """ Check whether or not a user has completed registration """    
    if not request.user.is_anonymous() and request.user.isauthenticated():
        if getUserProfile(request.user.username):
            return True
        else:
            return False
    else:
        return False

def dashboardData(request):
    """ Retrieve user profile information and return context dictionary for dashboard. """
    if checkRegistration(request):
        username = request.user.username
        userProfile = getUserProfile(username)
        userInformation = {}
        userInformation['unitsCompleted'] = getUnitsCompleted(username)
        userInformation['major'] = userProfile.major
        userInformation['graduationSemester'] = userProfile.graduationSemester
        userInformation['graduationYear'] = userProfile.graduationYear
        userInformation['remainingRequirements'] = remainingRequirements(getCoursesTaken(username), userProfile.college, majorToCollege(userProfile.major))
        return userInformation
    else:
        return False
