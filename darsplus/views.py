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
from django.utils.datastructures import MultiValueDictKeyError
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
    term = request.GET.get('term')
    courses = Courses.objects.filter(courseCode__contains=term)
    results = []
    for c in courses:
        courseJSON = {'id': c.id, 'label': c.courseCode, 'value': c.courseCode}
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
    abbreviations = {'CS':'COMPSCI',
        'BIO':'BIOLOGY', 
        'EE':'ELENG', 
        'AEROSPACE STUDIES': 'AEROSPC',
        'AFRICAN AMERICAN STUDIES': 'AFRICAM',
        'AGRICULTURAL AND ENVIRON CHEMISTRY': 'AGR.CHM',
        'AGRICULTURAL AND RESOURCE ECONOMICS': 'ARESEC',
        'AMERICAN STUDIES': 'AMERSTD',
        'ANCIENT HISTORY AND MED. ARCH.': 'AHMA',
        'ANTHROPOLOGY': 'ANTHRO',
        'APPLIED SCIENCE AND TECHNOLOGY': 'AST',
        'ARABIC': 'ARABIC',
        'ARCHITECTURE': 'ARCH',
        'ASIAN AMERICAN STUDIES': 'ASAMST',
        'ASIAN STUDIES': 'ASIANST',
        'ASTRONOMY': 'ASTRON',
        'BENGALI': 'BANGLA',
        'BIBLIOGRAPHY': 'BIBLIOG',
        'BIOENGINEERING': 'BIO.ENG',
        'BIOLOGY': 'BIOLOGY',
        'BIOPHYSICS': 'BIOPHY',
        'CATALAN': 'CATALAN',
        'CELTIC STUDIES': 'CELTIC',
        'CHEMICAL & BIOMOLECULAR ENGINEERING': 'CHM.ENG',
        'CHEMISTRY': 'CHEM',
        'CHICANO STUDIES': 'CHICANO',
        'CHINESE': 'CHINESE',
        'CITY AND REGIONAL PLANNING': 'CY.PLAN','CIVIL AND ENVIRONMENTAL ENGINEERING': 'CIV.ENG',
        'CLASSICS': 'CLASSIC',
        'COGNITIVE SCIENCE': 'COG.SCI',
        'COLLEGE WRITING PROGRAM': 'COLWRIT',
        'COMPARATIVE BIOCHEMISTRY': 'COMPBIO',
        'COMPARATIVE LITERATURE': 'COM.LIT',
        'COMPUTATIONAL BIOLOGY': 'CMPBIO',
        'COMPUTER SCIENCE': 'COMPSCI',
        'CRITICAL THEORY GRADUATE GROUP': 'CRIT.TH',
        'CUNEIFORM': 'CUNEIF',
        'DEMOGRAPHY': 'DEMOG',
        'DEVELOPMENT PRACTICE': 'DEVP',
        'DEVELOPMENT STUDIES': 'DEV.STD',
        'DUTCH': 'DUTCH',
        'EARTH AND PLANETARY SCIENCE': 'EPS',
        'EAST ASIAN LANGUAGES AND CULTURES': 'EA.LANG',
        'EAST EUROPEAN STUDIES': 'EAEURST',
        'ECONOMICS': 'ECON',
        'EDUCATION': 'EDUC',
        'EDUCATION IN LANGUAGE AND LITERACY': 'EDUC-LL',
        'EDUCATIONAL ADMINISTRATION': 'EDUC-AE',
        'EGYPTIAN': 'EGYPT',
        'ELECTRICAL ENGINEERING': 'EL.ENG',
        'ENERGY AND RESOURCES GROUP': 'ENE&#44;RES',
        'ENGINEERING': 'ENGIN',
        'ENGLISH': 'ENGLISH',
        'ENVIRON SCI&#44; POLICY&#44; AND MANAGEMENT': 'ESPM',
        'ENVIRONMENTAL DESIGN': 'ENV.DES',
        'ENVIRONMENTAL ECONOMICS AND POLICY': 'ENVECON',
        'ENVIRONMENTAL SCIENCES': 'ENV.SCI',
        'ETHNIC STUDIES': 'ETH.STD',
        'ETHNIC STUDIES GRADUATE GROUP': 'ETH.GRP',
        'EURASIAN STUDIES': 'EURA.ST',
        'EVE/WKND MASTERS IN BUS. ADM.': 'EWMBA',
        'EXECUTIVE MASTERS IN BUS. ADM.': 'XMBA',
        'FILIPINO': 'FILIPN',
        'FILM AND MEDIA': 'FILM',
        'FOLKLORE': 'FOLKLOR',
        'FRENCH': 'FRENCH',
        "GENDER AND WOMEN'S STUDIES": 'GWS',
        'GEOGRAPHY': 'GEOG',
        'GERMAN': 'GERMAN',
        'GLOBAL METROPOLITAN STUDIES': 'GMS',
        'GLOBAL POVERTY AND PRACTICE': 'GPP',
        'GRAD STUDENT PROF DEVELOPMENT PGM': 'GSPDP',
        'GREEK': 'GREEK',
        'GROUP IN BUDDHIST STUDIES': 'BUDDSTD',
        'HEALTH AND MEDICAL SCIENCES': 'HMEDSCI',
        'HEBREW': 'HEBREW',
        'HINDI-URDU': 'HIN-URD',
        'HISTORY': 'HISTORY',
        'HISTORY OF ART': 'HISTART',
        'INDIGENOUS LANGUAGES OF AMERICAS': 'ILA',
        'INDUSTRIAL ENGIN AND OPER RESEARCH': 'IND.ENG',
        'INFORMATION': 'INFO',
        'INTEGRATIVE BIOLOGY': 'INTEGBI',
        'INTERDISCIPLINARY STUDIES FIELD MAJ': 'ISF',
        'INTERNATIONAL AND AREA STUDIES': 'IAS',
        'IRANIAN': 'IRANIAN',
        'ITALIAN STUDIES': 'ITALIAN',
        'JAPANESE': 'JAPAN',
        'JEWISH STUDIES': 'JEWISH',
        'JOURNALISM': 'JOURN',
        'KHMER': 'KHMER',
        'KOREAN': 'KOREAN',
        'LANDSCAPE ARCHITECTURE': 'LD.ARCH',
        'LANGUAGE PROFICIENCY PROGRAM': 'LAN.PRO',
        'LATIN': 'LATIN',
        'LATIN AMERICAN STUDIES': 'LATAMST',
        'LEGAL STUDIES': 'LEGALST',
        'LESBIAN GAY BISEXUAL TRANSGENDER ST': 'LGBT',
        'LETTERS AND SCIENCE': 'L&S',
        'LIBRARY AND INFORMATION STUDIES': 'LINFOST',
        'LINGUISTICS': 'LINGUIS',
        'MALAY/INDONESIAN': 'MALAY/I',
        'MASTERS IN BUSINESS ADMINISTRATION': 'MBA',
        'MASTERS IN FINANCIAL ENGINEERING': 'MFE',
        'MATERIALS SCIENCE AND ENGINEERING': 'MAT.SCI',
        'MATHEMATICS': 'MATH',
        'MECHANICAL ENGINEERING': 'MEC.ENG',
        'MEDIA STUDIES': 'MEDIAST',
        'MEDIEVAL STUDIES': 'MED.ST',
        'MIDDLE EASTERN STUDIES': 'M.E.STU',
        'MILITARY AFFAIRS': 'MIL.AFF',
        'MILITARY SCIENCE': 'MIL.SCI',
        'MOLECULAR AND CELL BIOLOGY': 'MCELLBI',
        'MUSIC': 'MUSIC',
        'NANOSCALE SCIENCE AND ENGINEERING': 'NSE',
        'NATIVE AMERICAN STUDIES': 'NATAMST',
        'NATURAL RESOURCES': 'NAT.RES',
        'NAVAL SCIENCE': 'NAV.SCI',
        'NEAR EASTERN STUDIES': 'NE.STUD',
        'NEUROSCIENCE': 'NEUROSC',
        'NEW MEDIA': 'NWMEDIA',
        'NUCLEAR ENGINEERING': 'NUC.ENG',
        'NUTRITIONAL SCIENCES AND TOXICOLOGY': 'NUSCTX',
        'OPTOMETRY': 'OPTOM',
        'PEACE AND CONFLICT STUDIES': 'PACS',
        'PERSIAN': 'PERSIAN',
        'PH.D. IN BUSINESS ADMINISTRATION': 'PHDBA',
        'PHILOSOPHY': 'PHILOS',
        'PHYSICAL EDUCATION': 'PHYS.ED',
        'PHYSICS': 'PHYSICS',
        'PLANT AND MICROBIAL BIOLOGY': 'PLANTBI',
        'POLITICAL ECONOMY': 'POLECON',
        'POLITICAL SCIENCE': 'POL.SCI',
        'PORTUGUESE': 'PORTUG',
        'PRACTICE OF ART': 'ART',
        'PSYCHOLOGY': 'PSYCH',
        'PUBLIC HEALTH': 'PB.HLTH',
        'PUBLIC POLICY': 'PUB.POL',
        'PUNJABI': 'PUNJABI',
        'RELIGIOUS STUDIES': 'RELIGST',
        'RHETORIC': 'RHETOR',
        'SANSKRIT': 'SANSKR',
        'SCANDINAVIAN': 'SCANDIN',
        'SCIENCE AND MATHEMATICS EDUCATION': 'SCMATHE',
        'SCIENCE AND TECHNOLOGY STUDIES': 'STS',
        'SEMITICS': 'SEMITIC',
        'SLAVIC LANGUAGES AND LITERATURES': 'SLAVIC',
        'SOCIAL WELFARE': 'SOC.WEL',
        'SOCIOLOGY': 'SOCIOL',
        'SOUTH AND SOUTHEAST ASIAN STUDIES': 'S&#44;SEASN',
        'SOUTH ASIAN': 'S.ASIAN',
        'SOUTHEAST ASIAN': 'SEASIAN',
        'SPANISH': 'SPANISH',
        'SPECIAL EDUCATION': 'EDUCSPE',
        'STATISTICS': 'STAT',
        'TAGALOG': 'TAGALG',
        'TAMIL': 'TAMIL',
        'TELUGU': 'TELUGU',
        'THAI': 'THAI',
        'THEATER&#44; DANCE&#44; AND PERFORMANCE ST': 'THEATER',
        'TIBETAN': 'TIBETAN',
        'TURKISH': 'TURKISH',
        'UNDERGRAD INTERDISCIPLINARY STUDIES': 'UGIS',
        'UNDERGRAD. BUSINESS ADMINISTRATION': 'UGBA',
        'VIETNAMESE': 'VIETNMS',
        'VISION SCIENCE': 'VIS.SCI',
        'VISUAL STUDIES': 'VIS.STD',
        'YIDDISH': 'YIDDISH'}#TODO: Build abbreviation table
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
        if name in abbreviations:
            course = abbreviations[name]+number
        if getCourseInfo(course)==ERR_NO_RECORD_FOUND: #else possibly covnert to for loop for all possible conversions
            return ''
    return course
    
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
        
    
    """
    if index not in [str(ele) for ele in range(16)]: #Not valid for new save planner will wait to integrate
        dashboardContext.update({'errors':{'index':"{}. Please enter a valid numeric number.".format(index+" is not a valid semester number" if index else "Index cannot be left blank.")}})
        return render(request, 'dashboard.html',dashboardContext)
    
    courseName = standardizeCourse(request.POST['course'])

    try:
        if not courseName:
            dashboardContext.update({'errors':{'name':"{} is not a valid course name. Please ensure you are using the appropriate abbreviation of the major.".format(courseName)}})
        elif courseName in getCoursesTaken(user):
            dashboardContext.update({'errors':{'name':"You have already taken {}.".format(courseName)}})
        elif request.POST['change'] == 'add':
            if addCourseToPlanner(plannerID, index, courseName) in [ERR_NO_RECORD_FOUND, ERR_RECORD_EXISTS]:
                dashboardContext.update({'errors':{'index':"{} is not a valid course name or has already been added.".format(courseName)}})
            else:
                dashboardContext = dashboardData(request)    
        elif request.POST['change'] == 'remove':
            if removeCourseFromPlanner(plannerID, index, courseName) == ERR_NO_RECORD_FOUND:
                dashboardContext.update({'errors':{'name':"{} is not a valid course name to remove.".format(courseName)}})
            else:
                dashboardContext = dashboardData(request)
    except MultiValueDictKeyError:
        dashboardContext.update({'errors':{'change':"Please select either add or remove."}})
    return render(request, 'dashboard.html',dashboardContext)
    """

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

def diffSemesters(oldSemester, newSemester):
    """ Finds the number of semesters in between the two semesters
    
    Args:
        oldSemester (str): current semester
        newSemester (str): graduation year
    Returns:
        (int) Difference between number of semesters
    """
    semesters = ['Spring', 'Summer', 'Fall']
