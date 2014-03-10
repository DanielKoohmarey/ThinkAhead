from django.shortcuts import render
from thinkahead.darsplus.forms import LoginForm, RegForm
from thinkahead.darsplus.models import addUserProfile
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    """ Load the homepage, or appropriate page depending on user status """
    if checkRegistration(request):
        return render(request, 'dashboard.html', dashBoardData(request.user.username) 
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
            currentUser = authenticate(username=context['username'],password=request.POST['password'])
            #If user info is correct, retrieve login count
            if currentUser:
                login(request,current_user)
            else:
                return render(request, 'home.html',RequestContext(request,{'errors':"Invalid Username/Password. Please try again."}))
        else:
            return render(request, 'home.html',RequestContext(request,{'errors':form.errors})

def userRegistration(request):
    """ View called via create user button from homepage, attempts to create user with post data
    Upon sucesful creation redirects to registration page, else returns to home page"""
    if not request.user.isauthenticated():
        return render(request, 'home.html',RequestContext(request,{'errors':"Username/Password cannot be left blank."}))
   
     form = LoginForm(request.POST)
    
    #Check user/password and ensure meets requirements
    if form.is_valid():
        return render(request, 'home.html',RequestContext(request,{'errors':"Username/Password cannot be left blank."}))
        
    #Checks whether user already exists    
    if User.objects.filter(username=request.POST['username']):
        return render(request, 'register.html',RequestContext(request,{'errors':"Username is already taken."}))
        
    new_user = User.objects.create_user(username=username,password=password)
    new_user.save()
    new_user = authenticate(username=context['username'],password=request.POST['password']) #django requires authentification before logging in
    login(request,new_user)
    return render(request, 'register.html', RequestContext(request,{}))    

def userLogout(request):
    """ Logs out current user session if one exists, return to homepage"""
    if request.user.isauthenticated() and 'logout' in request.POST:
        #User was logged in and the logout button was pressed
        logout(request)
    return render(request, 'home.html', RequestContext(request,{}))

def dashboard(request):
    """ Button from registration page sends a post request to /dashboard. View takes in post data, populates user profile associated with user, then loads dashboard if no errors on registration page """
    if not request.user.isauthenticated():
        return render(request, 'home.html',RequestContext(request,{}))
    elif not checkRegistration(request):
        #Attempt to create user profile with data
        if request.method == 'POST':
            form = RegForm(response.POST)
            if form.is_valid():
                return render(request, 'register.html',RequestContext(request,{'errors':form.errors})) 
            major = form.major  
            graduationSemester = form.graduationSemester 
            graduationYear = form.graduationYear  
            coursesTaken = form.coursesTaken 
            newProfile = addUserProfile(response.user.username, major, graduationSemester, graduationYear, coursesTaken)
            if newProfile == SUCCESS:
                return render(request, 'dashboard.html',RequestContext(request,dashboardData(request.user.username))
            else:
                return return render(request, 'register.html',RequestContext(request,{'errors'::"Error adding user profile to database. Please try again later."}))
        else:        
            return render(request, 'register.html',RequestContext(request,{}))
    else:
        return render(request, 'dashboard.html',RequestContext(request,dashboardData(request.user.username))
        
def checkRegistration(request):
    """ Check whether or not a user has completed registration """    
    if request.user.isauthenticated():
        if UserProfile.UserExists(request.user.username):
            return True
        else:
            return False
    else:
        return False

def dashboardData(user):
    """ Retrieve user profile information and return context dictionary for dashboard """
    pass
