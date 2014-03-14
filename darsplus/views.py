from django.shortcuts import render
from darsplus.statics import SUCCESS
from darsplus.forms import LoginForm, GradForm, MajorForm, CourseFormSet
from darsplus.models import addUserProfile, getUserProfile, getCoursesTaken, getUnitsCompleted, majorToCollege, getCollegesToMajors
from darsplus.requirementscode import remainingRequirements
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import json

majorJSON = json.dumps(getCollegesToMajors())

@csrf_exempt
def splash(request):
    """ Load the splashpage, or appropriate page depending on user status """
    if request.method == 'POST':
        if 'Login' in request.POST:
            form = LoginForm(request.POST)
            #Ensure login fields are filled out
            if form.errors:
                return render(request, 'splash.html',{'errors':form.errors,'form':LoginForm()})
            
            else:            
                currentUser = authenticate(username=request.POST['username'],password=request.POST['password'])
                if currentUser:
                    login(request,currentUser)
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return render(request, 'splash.html',{'errors':"Invalid Username/Password. Please try again.", 'form':LoginForm()}) 
        else:
            if request.method=='POST':
                form = LoginForm(request.POST)
                
                #Check user/password and ensure meets requirements
                if form.errors:
                    return render(request, 'splash.html', RequestContext(request,{'errors':form.errors, 'form':LoginForm()}))
                
                username,password = request.POST['username'], request.POST['password']
                
                #Checks whether user already exists    
                if User.objects.get(username=request.POST['username']):
                    return render(request, 'splash.html',RequestContext(request,{'errors':"Username is already taken.",'form':LoginForm()}))
        
                new_user = User.objects.create_user(username=username,password=password)
                new_user.save()
                new_user = authenticate(username=username,password=password) #django requires authentification before logging in
                login(request,new_user)
                return render(request, 'registration.html', {'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON})    
    
    else:
        dashboardContext = dashboardData(request)
        if dashboardContext:
            return HttpResponseRedirect('/dashboard/')
        elif request.user.is_authenticated():
            return HttpResponseRedirect('/registration/')
        else:
            return render(request, 'splash.html', {'form':LoginForm()})
            
#@login_required
@csrf_exempt
def userRegistration(request):
    """ View called via create user button from splashpage, attempts to create user with post data
    Upon sucesful creation redirects to registration page, else returns to splash page"""
    if checkRegistration(request.user.username):
        return HttpResponseRedirect('/dashboard/')
    elif request.method == 'POST':
        gradInfo = GradForm(request.POST)
        majorInfo = MajorForm(request.POST)
        courseInfo = CourseFormSet(request.POST)
        errors = {}
        if gradInfo.errors or majorInfo.errors or CourseFormSet.errors:
            errors.update(gradInfo.errors)
            errors.update(majorInfo.errors)
            for form in courseInfo:
                errors.update(form.errors)
            return render(request, 'registration.html',{'errors':errors,'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON}) 
        major = request.POST['major']
        graduationSemester = request.POST['semester'] 
        graduationYear = request.POST['year']  
        coursesTaken = []
        for form in courseInfo:
            course = form.cleaned_data.get('name')
            coursesTaken.append(course)
        newProfile = addUserProfile(request.user.username, major, graduationSemester, graduationYear, coursesTaken)
        if newProfile == SUCCESS:
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, 'registration.html',{'errors':"Error adding user profile to database. Please try again later.", 'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON})
    if request.user.is_authenticated():
        return render(request, 'registration.html', {'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON})
    else:
        return HttpResponseRedirect('/home/')
@csrf_exempt
def userLogout(request):
    """ Logs out current user session if one exists, return to splashpage"""
    if request.user.is_anonymous():
        return HttpResponseRedirect('/home/')       
    elif request.user.is_authenticated() and 'logout' in request.POST:
        #User was logged in and the logout button was pressed
        logout(request)
    else:
        return HttpResponseRedirect('/home/')

#@login_required
@csrf_exempt
def dashboard(request):
    """ Button from registration page sends a post request to /dashboard. View takes in post data, populates user profile associated with user, then loads dashboard if no errors on registration page """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    dashboardContext = dashboardData(request)    

    if not dashboardContext:
        #Attempt to create user profile with data     
        return HttpResponseRedirect('/registration/') #GET request and user profile is not yet created
    else:
        return render(request, 'dashboard.html',dashboardContext)
        
def checkRegistration(request):
    """ Check whether or not a user has completed registration """    
    if request.user.is_authenticated():
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
