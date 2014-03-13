from django.shortcuts import render
from thinkahead.darsplus.statics import SUCCESS
from thinkahead.darsplus.forms import LoginForm, RegForm
from thinkahead.darsplus.models import addUserProfile, getUserProfile, getCoursesTaken, getUnitsCompleted
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    """ Load the homepage, or appropriate page depending on user status """
    dashboardContext = dashboardData(request)
    if dashboardContext:
        return render(request, 'dashboard.html', RequestContext(request,dashboardContext)) 
    elif request.user.is_anonymous():
        return render(request)
    elif request.user.isauthenticated():
        return render(request, 'register.html', {})
    return render(request, 'home.html', {})

def userLogin(request):
    """ View called via post request from button on homepage, attempt to login and load page 
        depending on registration status """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #Ensure login fields are filled out
        if form.is_valid():
            currentUser = authenticate(username=request.POST['username'],password=request.POST['password']) #form.username and form.password?
            #If user info is correct, retrieve login count
            if currentUser:
                login(request,currentUser)
            else:
                return render(request, 'home.html',RequestContext(request,{'errors':"Invalid Username/Password. Please try again."}))
        else:
            return render(request, 'home.html',RequestContext(request,{'errors':form.errors}))

def userRegistration(request):
    """ View called via create user button from homepage, attempts to create user with post data
    Upon sucesful creation redirects to registration page, else returns to home page"""
    if request.user.is_anonymous() or not request.user.isauthenticated():
        return render(request, 'home.html',RequestContext(request,{}))
   
    form = LoginForm(request.POST)
    
    #Check user/password and ensure meets requirements
    if form.is_valid():
        return render(request, 'home.html',RequestContext(request,{'errors':"Username/Password cannot be left blank."}))
        
    #Checks whether user already exists    
    if User.objects.filter(username=request.POST['username']):
        return render(request, 'register.html',RequestContext(request,{'errors':"Username is already taken."}))
    username,password = request.POST['username'], request.POST['password']
    new_user = User.objects.create_user(username=username,password=password)
    new_user.save()
    new_user = authenticate(username=username,password=password) #django requires authentification before logging in
    login(request,new_user)
    return render(request, 'register.html', RequestContext(request,{}))    

def userLogout(request):
    """ Logs out current user session if one exists, return to homepage"""
    if request.user.is_anonymous():
        return render(request, 'home.html', RequestContext(request,{}))        
    elif request.user.isauthenticated() and 'logout' in request.POST:
        #User was logged in and the logout button was pressed
        logout(request)
    else:
        return render(request, 'home.html', RequestContext(request,{}))

def dashboard(request):
    """ Button from registration page sends a post request to /dashboard. View takes in post data, populates user profile associated with user, then loads dashboard if no errors on registration page """
    dashboardContext = dashboardData(request)    
    if request.user.is_anonymous() or not request.user.isauthenticated():
        return render(request, 'home.html',RequestContext(request,{}))
    elif not dashboardContext:
        #Attempt to create user profile with data
        if request.method == 'POST':
            form = RegForm(request.POST) #can cast any form class from request.post TODO: do one for each form 
            if form.is_valid():
                return render(request, 'register.html',RequestContext(request,{'errors':form.errors})) 
            major = form.major  
            graduationSemester = form.graduationSemester 
            graduationYear = form.graduationYear  
            coursesTaken = form.coursesTaken 
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
        userInformation['coursesTaken'] = getCoursesTaken(username)
        userInformation['unitsCompleted'] = getUnitsCompleted(username)
        userInformation['major'] = userProfile.major
        userInformation['graduationSemester'] = userProfile.graduationSemester
        userInformation['graduationYear'] = userProfile.graduationYear
        return userInformation
    else:
        return False