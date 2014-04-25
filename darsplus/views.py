from django.shortcuts import render
from darsplus.statics import *
from darsplus.forms import LoginForm, EmailForm, GradForm, MajorForm, CourseFormSet
from darsplus.models import Courses, addUserProfile, getUserProfile, getCoursesTaken, getUnitsCompleted, majorToCollege, getCollegesToMajors, setEmail, setUserProfile, getPlanners, addCourseToPlanner, getAllCourses, removeCourseFromPlanner, getCourseInfo, totalUnitsPlanner, setPlanner
from darsplus.requirementscode import remainingRequirements
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.util import ErrorList
from darsplus.abbreviations import abbreviationDict, reverseAbbreviationDict, shorthandDict, reverseShorthandDict
import datetime
import json
import re

majorJSON = json.dumps(getCollegesToMajors())

""" ============= Functions required by decorators ========== """
def registrationCheck(user):
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
        
""" ============ View functions called from urls ================= """        
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
    if registrationCheck(request.user):
        return HttpResponseRedirect('/dashboard/')
    elif request.method == 'POST':
        newUser = addUserProfile(*register(request))
        if newUser == SUCCESS:
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, 'registration.html',{'errors':"Error adding user profile to database. Please try again later.", 'form0': EmailForm(), 'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON})
    else:
        return render(request, 'registration.html', {'form0': EmailForm(), 'form1': GradForm(), 'form2':MajorForm(), 'form3':CourseFormSet(), 'majorDict':majorJSON})
        
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
@user_passes_test(registrationCheck, login_url='/registration/')
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
    print "start"
    if not dashboardContext:
        #Attempt to create user profile with data     
        return HttpResponseRedirect('/registration/') #TODO: test if we can remove this, decorator now ensures user registered
    elif (request.is_ajax()) :#and request.method == 'POST': 
        #Add/Remove courses from the planner
        print "A"
        return handlePlannerData(request,dashboardContext)

    else: # Get. Just display dashboard, no update
        print "B"
        return render(request, 'dashboard.html',dashboardContext)

@login_required
@user_passes_test(registrationCheck, login_url='/registration/')
def updateProfile(request):
    """ Allow a user to update their profile
        Args:
            request (HttpRequest): The request sent the Django server 
        Returns:
            (HttpResponse) The data containing the page the browser will server to the client 
    """
    if request.method == 'POST': #updates user
        newUser = register(request)
        response = setUserProfile(*newUser)
        if not isinstance(newUser, list):
            return newUser #User did not fill out every field, show errors
        if response == SUCCESS:
            return HttpResponseRedirect('/dashboard/',{'update':True})
    else:
        profile = getUserProfile(request.user)
        initialData = []
        for course in profile.coursesTaken:
            initialData.append({'name':course.replace('.', ' ')}) # Revert our representation to a user-friendly one
        initialData.sort()
        formset = CourseFormSet(initial=initialData)

        return render(request,'registration.html',{'form0': EmailForm({'email':User.objects.filter(username=request.user)[0].email}), 
                                                   'form1': GradForm({'semester':profile.graduationSemester,'year':profile.graduationYear}),
                                                   'form2':MajorForm(initial={'college':profile.college, 'major':profile.major}),#,'college_id':2,'major_id':2}), # Does not work. Has to be the index
                                                   'form3':formset,
                                                   'majorDict':majorJSON,
                                                   'userCollege':profile.college,
                                                   'userMajor':profile.major,
                                                   }
                                                   )

def autocompleteCourse(request):
    """ Allow a user to update their profile
    Args:
    request (HttpRequest): The request sent the Django server which contains user's input into CourseForm
    Returns:
    (HttpResponse) The data containing the list of courses matching user's input
    """
    term = request.GET.get('term').upper().strip()
    name = term[:term.rfind(' ')].replace(' ','') if ' ' in term else term
    standardized = standardizeCourse(term)
    #Convert shorthands cs ->COMPSCI
    if term in shorthandDict:
        term = shorthandDict[term]
    #Convert shorthands ee 122 -> ELENG 122
    elif name in shorthandDict:
        term = shorthandDict[name]+term[term.rfind(' '):]
    #Name like cs169 or cs 169 resolved to COMPSCI.169
    elif standardized:
        term = standardized
    term = term.replace(' ','.') #Convert to database form
    courses = Courses.objects.filter(courseCode__contains=term)
    #Only return courses matching the user's input department
    if name in reverseAbbreviationDict:
        courses = [elem for elem in courses if elem.courseCode.split('.')[0]==name]
    results = []
    for c in courses:
        try:
            #Try to convert the name to something cleaner, COMPSCI.169 -> CS 169
            courseCode = dbToReadable(c.courseCode)
        except:
            courseCode = c.courseCode        
        courseJSON = {'id': c.id, 'label': courseCode, 'value': courseCode}
        results.append(courseJSON)
    data = json.dumps(results)
    return HttpResponse(data)
    
""" ====================================== Support functions for the views ====================================== """

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
        if emailInfo.errors:
            print "email error"
            errors.update(emailInfo.errors)
        
        for form in courseInfo:
            print form.errors
        #    errors.update(form.errors)
        
    majorForm_errors = majorInfo.errors()
    if majorForm_errors:
        print "major form error"
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
            valid = standardizeCourse(course)
            if valid:
                coursesTaken.append(valid)
            else:
                continue #could not determine course format, skipping course

    return [request.user.username, major, college, graduationSemester, graduationYear, coursesTaken]    
    
def standardizeCourse(course):
    """ Converts a course name into the standardized form NAME.NUMBER
        Args:
            course (str): The course name to standardize
        Returns:
            (str) the standardized course name of form NAME.NUMBER
    """
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
            course = ''
    if course:
        name,number = course[:course.rfind('.')], course[course.rfind('.'):]
        if name in abbreviationDict:
            course = abbreviationDict[name]+number
        elif name in shorthandDict:
            course = shorthandDict[name]+number
        if getCourseInfo(course)==ERR_NO_RECORD_FOUND:
            return ''
    return course
 
def dbToReadable(course):
    """ Converts a course name from database format DPT.NUM to readable ABBREVIATION NUM
    Args:
    course (str): The course in DB readable format
    Returns:
    (str): The course in human readable format
    """

    if course.count('.') >1:
        course = course.replace('.','',course.count('.')-1)
    course = course.replace('.',' ') 
    courseCode = course.split(' ')   
    if courseCode[0] in reverseShorthandDict:
        courseCode = ' '.join([reverseShorthandDict[courseCode[0]]]+courseCode[1:]).upper()
    else:
        courseCode = ' '.join(courseCode)
    return courseCode
   
def handlePlannerData(request,dashboardContext):
    """ Handles the user's planner action (add/remove) and updates their planner accordingly
       Args:
        request (HttpRequest): The request sent the Django server 
        dashboardContext (dict): The user information for the dashboard template
    Returns:
        (HttpResponse) The data containing the page the browser will server to the client 
    """
    user = request.user.username
    plannerID = getUserProfile(user).plannerID

    planners = request.POST.getlist('planners[]')
    for index in range(0, len(planners)):
        names = planners[index]
        courses = names.split(",")
        courses = filter(lambda course: course != '', courses)
        courses = [standardizeCourse(course) for course in courses]
        setPlanner(plannerID, index+1, courses)
    #request.method = 'GET' # prevent infinite loop because request is still ajax
    dashboardContext = dashboardData(request) # Updates context
    print "refreshing"
    return HttpRedirect('/registration/')
    #return render(request,'dashboard.html',dashboardContext)
        

def dashboardData(request):
    """ Retrieve user profile information and return context dictionary for dashboard. 
        Args:
            request (HttpRequest): The request sent the Django server 
        Returns:
            (dict) User profile information for the template context  
    """
    username = request.user.username
    userProfile = getUserProfile(username)
    plannerID = userProfile.plannerID
    userInformation = {}
    userInformation['unitsCompleted'] = int(getUnitsCompleted(username))
    userInformation['major'] = userProfile.major
    userInformation['graduationSemester'] = userProfile.graduationSemester
    userInformation['graduationYear'] = userProfile.graduationYear
    allCourses = getCoursesTaken(username) #If a course is in the planner, should be excluded as well 
    allCourses += getAllCourses(plannerID)
    userInformation['requirements'] = remainingRequirements(allCourses, majorToCollege(userProfile.major), userProfile.major)
    userInformation['planners'] = getPlanners(plannerID)
    unitCount = []
    currentSemester = getCurrentSemester()
    semesterNames = [getNextSemester(currentSemester)]

    dates = currentSemester.split(" ")
    oldSemester = dates[0]
    oldYear = datetime.date.today().year
    numPlanner = diffDates(oldSemester, oldYear, userProfile.graduationSemester, userProfile.graduationYear)
    for semester in range(1,numPlanner + 1):
        unitCount.append(totalUnitsPlanner(plannerID, semester))
        semesterNames.append(getNextSemester(semesterNames[-1]))

    semesterNames.pop() #remove extra name generated by loop
    userInformation['planners'] = zip(semesterNames, userInformation['planners'],unitCount)


    userInformation['unitsPlanner'] = int(userInformation['unitsCompleted']+sum(unitCount))
    
    userInformation['form'] = CourseFormSet()

    return userInformation

def getCurrentSemester():
    """ Get the current semester based on date
    Args:
    Returns:
        (str) SEM YR the semester and year
    """
    month = datetime.datetime.now().strftime("%m")
    semesters = {'Spring':['01','02','03','04','05'], 'Summer':['06','07','08'], 'Fall':['09','10','11','12']}
    for semester,months in semesters.items():
        if month in months:
            return '{} {}'.format(semester,datetime.datetime.now().strftime("%y"))
        
def getNextSemester(semester):
    """ Get the current semester based on date
    Args:
        semester (str): The current semester to get the next semester from
    Returns:
        (str) SEM YR the next semester and year
    """
    nextSemester = {'Fall':'Spring','Spring':'Summer','Summer':'Fall' }
    semester,year = semester.split()
    semester = nextSemester[semester]
    if semester == 'Spring':
        year = str(int(year)+1)
    return '{} {}'.format(semester,year)

def diffDates(oldSemester, oldYear, newSemester, newYear):
    """ Finds the number of semesters between old Semester-Year to new Semester-Year
    """

    semesters = ['Spring', 'Summer', 'Fall']

    if oldYear > newYear:
        return ERR_INVALID_DATE
    elif oldSemester not in semesters or newSemester not in semesters:
        return ERR_INVALID_DATE    
    else:
        if oldYear == newYear:    
            diff = semesters.index(newSemester) - semesters.index(oldSemester)
            if diff < 0:
                return ERR_INVALID_DATE
            else:
                return  diff

        else: # oldYear < newYear
            fill = len(semesters) - semesters.index(oldSemester)
            fill += semesters.index(newSemester)
            diff = ((newYear - 1) + 1 - (oldYear + 1)) * 3 # Number of semesters 
            return fill + diff

