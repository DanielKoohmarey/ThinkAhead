from django.shortcuts import render
from darsplus.statics import SUCCESS
from darsplus.forms import LoginForm, EmailForm, GradForm, MajorForm, CourseFormSet
from darsplus.models import addUserProfile, getUserProfile, getCoursesTaken, getUnitsCompleted, majorToCollege, getCollegesToMajors, setEmail
from darsplus.requirementscode import remainingRequirements
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.forms.util import ErrorList
import json
import re

majorJSON = json.dumps(getCollegesToMajors())

@csrf_exempt
def splash(request):
    """ Load the splashpage if the user is not logged in, the registration page if they are logged in
        and have not registered, or the dashboard if they are logged in and have registered.
        Args:
            request (HttpRequest): The request sent the Django server 
        Returns:
            (HttpResponse) The data containing the page the browser will server to the client """
    if request.method == 'POST':
        if 'login' in request.POST:
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
                    return render(request, 'splash.html',{'errors':{"user":ErrorList([u"Invalid Username/Password. Please try again."])}, 'form':LoginForm()}) 
        else:
            if 'add' in request.POST:
                form = LoginForm(request.POST)
                
                #Check user/password and ensure meets requirements
                if form.errors:
                    return render(request, 'splash.html', RequestContext(request,{'errors':form.errors, 'form':LoginForm()}))
                
                username,password = request.POST['username'], request.POST['password']
                
                #Checks whether user already exists    
                if User.objects.filter(username=request.POST['username']):
                    return render(request, 'splash.html',RequestContext(request,{'errors':{"user":ErrorList([u"Username is already taken."])},'form':LoginForm()}))

                new_user = User.objects.create_user(username=username,password=password)
                new_user.save()
                new_user = authenticate(username=username,password=password) #django requires authentification before logging in
                login(request,new_user)
                return HttpResponseRedirect('/registration/')
    
    else:
        #Handle GET request
        if not request.user.is_authenticated():
            return render(request, 'splash.html', {'form':LoginForm()})
        else:
            return HttpResponseRedirect('/dashboard/')
            
    return render(request, 'splash.html',{'form':LoginForm()})

def registration_check(user):
    """ Check whether or not a user has completed registration. 
        Args: 
            user (django.contrib.auth.models.User): The user to check for registration
        Returns:
            (bool) True if the user has registered, False if the user has not/ is not logged in.
    """    
    if not user.is_anonymous() and getUserProfile(user.username):
        return True
    else:
        return False
        
@login_required
@csrf_exempt
def userRegistration(request):
    """ If there is no current user logged in, attempts to create user with post data.
    Upon sucesful creation redirects to registration page, else returns to splash page 
        Args:
            request (HttpRequest): The request sent the Django server 
        Returns:
            (HttpResponse) The data containing the page the browser will server to the client 
    """
    if registration_check(request.user):
        return HttpResponseRedirect('/dashboard/')
    elif request.method == 'POST':
        newUser = addUserProfile(*register(request))
        if newUser == SUCCESS:
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, 'registration.html',{'errors':"Error adding user profile to database. Please try again later.", 'form0': EmailForm(), 'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON})
    else:
        return render(request, 'registration.html', {'form0': EmailForm(), 'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON})

def register(request):
    """ Saves user profile information for the user
            Args:
            request (HttpRequest): The request sent the Django server 
        Returns:
            (list) The user profile information, [request.user.username (str), major (str), college (str), graduationSemester (str), graduationYear (str), coursesTaken(list)]
    """
    emailInfo = EmailForm(request.POST)
    majorInfo = MajorForm(request.POST)
    courseInfo = CourseFormSet(request.POST)
    errors = {}
    if emailInfo.errors or CourseFormSet.errors:
        errors.update(emailInfo.errors)
        for form in courseInfo:
            errors.update(form.errors)
    majorForm_errors = majorInfo.errors()
    if majorForm_errors:
        errors.update({'major':majorForm_errors})

    if errors:
        return render(request, 'registration.html',{'errors':errors,'form0': EmailForm(),'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON}) 
    
    setEmail(request.user.username,request.POST['email'])     
    major = request.POST['major']
    college = request.POST['college']
    graduationSemester = request.POST['semester'] 
    graduationYear = request.POST['year']  
    coursesTaken = []
    for form in courseInfo:
        course = form.cleaned_data.get('name')
        #Convert course name to our format
        #Supports cs.169, cs 170, cs188 type formats and any capitalization
        if course:
            course = course.strip().upper()
            course = course.replace(' ','.')
            periods = course.count('.')
            if periods:
                course = course.replace('.','',periods-1)
            else:
                m = re.search("\d",course)
                if m:
                    digit_index = m.start()
                    course = course[:digit_index]+'.'+course[digit_index:]
                else:
                    continue #could not determine course format, skipping course
            coursesTaken.append(course)
            
    return [request.user.username, major, college, graduationSemester, graduationYear, coursesTaken]
        
@csrf_exempt
def userLogout(request):
    """ Logs out current user session if one exists, return to splashpage
           Args:
            request (HttpRequest): The request sent the Django server 
        Returns:
            (HttpResponse) The data containing the page the browser will server to the client 
    """
    if not request.user.is_anonymous() and request.user.is_authenticated():
        #User was logged in and the logout button was pressed
        logout(request)
    return HttpResponseRedirect('/home/')
        
@login_required
@user_passes_test(registration_check, login_url='/registration/')
@csrf_exempt
def dashboard(request):
    """ Populates user profile associated with user with request POST data, 
    then loads dashboard if no errors occurred on registration page. If the user
    was not logged in, redirects to splash page.
        Args:
            request (HttpRequest): The request sent the Django server 
        Returns:
            (HttpResponse) The data containing the page the browser will server to the client 
    """
    dashboardContext = dashboardData(request)    

    if not dashboardContext:
        #Attempt to create user profile with data     
        return HttpResponseRedirect('/registration/') #GET request and user profile is not yet created
    else:
        return render(request, 'dashboard.html',dashboardContext)
        


def dashboardData(request):
    """ Retrieve user profile information and return context dictionary for dashboard. 
        Args:
            request (HttpRequest): The request sent the Django server 
        Returns:
            (dict) User profile information for the template context  
    """
    username = request.user.username
    userProfile = getUserProfile(username)
    userInformation = {}
    userInformation['unitsCompleted'] = getUnitsCompleted(username)
    userInformation['major'] = userProfile.major
    userInformation['graduationSemester'] = userProfile.graduationSemester
    userInformation['graduationYear'] = userProfile.graduationYear
    userInformation['requirements'] = remainingRequirements(getCoursesTaken(username), majorToCollege(userProfile.major), userProfile.major)
  
    return userInformation

@login_required
@user_passes_test(registration_check, login_url='/registration/')
def updateProfile(request):
    """ Allow a user to update their profile
        Args:
            request (HttpRequest): The request sent the Django server 
        Returns:
            (HttpResponse) The data containing the page the browser will server to the client 
    """
    if request.method == 'POST':
        newUser = addUserProfile(*register(request))
        if newUser == SUCCESS:
            return HttpResponseRedirect('/dashboard/')
        else:
            return newUser
    else:
        #TODO:PREPOPULATE WITH USER DATA
        #TODO:CHANGE BUTTON NAME TO SUBMIT using django.core.context_processors.request
        return render(request, 'registration.html',{'form0': EmailForm(), 'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON})