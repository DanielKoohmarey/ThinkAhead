__author__ = 'Jessica'
from darsplus.models import getCourseUnits
import re
import os, sys
class MyError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
def main():
	print 'hello'
"""
Determines the number of units each course is through accessing the database of classes and units
For now it just returns 4 for the sake of testing
"""
def units(course):
	return getCourseUnits(course)
	#return 4
"""
handles a simple requirement that a student must take a class
formally known as req but refered to as reqName
the description is an explanation of the general requirement
"""
def basicReq(takenClasses, req, reqName, description):
	if (req in takenClasses):
		return {'reqName':reqName, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName], 'courseLeft':[]}
	else:
		return {'reqName':reqName, 'reqCompleted':False, 'reqDescription':description,'courseDone':[], 'courseLeft':[reqName]}
"""
handles a relatively simple requirement known as requirement
that a student must take one of two classes
formally known as req and req1 but refered to as reqName and reqName1
the description is an explanation of the general requirement
"""
def twoChoiceReq(takenClasses, requirement, req, reqName, req1, reqName1, description):
	if (req in takenClasses)and (req1 in takenClasses):
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName,reqName1], 'courseLeft':[]}
	elif (req in takenClasses):
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName], 'courseLeft':[reqName1]}
	elif (req1 in takenClasses):
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName1], 'courseLeft':[reqName]}
	else:
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[], 'courseLeft':[reqName, reqName1]}
"""
handles a relatively simple requirement known as requirement
that a student must take two classes
formally known as req and req1 but refered to as reqName and reqName1
the description is an explanation of the general requirement
"""
def twoReq(takenClasses, requirement, req, reqName, req1, reqName1, description):
	if ((req in takenClasses)and (req1 in takenClasses)):
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName, reqName1], 'courseLeft':[]}
	elif (req1 in takenClasses):
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[reqName1], 'courseLeft':[reqName]}
	elif (req in takenClasses):
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[reqName], 'courseLeft':[reqName1]}
	else:
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[], 'courseLeft':[reqName, reqName1]}
"""
handles the complex requirement known as requirement
that a student must take one of a large number classes
these requirements are stored in a dictionary, requirements, that maps req to reqName
the description is an explanation of the general requirement
"""
def manyChoiceReq(takenClasses, requirement, requirements, description):
	listOfClassesTaken=[]
	listOfClassesNotTaken=[]
	# iterate over all elements in the dictionary to check if they have been taken or not
	for key in requirements:
		if (key in takenClasses):
			listOfClassesTaken.append(requirements[key])
		else:
			listOfClassesNotTaken.append(requirements[key])
	# No classes on the list were taken
	if (not listOfClassesTaken):
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[], 'courseLeft':listOfClassesNotTaken}
	# Some class was taken
	else:
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':listOfClassesTaken, 'courseLeft':listOfClassesNotTaken}
	return ans
"""
handles the complex requirement known as requirement
that a student must take at least i of a large number classes
these requirements are stored in a dictionary, requirements, that maps req to reqName
the description is an explanation of the general requirement
"""
def doSomeManyChoiceReq(takenClasses, requirement, requirements, description, i):
	listOfClassesTaken=[]
	listOfClassesNotTaken=[]
	# iterate over all elements in the dictionary to check if they have been taken or not
	for key in requirements:
		if (key in takenClasses):
			listOfClassesTaken.append(requirements[key])
		else:
			listOfClassesNotTaken.append(requirements[key])
	# Less than i classes on the list were taken
	if (len( listOfClassesTaken)<i):
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':listOfClassesTaken, 'courseLeft':listOfClassesNotTaken}
	# At least i classes were taken
	else:
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':listOfClassesTaken, 'courseLeft':listOfClassesNotTaken}
	return ans

#college is in {Engineering, Chemistry, NaturalResources, LettersAndSciences, Haas, EnvironmentalDesign}
def abbreviateMajor(major):
	abr = {'EECS':'Electrical Engineering & Computer Sciences',
	'BIOENG':'Bioengineering', 'CIVENG':'Civil and Environmental Engineering', 'COENG':'Computational Engineering Science',
	'ENENG':'Energy Engineering', 'ENGMS':'Engineering Math and Statistics', 
	'ENGP':'Engineering Physics','INDENG':'Industrial Engineering & Operations Research',
	'MATSCI':'Materials Science & Engineering', 'MECENG':'Mechanical Engineering',
	'NUCENG':'Nuclear Engineering', 'BIOMATSCI':'Bioengineering and Materials Science & Engineering',
	'EECSMATSCI':'Electrical Engineering & Computer Sciences and Materials Science & Engineering',
	'EECSNUCENG':'Electrical Engineering & Computer Sciences and Nuclear Engineering',
	'MATMECENG':'Materials Science & Engineering and Mechanical Engineering',
	'MATNUCENG':'Materials Science & Engineering and Nuclear Engineering',
	'MECNUCENG':'Mechanical Engineering and Nuclear Engineering'}
	abr = dict (zip(abr.values(),abr.keys()))
	return abr[major.replace('and','&')]

def abbreviateCollege(college):
	abr = {"College of Engineering":'Engineering'}
	return abr[college]
	
"""
if college is Chemistry then major is in {BSCHEM:'Bachelor of Science Degree in Chemistry',
	CHEMENG:'Chemical Engineering', CHEMBIO:'Chemical Biology', BACHEM:'Bachelor of Arts Degree in Chemistry'
	CHEMMATSCI:'Chemical Engineering and Materials Science and Engineering',
	CHEMNUCENG:'Chemical Engineering and Nuclear Engineering'}
if college is NaturalResources then major is in {}
if college is LettersAndSciences then major is in {AMERSTD:'American Studies'
	ASIANST: 'Asian Studies', COGSCI: 'Cognitive Science', DEVSTD:'Development Studies',
	ISF: 'Interdisciplinary Studies', LATAMST:'Latin American Studies', LEGALST:'Legal Studies',
	MEDIAST: 'Media Studies', MESTU:'Middle Eastern Studies', PACS:'Peace and Conflict Studies',
	POLECON:'Political Economy',RELIGST:'Religious Studies', AFRICAM:'African American Studies',
	ANTHRO:'Anthropology', ASAMDST:'Asian American and Asian Diaspora Studies',
	CHICANO: 'Chicano Studies',ECON:'Economics', ENVECON:'Environmental Economics',
	ETHSTD:'Ethnic Studies', GWS:'Gender & Women's Studies', GEOG:'Geography', HISTORY:'History',
	LINGUIS:'Linguistics', NATAMS:'Native American', POLSCI:'Political Science',
	PSYCH:'Psychology', SOCWEL:'Social Welfare', SOCIOL:'Sociology', ASTRON:'Astronomy',
	CHEM:'Chemistry', COMPSCI:'Computer Science', EPS:'Earth and Planetary Science',
	AMATH:'Applied Mathematics', PMATH:'Pure Mathematics', OPER:'Operations Research and Management',
	PHYSSCI:'Physical Sciences', PHYSICS:'Physics', STAT:'Statistics', INTEGBI:'Integrative Biology',
	MCELLBI:'Molecular and Cell Biology', PBHLTH:'Public Health', HISTART:'History of Art',
	ART:'Practice of Art', CELTIC:'Celtic Studies', CLASSIC:'Classics', COMLIT:'Comparative Literature',
	EALANG:'East Asian Languages and Cultures', ENGLISH:'English', FILM:'Film',
	FRENCH:'French', GERMAN:'German', ITALIAN:'Italian Studies',MUSIC:'Music',
	NESTUD:'Near Eastern Studies',PHILOS:'Philosophy', RHETOR:'Rhetoric', SCANDIN:'Scandinavian',
	SLAVIC:'Slavic Languages and Literatures', SEASN:'South and Southeast Asian Studies',
	SPANISH:'Spanish and Portuguese', THEATER:'Theater, Dance, and Performance Studies'}
if college is Haas then major is in {UGBA:'Undergraduate Business Administration'}
if college is EnvironmentalDesign then major is in {ARCH:'Architecture', CYPLAN:'City and Regional Planning',
	LDARCH:'Landscape Architecture and Environmental Planning', URDES:'Urban Design',
	SENVDES:'Sustainable Environmental Design'}
"""
def remainingRequirements(takenClasses, college, major):
	major = abbreviateMajor(major)
	college = abbreviateCollege(college)
	ans = [];
	# University Requirements: Common for everyone
	#American Cultures
	ac=False
	for item in takenClasses:
		if 'AC' in item:
			ac=True
	if ac:
		ans.append({'reqName':'American Cultures', 'reqCompleted':True, 'reqDescription':"Take at least one course labeled AC",'courseDone':[], 'courseLeft':[]})
	else:
		ans.append({'reqName':'American Cultures', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled AC",'courseDone':[], 'courseLeft':[]})
	#120 units
	unit=0
	for item in takenClasses:
		unit+=units(item)
	if unit>=120:
		ans.append({'reqName':'Unit Requirement', 'reqCompleted':True, 'reqDescription':"Complete at least 120 units",'courseDone':[], 'courseLeft':[]})
	else:
		ans.append({'reqName':'Unit Requirement', 'reqCompleted':False, 'reqDescription':"Complete at least 120 units",'courseDone':[], 'courseLeft':[]})
	#American Institutions and History
	ans.append({'reqName':'American Institutions and History', 'reqCompleted':True, 'reqDescription':"This requirement is usually satisfied before coming to UC Berkeley. See http://registrar.berkeley.edu/?PageID=ahi.html for more information",'courseDone':[], 'courseLeft':[]})
	#Entry Level Writing
	ans.append({'reqName':'Entry Level Writing', 'reqCompleted':True, 'reqDescription':"This requirement is usually satisfied before coming to UC Berkeley but can be fulfilled by taking a placement exam. See http://writing.berkeley.edu/classes-and-awp/awp-exam for more information",'courseDone':[], 'courseLeft':[]})
	#Residency
	ans.append({'reqName':'Residency', 'reqCompleted':True, 'reqDescription':"There are residency requirements placed on students but our program is not capabale of checking if they are fulfilled. See http://ls-advise.berkeley.edu/requirement/summary.html for more information",'courseDone':[], 'courseLeft':[]})
	# College of Engineering
	if(college=='Engineering'):
		# College Requirements
		#Reading and Composition
		OneA=False
		OneB=False
		for item in takenClasses:
			if 'R1A' in item:
				OneA=True
			if 'R1B' in item:
				OneB=True
		if (OneA and OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':True, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		elif (OneA):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1A",'courseDone':[], 'courseLeft':[]})
		elif (OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1B",'courseDone':[], 'courseLeft':[]})
		else:
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		#Electives: Humanities / Social Studies
		#A minimum of six courses from the approved Humanities/Social Sciences (H/SS) lists. 
		#At least two of the courses must be upper division (courses numbered 100--196.) 
		#At  least two of the courses must be from the same department and at least one of  the two must be upper division. (*Series) 
		#No courses offered by an Engineering  department (IEOR, CE, etc.) other than BIOE 100, COMPSCI C79,  ENGIN 125, ENGIN 130AC,  and ME 191AC may be used to complete H/SS requirements. 
			ans.append({'reqName':'Electives: Humanities / Social Studies', 'reqCompleted':True, 'reqDescription':"A minimum of six courses from the approved Humanities/Social Sciences (H/SS) lists. At least two of the courses must be upper division (courses numbered 100--196.) At  least two of the courses must be from the same department and at least one of  the two must be upper division.",'courseDone':[], 'courseLeft':[]})
		# Electrical Engineering & Computer Sciences
		if(major=='EECS'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Computer Science 70
			ans.append(basicReq(takenClasses, 'COMPSCI.70', 'CS 70', "The sophomore year Discrete Math requirement"))
			#Physics 7C or H7C,Chemistry 1A and 1AL, Chemistry 1B, 3A, 3B , 4A, 4B or 5.Biology 1A/1AL, Biology 1B, Astronomy 7A or B,Molecular and Cell Biology 32/32L
			nat={'PHYSICS.7C':'Physics 7C','CHEM.1A':'Chem 1A','CHEM.1B':'Chem 1B','CHEM.3A':'Chem 3A','CHEM.3B':'Chem 3B','CHEM.4A':'Chem 4A','CHEM.4B':'Chem 4B','CHEM.5':'Chem 5','BIOLOGY.1A':'Bio 1A','BIOLOGY.1B':'Bio 1B','ASTRO.7A':'Astro 7A','ASTRO.7B':'Astro 7B','MCELLBI.32':'MCB 32'}
			ans.append(manyChoiceReq(takenClasses, 'Natural Science', nat, "Requirement of one of Physics 7C or H7C,Chemistry 1A and 1AL, Chemistry 1B, 3A, 3B , 4A, 4B or 5.Biology 1A/1AL, Biology 1B, Astronomy 7A or B,Molecular and Cell Biology 32/32L"))
			#45 units of technical engineering courses comprised of at least 20 units of upper-division EECS courses
			num=0
			for item in takenClasses:
				if((re.search(r'ELENG.1\d\d',item))or((re.search(r'COMPSCI.1\d\d',item)))):
					num+=units(item)
			if (num>=20):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 20 units of upper-division EECS courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 20 units of upper-division EECS courses. "+"You have only taken "+str(num),'courseDone':[], 'courseLeft':[]})
			
			#Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CSH195; Engin 125, 130AC, 140; IEOR 172, IEOR 190 series; IEOR 191; ME 191AC, 190K; 191K
			#15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K.
			num=0
			for item in takenClasses:
				if ((('ENG' in item)or ('COMPSCI' in item)or('MATSCI'in item)or ('NSE' in item))and (not (('ENGLISH' in item)or ('.24' in item)or ('.39' in item)or ('.84' in item)or ('BIOENG.100' in item)or ('COMPSCI.C79' in item)or ('COMPSCI.195' in item)or ('COMPSCI.H195' in item)or ('ENGIN.125' in item)or ('ENGIN.130AC' in item)or ('ENGIN.140' in item)or ('INDENG.172' in item)or ('INDENG.190' in item)or ('INDENG.191' in item)or ('MECENG.191AC' in item)or ('MECENG.190K' in item)or ('MECENG.191K' in item)))):
					num+=units(item)
			if (num>=15):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K.",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K."+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#EE 20N-Structure and Interpretation of Systems and Signals
			ans.append(basicReq(takenClasses, 'ELENG.20N', 'EE 20N', "The sophomore year Structure and Interpretation of Systems and Signals requirement"))
			#EE 40-Introduction to Microelectronic Circuits
			ans.append(basicReq(takenClasses, 'ELENG.40', 'EE 40',  "The sophomore year Electrical Engineering requirement"))
			#Computer Science 61B, Data Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61B', 'CS 61B', "The sophomore year Programming Data Structures requirement"))
			#CS 61A-Structure and Interpretation of Computer Programs
			ans.append(basicReq(takenClasses, 'COMPSCI.61A', 'CS 61A', "The freshman year Structure and Interpretation of Computer Programs requirement"))
			#CS 61C-Machine Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61C','CS 61C', "The junior year Machine Structures requirement"))
			#Ethics Requirement:CS 195, CS H195, ERG 100 or ERG C100, ISF 60 ISF 100D
			ethic={'COMPSCI.195':'CS 195','COMPSCI.H195':'CS H195','ENERES.100':'ERG 100','ENERES.C100':'ERG C100','ISF.100D':'ISF 100D'}
			ans.append(manyChoiceReq(takenClasses, 'Ethics Requirement', ethic, "One required elective with an emphasis on ethics"))
			#Design Requirement:EE C125, C128, 130, 140, 141, 143, C149, 192,CS C149, 150, 160, 162, 164, 169, 184, 186 A course in other engineering departments having substantial engineering design content can be substituted by petition.
			design={'ELENG.C125':'EE C125','ELENG.C128':'EE C128','ELENG.130':'EE 130','ELENG.140':'EE 140','ELENG.141':'EE 141','ELENG.143':'EE 143','ELENG.C149':'EE C149','ELENG.192':'EE 192','COMPSCI.C149':'CS C149','COMPSCI.150':'CS 150','COMPSCI.160':'CS 160','COMPSCI.162':'CS 162','COMPSCI.164':'CS 164','COMPSCI.169':'CS 169','COMPSCI.184':'CS 184','COMPSCI.186':'CS 186'}
			"""advancement"""
			ans.append(manyChoiceReq(takenClasses, 'Design Requirement', design, "One required design class from the list **A course in other engineering departments having substantial engineering design content can be substituted by petition"))
			return ans
		# BioEngineering
		elif(major=='BIOENG'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Chemistry 3A and 3AL , or Chem 112A
			if(('CHEM.3A' in takenClasses) and ('CHEM.3AL' in takenClasses)):
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':['Chem 3A', 'Chem 3AL'], 'courseLeft':['Chem 112A']})
			elif('CHEM.112A' in takenClasses):
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':['Chem 112A'], 'courseLeft':['Chem 3A', 'Chem 3AL']})
			else:
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 3A', 'Chem 3AL','Chem 112A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#BioE 10
			ans.append(basicReq(takenClasses, 'BIOENG.10', 'BioE 10', "The freshman year requirement of BioE"))
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Freshman Seminar: BioE 24 and BioE 25
			ans.append( twoReq(takenClasses,'Freshman Seminar', 'BIOENG.24', 'BioE 24', 'BIOENG.25', 'BioE 25', "The freshman year bioengineering seminar requirement of both BioE 24 and 25"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Biology 1A & 1AL , General Biology
			ans.append( twoReq(takenClasses,'General Biology', 'BIOLOGY.1A', 'Bio 1A', 'BIOLOGY.1AL', 'Bio 1AL', "The sophomore year biology requirement of both Bio 1A and 1AL"))
			#Engineering/Biology Preparation
			bioprep= {'ENGIN.45':'E 45', 'ELENG.20N':'EE 20N', 'ELENG.40':'EE 40','ELENG.100':'EE 100','CHEM.120B':'Chem 120B','BIOENG.C105B':'BioE C105B','CHEM.C130':'Chem C130','MCELLBI.100A':'MCB 100A', 'CIVENG.C30':'CE C30','MECENG.C85':'ME C85','COMPSCI.61B':'CompSci 61B','COMPSCI.61BL':'CompSci 61BL'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Engineering/Biology Preparation', bioprep, "Sophomore year engineering or biology preparation requireing two classes from the given list",2))
			#Bioengineering Design Project
			design={'BIOENG.121L':'BioE 121L','BIOENG.140L':'BioE 140L','BIOENG.168L':'BioE 168L','BIOENG.192':'BioE 192','BIOENG.H194':'BioE H194','BIOENG.196':'BioE 196'}
			ans.append(manyChoiceReq(takenClasses, 'Bioengineering Design Project', design, "The senior year requirement of a Bioengineering Design Project or research"))
			#Upper Division Biology Elective
			bioelec={'CHEM.130':'Chem 130desi', 'CHEM.135':'Chem 135', 'INTEGBI.115':'IB 115', 'INTEGBI.127':'IB 127', 'INTEGBI.131':'IB 131', 'INTEGBI.132':'IB 132', 'INTEGBI.135':'IB 135', 'INTEGBI.148':'IB 148', 'INTEGBI.163':'IB 163', 'MCELLBI.C100A':'MCB C100A', 'MCELLBI.100B':'MCB 100B', 'MCELLBI.102':'MCB 102', 'MCELLBI.110':'MCB 110', 'MCELLBI.111':'MCB 111', 'MCELLBI.C112':'MCB C112', 'MCELLBI.130A':'MCB 130A', 'MCELLBI.132':'MCB 132', 'MCELLBI.133L':'MCB 133L', 'MCELLBI.136':'MCB 136', 'MCELLBI.140':'MCB 140', 'MCELLBI.140L':'MCB 140L', 'MCELLBI.C145':'MCB C145', 'MCELLBI.C148':'MCB C148', 'MCELLBI.150':'MCB 150', 'PLANTBI.C112':'PMB C148', 'PLANTBI.C148':'PMB C148', 'MCELLBI.C160':'MCB C160', 'NEUROSC.C160':'NeuroScience C160', 'MCELLBI.160L':'MCB 160L', 'MCELLBI.166':'MCB 166', 'PLANTBI.185':'PMB 185'}
			belec=0
			for key in bioelec:
				if key in takenClasses:
					belec+=1
			ans.append(manyChoiceReq(takenClasses, 'Upper Division Biology Elective', bioelec, "The junior year requirement of an upper division biology elective"))
			#BioE 100 or Humanities / Social Studies course with ethics content
			ethics={'ANTHRO.156B':'Anthro 156B','BIOENG.100':'BioE 100','ENGIN.125':'E 125','ESPM.161':'ESPM 161','ESPM.162':'ESPM 162','LNS.160B':'L&S 160B','PHILOS.2':'Philo 2','PHILOS.104':'Philo 104','PHIMOS.107':'Philo 107','PBHLTH.116':'Public Health 116'}
			ans.append(manyChoiceReq(takenClasses, 'Ethics Requirement', ethics, "The junior year requirement of a course with ethics content"))
			#Bioengineering Fundamentals- 2
			biofund={'BIOENG.101':'BioE 101','BIOENG.102':'BioE 102','BIOENG.104':'BioE 104','BIOENG.110':'BioE 110','BIOENG.116':'BioE 116','BIOENG.131':'BioE 131','BIOENG.150':'BioE 150'}
			fund=0
			for key in biofund:
				if key in takenClasses:
					fund+=1
			if fund>=2:
				ans.append({'reqName':'Bioengineering Fundamentals', 'reqCompleted':True, 'reqDescription':"Two classes from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Bioengineering Fundamentals', 'reqCompleted':False, 'reqDescription':"Two classes from the given list",'courseDone':[], 'courseLeft':[]})
			#Bioengineering Lab Course
			biolab={'BIOENG.22L':'BioE 22L','BIOENG.101':'BioE 101','BIOENG.115':'BioE 115','BIOENG.121L':'BioE 121L','BIOENG.C136L':'BioE C136L','BIOENG.140L':'BioE 140L','BIOENG.C144L':'BioE C144L','BIOENG.C145L':'BioE C145L','BIOENG.C145M':'BioE C145M','BIOENG.163L':'BioE 163L','BIOENG.168L':'BioE 168L'}
			lab=0
			overlap=('BIOENG.101'in takenClasses)
			simple=('BIOENG.22L'in takenClasses)
			for key in biolab:
				if key in takenClasses:
					lab+=1	
			if((not overlap) and (lab>=1))or(overlap and (lab>=2)):
				ans.append({'reqName':'Bioengineering Lab', 'reqCompleted':True, 'reqDescription':"One lab course from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Bioengineering Lab', 'reqCompleted':False, 'reqDescription':"One lab course from the given list",'courseDone':[], 'courseLeft':[]})
			#Bioengineering Topics-2
			# two off the list but the list includes the fundamentals
			biotopic={'BIOENG.111':'BioE 111','BIOENG.112':'BioE 112','BIOENG.113':'BioE 113','BIOENG.C117':'BioE C117','BIOENG.C118':'BioE C118','BIOENG.C119':'BioE C119','BIOENG.121':'BioE 121','BIOENG.C125':'BioE C125','BIOENG.132':'BioE 132','BIOENG.135':'BioE 135','BIOENG.C144':'BioE C144','BIOENG.C146':'BioE C146','BIOENG.147':'BioE 147','BIOENG.148':'BioE 148','BIOENG.151':'BioE 151','BIOENG.163':'BioE 163','BIOENG.164':'BioE C164','BIOENG.C165':'BioE C165','BIOENG.C181':'BioE C181','BIOENG.190A':'BioE 190A','BIOENG.190B':'BioE 190B','BIOENG.190C':'BioE 190C','BIOENG.190D':'BioE 190D','BIOENG.190E':'BioE 190E','BIOENG.190F':'BioE 190F','BIOENG.190G':'BioE 190G','BIOENG.190H':'BioE 190H'}
			topic=0
			for key in biotopic:
				if key in takenClasses:
					topic+=1
			if (not overlap):
				topic+=fund
				topic+=lab
				topic-=3
			else:
				topic+=fund
				topic+=lab
				topic-=4
			if topic>=2:
				ans.append({'reqName':'Bioengineering Topics', 'reqCompleted':True, 'reqDescription':"Two classes from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Bioengineering Topics', 'reqCompleted':False, 'reqDescription':"Two classes from the given list",'courseDone':[], 'courseLeft':[]})
			#Engineering Topic-1
			engtopic={'BIOENG.192':'BioE 192' ,'BIOENG.H194':'BioE H194' ,'BIOENG.196':'BioE 196' , 'CHMENG.140':'Chem E 140', 'CHMENG.141':'Chem E 141' ,'CHMENG.150A':'Chem E 150A' , 'CHMENG.150B':'Chem E 150B' , 'CHMENG.170A':'Chem E 170A' , 'CHMENG.170B':'Chem E 170B' , 'CHMENG.170L':'Chem E 170L' , 'CHMENG.171':'Chem E 171' ,'CHMENG.C178':'Chem E C178' , 'CIVENG.C30':'CE C30','MECENG.C85':'ME C85','CIVENG.130N':'CE 130N' ,'COMPSCI.61A':'CS 61A' , 'COMPSCI.61B':'CS 61B' ,'COMPSCI.61BL':'CS 61BL' ,'COMPSCI.170':'CS 170','COMPSCI.186':'CS 186','COMPSCI.191':'CS 191','PHYSICS.C191':'Physics C191' ,'ENGIN.7':'E 7', 'ENGIN.115':'E 115', 'ENGIN.170':'E 170', 'ENGIN.190':'E 190','ELENG.20N':'EE 20N','ELENG.40':'EE 40','ELENG.100':'EE 100','ELENG.105':'EE 105','ELENG.117':'EE 117','ELENG.120':'EE 120','ELENG.126':'EE 126','ELENG.129':'EE 129','ELENG.142':'EE 142','ELENG.143':'EE 143','ELENG.192':'EE 192','INDENG.162':'IEOR 162','MECENG.102B':'ME 102B','MECENG.104':'ME 104','MECENG.106':'ME 106','MECENG.109':'ME 109','MECENG.118':'ME 118','MECENG.119':'ME 119','MECENG.128':'ME 128','MECENG.132':'ME 132','MECENG.133':'ME 133', 'MECENG.167':'ME 167','MECENG.185':'ME 185','MATSCI.102':'MSE 102','MATSCI.104':'MSE 104','MATSCI.111':'MSE 111','MATSCI.113':'MSE 113','MATSCI.151':'MSE 151','NUCENG.101':'NE 101','NUCENG.107':'NE 107', 'NUCENG.170B':'NE 170B'}
			eng=0
			for key in engtopic:
				if key in takenClasses:
					eng+=1
			eng+=topic
			eng-=2
			if eng>=1:
				ans.append({'reqName':'Engineering Topic', 'reqCompleted':True, 'reqDescription':"One class from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Engineering Topic', 'reqCompleted':False, 'reqDescription':"One class from the given list",'courseDone':[], 'courseLeft':[]})
			#Technical Electives-3
			elec=eng-1
			elec+=(belec-1)
			techelec={'BIOLOGY.1B':'Bio 1B','CHEM.3B':'Chem 3B' , 'CHEM.120A':'Chem 120A','CHEM.120B': 'Chem 120B' ,'CHEM.C130':'Chem C130','MCELLBI.C100A':'MCB C100A','CHEM.130B':'Chem 130B' ,'COMPSCI.70':'CS 70' ,'MATH.55': 'Math 55','MATH.110':'Math 110' ,'MATH.118':'Math 118', 'MATH.127':'Math 127' ,'MATH.128A':'Math 128A' , 'MATH.170':'Math 170' ,  'NUSCTX.121':'NutriSci 121' , 'PHYSICS.7C': 'Physics 7C', 'PHYSICS.110A':'Physics 110A' , 'PHYSICS.112': 'Physics 112','PHYSICS.137A':'Physics 137A' , 'PHYSICS.177':'Physics 177', 'PHYSICS.C191':'Physics C191' , 'PBHLTH.143':'Public Health 143' , 'STAT.133':'Stata 133' ,'STAT.134':'Stats 134', 'INDENG.172':'IEOR 172', 'STAT.135':'Stats 135' , 'STAT.150': 'Stats 150'}
			for key in techelec:
				if key in takenClasses:
					elec+=1
			if elec>=3:
				ans.append({'reqName':'Technical Electives', 'reqCompleted':True, 'reqDescription':"Three classes from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Electives', 'reqCompleted':False, 'reqDescription':"Three classes from the given list",'courseDone':[], 'courseLeft':[]})
			return ans
		# Civil and Environmental Engineering
		elif(major=='CIVENG'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 - Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Basic Science Breadth Elective (Bio 1B or CE 70)
			ans.append(twoChoiceReq(takenClasses,'Basic Science Breadth Elective', 'BIOLOGY.1B', 'Bio 1B', 'CIVENG.70','CivEng 70', "The freshman year Basic Science Breadth Elective requirement of Bio 1B and CE 70"))
			#CE 92 - Introduction to Civil & Environmental Engineering
			ans.append(basicReq(takenClasses, 'CIVENG.92', 'CivEng 92', "The freshman year Introduction to Civil & Environmental Engineering requirement of CE 92"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Either Chem 1B: General Chemistry, OR Chem 4B General Chemistry and Quantitative Analysis OR Physics 7C: Physics for Scientists & Engineers
			science={'CHEM.1B':'Chem 1B','CHEM.4B':'Chem 4B','PHYSICS.7C':'Physics 7C'}
			ans.append(manyChoiceReq(takenClasses, 'Basic Science', science, "Either Chem 1B: General Chemistry, OR Chem 4B General Chemistry and Quantitative Analysis OR Physics 7C: Physics for Scientists & Engineers"))
			#CE C30/ME C85
			ans.append(twoChoiceReq(takenClasses,'Introduction to Solid Mechanics', 'MECENG.C85', 'MecEng C85','CIVENG.C30','CivEng C30', "The sophomore year Introduction to Solid Mechanics requirement"))
			#CE 60 - Structure & Properties of Civil Engineering Materials
			ans.append(basicReq(takenClasses, 'CIVENG.60', 'CivEng 60', "The sophomore year Structure & Properties of Civil Engineering Materials requirement of CE 60"))
			#Engineering Elective CE 11 or CE 70
			ans.append(twoChoiceReq(takenClasses,'Engineering Sophomore Elective', 'CIVENG.11', 'CivEng 11','CIVENG.70','CivEng 70', "The sophomore year Engineering Sophomore Elective requirement"))
			#CE 93 - Engineering Data Analysis
			ans.append(basicReq(takenClasses, 'CIVENG.93', 'CivEng 93', "The sophomore year Engineering Data Analysis requirement of CE 93"))
			#CE 100 - Elementary Fluid Mechanics
			ans.append(basicReq(takenClasses, 'CIVENG.100', 'CivEng 100', "The junior year Elementary Fluid Mechanics requirement of CE 100"))
			#CE 130N
			ans.append(basicReq(takenClasses, 'CIVENG.130N', 'CivEng 130N', "The junior year Mechanics of Structures requirement of CE 130N"))
			#Engineering Science Electives
			engelec={'ENGIN.115':'E 115','MECENG.40':'MecEng 40','MECENG.104':'MecEng 104'}
			ans.append(manyChoiceReq(takenClasses, 'Engineering Science Elective', engelec, "One off the following list"))
			#Elective Core (four of the following seven): CE 103 - Hydrology (Spring) CE 111 - Environmental Engineering (Fall) CE 120 - Structural Engineering (Spring) CE 155 - Transportation Systems Engineering (Spring) CE 167 - Engineering Project Management (Fall) CE 175 - Geotechnical & Geoenvironmental Engineering (Fall & Spring) CE 191 - Civil & Environmental Systems Analysis (Fall)
			elco={'CIVENG.103':'CivEng 103','CIVENG.111':'CivEng 111','CIVENG.120':'CivEng 120','CIVENG.155':'CivEng 155','CIVENG.167':'CivEng 167','CIVENG.175':'CivEng 175','CIVENG.191':'CivEng 191'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Elective Core', elco, "Elective Core (four of the following seven): CE 103 - Hydrology, CE 111 - Environmental Engineering, CE 120 - Structural Engineering, CE 155 - Transportation Systems Engineering, CE 167 - Engineering Project Management, CE 175 - Geotechnical & Geoenvironmental Engineering,CE 191 - Civil & Environmental Systems Analysis", 4))
			#CE 192 - Art & Science of Civil & Environmental Engineering Practice
			ans.append(basicReq(takenClasses, 'CIVENG.192', 'CivEng 192', "The senior year Art & Science of Civil & Environmental Engineering Practice requirement of CE 192"))
			#Engineering Electives: 15 additional units of upper-division technically oriented engineering coursework offered in the College of Engineering or in Chemical Engineering. BioE 100; CS 194, 195, C195; E 100, 110, C111, 124, 130AC, 140, 191, 193, 195, 196; EE 194, IEOR 172, 190 series; ME 106; Chem E 185.
			num=0
			notlist={'BIOENG.100', 'COMPSCI.194', 'COMPSCI.195', 'COMPSCI.C195', 'ENGIN.100', 'ENGIN.110', 'ENGIN.C111', 'ENGIN.124', 'ENGIN.130AC', 'ENGIN.140', 'ENGIN.191', 'ENGIN.193', 'ENGIN.195', 'ENGIN.196', 'ELENG.194', 'INDENG.172', 'INDENG.190A','INDENG.190B','INDENG.190C','INDENG.190D','INDENG.190E','INDENG.190F','INDENG.190G', 'MECENG.106', 'CHMENG.185'}
			for item in takenClasses:
				if((re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'COMPSCI.1\d\d',item))or(re.search(r'MATSCI.1\d\d',item)))and (not re.search(r'ENGLISH.1\d\d',item))and (item not in notlist):
					num+=units(item)
			if num>=15:
				ans.append({'reqName':'Engineering Electives', 'reqCompleted':True, 'reqDescription':"Engineering Electives: 15 additional units of upper-division technically oriented engineering coursework offered in the College of Engineering or in Chemical Engineering. BioE 100; CS 194, 195, C195; E 100, 110, C111, 124, 130AC, 140, 191, 193, 195, 196; EE 194, IEOR 172, 190 series; ME 106; Chem E 185",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Engineering Electives', 'reqCompleted':False, 'reqDescription':"Engineering Electives: 15 additional units of upper-division technically oriented engineering coursework offered in the College of Engineering or in Chemical Engineering. BioE 100; CS 194, 195, C195; E 100, 110, C111, 124, 130AC, 140, 191, 193, 195, 196; EE 194, IEOR 172, 190 series; ME 106; Chem E 185",'courseDone':[], 'courseLeft':[]})
			#Design Electives
			deselec={'CIVENG.105':'CivEng 105','CIVENG.112':'CivEng 112','CIVENG.122N':'CivEng 122N','CIVENG.122L':'CivEng 122L','CIVENG.123N':'CivEng 123N','CIVENG.123L':'CivEng 123L','CIVENG.153':'CivEng 153','CIVENG.177':'CivEng 177','CIVENG.180':'CivEng 180','CIVENG.186':'CivEng 186'}
			ans.append(manyChoiceReq(takenClasses, 'Design Elective', deselec, "One of the following"))
			return ans
		# Computational Engineering Science
		elif(major=='COENG'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#UCB Chemistry 1A
			ans.append(basicReq(takenClasses, 'CHEM.1A', 'Chem 1A', "The freshman year General Chemistry requirement"))
			#UCB Engineering 10
			ans.append(basicReq(takenClasses, 'ENGIN.10', 'E 10', "The sophomore year Engineering Design and Analysis requirement"))
			#UCB  Engineering 7
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Three science electives from the following: UCB  Physics 7C; Chemistry 1B; Chemistry 3A/L; Chemistry 3B/L; Biology 1A/L; Biology 1B; Engineering 45
			science={'PHYSICS.7C':'Physics 7C','CHEM.1B':'Chem 1B','CHEM.3A':'Chem 3A','BIOLOGY.1A':'Bio 1A','BIOLOGY.1B':'Bio 1B','ENGIN.45':'E 45','CHEM.3B':'Chem 3B'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Science Electives', science, "The sophomore year science elective requirement of three classes", 3))
			#One from the following: UCB  Math 55; Statistics 134; Math 110; Computer Science 70
			math={'MATH.55':'Math 55','STAT.134':'Stats 134','MATH.110':'Math 110','COMPSCI.70':'CS 70'}
			ans.append(manyChoiceReq(takenClasses, 'Advanced Math', math, "The sophomore year requirement of one more advanced math class"))
			#UCB  English 1A and 1B
			ans.append(twoReq(takenClasses,'English', 'ENGLISH.1A', 'English 1A','ENGLISH.1B', 'English 1B', "The freshman year English requirement of both English 1A and 1B"))
			#Engin 39B, Introduction to Computational Engineering Science (Freshman Seminar)
			ans.append(basicReq(takenClasses, 'ENGIN.39B', 'E 39B', "The freshman year Introduction to Computational Engineering Science (Freshman Seminar) requirement"))
			#Computer Science 61B, Data Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61B', 'CS 61B', "The sophomore year Programming Data Structures requirement"))
			#Math 128A, 128B, Numerical Analysis3
			ans.append(twoReq(takenClasses,'Numerical Analysis', 'MATH.128A', 'Math 128A','MATH.128B', 'Math 128B', "The junior year Numerical Analysis requirement of both Math 128A and 128B"))
			#Core Course 1-4: One course from each of four of the following eleven groups: 
			#	Bioengineering: Bio Eng 153
			#	Electrical Engineering: El Eng 100, El Eng 120, El Eng 105, El Eng 130
			#	Electromagnetics: EECS 117A, Phys 110A
			#	Engineering Economics: Engin 120
			#	Fluid Mechanics: Mec Eng 106, Chem Eng 150A, Civ Eng 100
			#	Operations Research: Engin 102, Ind Eng 160
			#	Properties of Materials: Engin 45, Mat Sci 102, Mat Sci 111
			#	Quantum Mechanics: Phys 137A
			#	Solid State Electronics: El Eng 130, Phys 141A
			#	Statics/Dynamics: Mec Eng 104, Civ Eng 130, Phys 105
			#	Thermodynamics: Mec Eng 105, Eng 115, Chem Eng 141
			core=0
			coreTaken=[]
			coreNotTaken=[]
			if ('BIOENG.153' in takenClasses):
				core+=1
				coreTaken.append('BioE 153')
			else:
				coreNotTaken.append('BioE 153')
			if ('ENGIN.120' in takenClasses):
				core+=1
				coreTaken.append('E 120')
			else:
				coreNotTaken.append('E 120')
			if ('PHYSICS.137A' in takenClasses):
				core+=1
				coreTaken.append('Physics 137A')
			else:
				coreNotTaken.append('Physics 137A')
			ee={'ELENG.100':'EE 100','ELENG.120':'EE 120','ELENG.105':'EE 105','ELENG.130':'EE 130'}
			eeDone=False
			for key in ee:
				if key in takenClasses:
					eeDone=True
					coreTaken.append(ee[key])
				else:
					coreNotTaken.append(ee[key])
			if eeDone:
				core+=1
			em={'EECS.117A':'EECS 117A','PHYSICS.110A': 'Physics 110A'}
			emDone=False
			for key in em:
				if key in takenClasses:
					emDone=True
					coreTaken.append(em[key])
				else:
					coreNotTaken.append(em[key])
			if emDone:
				core+=1
			fm={'MECENG.106':'Mec Eng 106','CHMENG.150A': 'Chem Eng 150A','CIVENG.100': 'Civ Eng 100'}
			fmDone=False
			for key in fm:
				if key in takenClasses:
					fmDone=True
					coreTaken.append(fm[key])
				else:
					coreNotTaken.append(fm[key])
			if fmDone:
				core+=1
			ore={'ENGIN.102':'E 102','INDENG.160': 'IEOR 160'}
			oreDone=False
			for key in ore:
				if key in takenClasses:
					oreDone=True
					coreTaken.append(ore[key])
				else:
					coreNotTaken.append(ore[key])
			if oreDone:
				core+=1
			pm={'ENGIN.45':'E 45', 'MATSCI.102':'Mat Sci 102','MATSCI.111': 'Mat Sci 111'}
			pmDone=False
			for key in pm:
				if key in takenClasses:
					pmDone=True
					coreTaken.append(pm[key])
				else:
					coreNotTaken.append(pm[key])
			if pmDone:
				core+=1
			ss={'ELENG.130':'EE 130','PHYSICS.141A': 'Physics 141A'}
			ssDone=False
			for key in ss:
				if key in takenClasses:
					ssDone=True
					coreTaken.append(ss[key])
				else:
					coreNotTaken.append(ss[key])
			if ssDone:
				core+=1
			sd={'MECENG.104':'Mec Eng 104','CIVENG.130': 'Civ Eng 130','PHYSICS.105': 'Physics 105'}
			sdDone=False
			for key in sd:
				if key in takenClasses:
					sdDone=True
					coreTaken.append(sd[key])
				else:
					coreNotTaken.append(sd[key])
			if sdDone:
				core+=1
			td={'MECENG.105':'Mec Eng 105','ENGIN.115': 'E 115','CHMENG.141': 'Chem Eng 141'}
			tdDone=False
			for key in td:
				if key in takenClasses:
					tdDone=True
					coreTaken.append(td[key])
				else:
					coreNotTaken.append(td[key])
			if tdDone:
				core+=1
			if core>=4:
				ans.append({'reqName':'Core Course', 'reqCompleted':True, 'reqDescription':"One course from each of four of the following eleven groups:  Bioengineering: Bio Eng 153; Electrical Engineering: El Eng 100, El Eng 120, El Eng 105, El Eng 130; Electromagnetics: EECS 117A, Phys 110A; Engineering Economics: Engin 120; Fluid Mechanics: Mec Eng 106, Chem Eng 150A, Civ Eng 100; Operations Research: Engin 102, Ind Eng 160; Properties of Materials: Engin 45, Mat Sci 102, Mat Sci 111; Quantum Mechanics: Phys 137A; Solid State Electronics: El Eng 130, Phys 141A; Statics/Dynamics: Mec Eng 104, Civ Eng 130, Phys 105; Thermodynamics: Mec Eng 105, Eng 115, Chem Eng 141",'courseDone':coreTaken, 'courseLeft':coreNotTaken})
			else:
				ans.append({'reqName':'Core Course', 'reqCompleted':False, 'reqDescription':"One course from each of four of the following eleven groups:  Bioengineering: Bio Eng 153; Electrical Engineering: El Eng 100, El Eng 120, El Eng 105, El Eng 130; Electromagnetics: EECS 117A, Phys 110A; Engineering Economics: Engin 120; Fluid Mechanics: Mec Eng 106, Chem Eng 150A, Civ Eng 100; Operations Research: Engin 102, Ind Eng 160; Properties of Materials: Engin 45, Mat Sci 102, Mat Sci 111; Quantum Mechanics: Phys 137A; Solid State Electronics: El Eng 130, Phys 141A; Statics/Dynamics: Mec Eng 104, Civ Eng 130, Phys 105; Thermodynamics: Mec Eng 105, Eng 115, Chem Eng 141",'courseDone':coreTaken, 'courseLeft':coreNotTaken})
			#CES Cluster Course 1-4
			#	Optoelectronics, Electromagnetics, and Plasmas: Electrical Engineering 117, 118, 119, 120, 121, 136, 145A; Materials Science 111; Nuclear Engineering 180; Physics 142;	Statistics 134.
			#	Bionuclear Engineering. Electrical Engineering C145B; NuclearEngineering 101, 107, 162, 167.
			#	Radiation Transport. Nuclear Engineering 101, 124, 150, 155, 162, 180.
			#	Thermodynamics and Combustion. Chemical Engineering 141; Engineering 115; Mechanical Engineering 105, 109, 140, 145, 151, 142; Materials Science 115; Physics 112.
			#	Mass and Energy Transport. Chemical Engineering 150A, 150B, 152,157, 171; Mechanical Engineering 106, 107A, 107B, 162, 165, 185;Materials Science 149, 176.
			#	Optimization. Computer Science 170, 172, 174, 188; IndustrialEngineering 131, 160, 161, 162, 166.
			#	Computational Materials Science.Engineering 45;Materials Science 102, 103; Electrical Engineering 131 or MaterialsScience 111 or Physics 141A; Materials Science 112, 113, 116, 117 (orPhysics 141B), 118, 120, 121, 122, 123, 124, 125.
			#	Mechanics. Civil Engineering 130, 131; Engineering 36, C164,Integrative Biology 135; Mechanical Engineering 104, 106, 132, 133,134, 165, 170, 175, 176, 185; Physics 105.
			#	Environmental Transport. Civil Engineering 108, 116, 173; ChemicalEngineering 171; Materials Science 149, 176.
			"""advancement"""
			cluster={'oep':0,'be':0,'rt':0,'tc':0,'met':0,'o':0,'cms':0,'m':0,'et':0}
			oep={'ELENG.117':'EE 117', 'ELENG.118':'EE 118', 'ELENG.119':'EE 119', 'ELENG.120':'EE 120', 'ELENG.121':'EE 121', 'ELENG.136':'EE 136', 'ELENG.145A':'EE 145A', 'MATSCI.111':'MatSci 111', 'NUCENG.180':'NucEng 180','PHYSICS.142':'Physics 142','STAT.134':'Stats 134'}
			be={'ELENG.C145B':'EE C145B','NUCENG.101':'NucEng 101','NUCENG.107':'NucEng 107','NUCENG.162':'NucEng 162','NUCENG.167':'NucEng 167'}
			rt={'NUCENG.101':'NucEng 101','NUCENG.124':'NucEng 124','NUCENG.150':'NucEng 150','NUCENG.155':'NucEng 155','NUCENG.162':'NucEng 162','NUCENG.180':'NucEng 180'}
			tc={'CHMENG.141':'Chem Eng 141', 'ENGIN.115':'E 115','MECENG.105':'MecEng 105','MECENG.109':'MecEng 109','MECENG.140':'MecEng 140','MECENG.145':'MecEng 145','MECENG.151':'MecEng 151','MECENG.142':'MecEng 142', 'MATSCI.115':'MatSci 115','PHYSICS.112':'Physics 112'}
			met={'CHMENG.150A':'ChemEng 150A','CHMENG.150B':'ChemEng 150B','CHMENG.152':'ChemEng 152','CHMENG.157':'ChemEng 157','CHMENG.171':'ChemEng 171','MECENG.106':'MecEng 106','MECENG.107A':'MecEng 107A','MECENG.107B':'MecEng 107B','MECENG.162':'MecEng 162','MECENG.165':'MecEng 165','MECENG.185':'MecEng 185', 'MATSCI.149':'MatSci 149','MATSCI.176':'MatSci 176'}
			o={'COMPSCI.170':'CompSci 170','COMPSCI.172':'CompSci 172','COMPSCI.174':'CompSci 174','COMPSCI.188':'CompSci 188','INDENG.131':'IndEng 131','INDENG.160':'IndEng 160','INDENG.161':'IndEng 161','INDENG.162':'IndEng 162','INDENG.166':'IndEng 166'}
			cms={'ENGIN.45':'E 45','MATSCI.102':'MatSci 102','MATSCI.103':'MatSci 103','ELENG.131':'EE 131', 'MATSCI.111':'MatSci 111', 'PHYSICS.141A':'Physics 141A', 'PHYSICS.141B':'Physics 141B','MATSCI.112':'MatSci 112','MATSCI.113':'MatSci 113','MATSCI.116':'MatSci 116','MATSCI.117':'MatSci 117','MATSCI.118':'MatSci 118','MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.124':'MatSci 124','MATSCI.125':'MatSci 125'}
			m={'CIVENG.130':'CivEng 130','CIVENG.131':'CivEng 131','ENGIN.36':'E 36','ENGIN.C164':'E C164','INTEGBI.135':'IB 135','PHYSICS.105':'Physics 105','MECENG.104':'MecEng 104', 'MECENG.106':'MecEng 106','MECENG.132':'MecEng 132','MECENG.133':'MecEng 133','MECENG.134':'MecEng 134','MECENG.165':'MecEng 165','MECENG.170':'MecEng 170','MECENG.175':'MecEng 175','MECENG.176':'MecEng 176','MECENG.185':'MecEng 185'}
			et={'CIVENG.108':'CivEng 108','CIVENG.116':'CivEng 116','CIVENG.173':'CivEng 173','CHMENG.171':'ChemE 171','MATSCI.149':'MatSci 149','MATSCI.176':'MatSci 176'}
			clusterTaken=[]
			clusterNotTaken=[]
			for key in oep:
				if (key in takenClasses):
					cluster['oep']=cluster['oep']+1
					clusterTaken.append(oep[key])
				else:
					clusterNotTaken.append(oep[key])
			for key in be:
				if (key in takenClasses):
					cluster['be']=cluster['be']+1
					clusterTaken.append(be[key])
				else:
					clusterNotTaken.append(be[key])
			for key in rt:
				if (key in takenClasses):
					cluster['rt']=cluster['rt']+1
					clusterTaken.append(rt[key])
				else:
					clusterNotTaken.append(rt[key])
			for key in tc:
				if (key in takenClasses):
					cluster['tc']=cluster['tc']+1
					clusterTaken.append(tc[key])
				else:
					clusterNotTaken.append(tc[key])
			for key in met:
				if (key in takenClasses):
					cluster['met']=cluster['met']+1
					clusterTaken.append(met[key])
				else:
					clusterNotTaken.append(met[key])
			for key in o:
				if (key in takenClasses):
					cluster['o']=cluster['o']+1
					clusterTaken.append(o[key])
				else:
					clusterNotTaken.append(o[key])
			for key in cms:
				if (key in takenClasses):
					cluster['cms']=cluster['cms']+1
					clusterTaken.append(cms[key])
				else:
					clusterNotTaken.append(cms[key])
			for key in m:
				if (key in takenClasses):
					cluster['m']=cluster['m']+1
					clusterTaken.append(m[key])
				else:
					clusterNotTaken.append(m[key])
			for key in et:
				if (key in takenClasses):
					cluster['et']=cluster['et']+1
					clusterTaken.append(et[key])
				else:
					clusterNotTaken.append(et[key])
			if (cluster['oep']>=4 or cluster['be']>=4 or cluster['rt']>=4 or cluster['tc']>=4 or cluster['met']>=4 or cluster['o']>=4 or cluster['cms']>=4 or cluster['m']>=4 or cluster['et']>=4 ):
				ans.append({'reqName':'Cluster Courses', 'reqCompleted':True, 'reqDescription':"CES Cluster Course: Each student must complete four courses from one of the given clusters: Optoelectronics, Electromagnetics, and Plasmas: Electrical Engineering 117, 118, 119, 120, 121, 136, 145A; Materials Science 111; Nuclear Engineering 180; Physics 142;Statistics 134. Bionuclear Engineering: Electrical Engineering C145B; Nuclear Engineering 101, 107, 162, 167. Radiation Transport: Nuclear Engineering 101, 124, 150, 155, 162, 180. Thermodynamics and Combustion: Chemical Engineering 141; Engineering 115; Mechanical Engineering 105, 109, 140, 145, 151, 142; Materials Science 115; Physics 112. Mass and Energy Transport: Chemical Engineering 150A, 150B, 152,157, 171; Mechanical Engineering 106, 107A, 107B, 162, 165, 185;Materials Science 149, 176. Optimization: Computer Science 170, 172, 174, 188; Industrial Engineering 131, 160, 161, 162, 166. Computational Materials Science: Engineering 45;Materials Science 102, 103; Electrical Engineering 131 or Materials Science 111 or Physics 141A; Materials Science 112, 113, 116, 117 (or Physics 141B), 118, 120, 121, 122, 123, 124, 125.  Mechanics: Civil Engineering 130, 131; Engineering 36, C164,Integrative Biology 135; Mechanical Engineering 104, 106, 132, 133,134, 165, 170, 175, 176, 185; Physics 105. Environmental Transport: Civil Engineering 108, 116, 173; Chemical Engineering 171; Materials Science 149, 176.**Alternative Cluster courses can be considered by advisors**",'courseDone':clusterTaken, 'courseLeft':clusterNotTaken})
			else:
				ans.append({'reqName':'Cluster Courses', 'reqCompleted':False, 'reqDescription':"CES Cluster Course: Each student must complete four courses from one of the given clusters: Optoelectronics, Electromagnetics, and Plasmas: Electrical Engineering 117, 118, 119, 120, 121, 136, 145A; Materials Science 111; Nuclear Engineering 180; Physics 142;Statistics 134. Bionuclear Engineering: Electrical Engineering C145B; Nuclear Engineering 101, 107, 162, 167. Radiation Transport: Nuclear Engineering 101, 124, 150, 155, 162, 180. Thermodynamics and Combustion: Chemical Engineering 141; Engineering 115; Mechanical Engineering 105, 109, 140, 145, 151, 142; Materials Science 115; Physics 112. Mass and Energy Transport: Chemical Engineering 150A, 150B, 152,157, 171; Mechanical Engineering 106, 107A, 107B, 162, 165, 185;Materials Science 149, 176. Optimization: Computer Science 170, 172, 174, 188; Industrial Engineering 131, 160, 161, 162, 166. Computational Materials Science: Engineering 45;Materials Science 102, 103; Electrical Engineering 131 or Materials Science 111 or Physics 141A; Materials Science 112, 113, 116, 117 (or Physics 141B), 118, 120, 121, 122, 123, 124, 125.  Mechanics: Civil Engineering 130, 131; Engineering 36, C164,Integrative Biology 135; Mechanical Engineering 104, 106, 132, 133,134, 165, 170, 175, 176, 185; Physics 105. Environmental Transport: Civil Engineering 108, 116, 173; Chemical Engineering 171; Materials Science 149, 176.**Alternative Cluster courses can be considered by advisors**",'courseDone':clusterTaken, 'courseLeft':clusterNotTaken})
			#Engineering 170A, 170B, Introduction to Modeling and Simulation
			ans.append(twoReq(takenClasses, 'Introduction to Modeling and Simulation', 'ENGIN.170A', 'E 170A', 'ENGIN.170B', 'E 170B', "Senior year requirement of both Engineering 170A and 170B"))
			#Engin 180A, Computational Engineering Science: Modeling, Simulation
			ans.append(basicReq(takenClasses, 'ENGIN.180A', 'E 180A', "Senior year Computational Engineering Science: Modeling and Simulation requirement of Engineering 180A"))
			#Computational Project Course
			project={'ENGIN.180B':'E 180B','ENGIN.177':'E 177','BIOENG.143':'BioE 143','INDENG.131':'IEOR 131','INDENG.162':'IEOR 162','MECENG.135':'MecEng 135','MECENG.145':'MecEng 145','MECENG.180':'MecEng 180','NUCENG.155':'NucEng 155','MATSCI.215':'MatSci 215'}
			ans.append(manyChoiceReq(takenClasses, 'Computational Project Course', project, "Senior year Project requirement of one course"))
			#Engineering 190, Technical Communication
			ans.append(basicReq(takenClasses, 'ENGIN.190', 'E 190', "Senior year Technical Communication requirement of Engineering 190"))
			return ans
		# Energy Engineering
		elif(major=='ENENG'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Engineering 93-Energy Engineering Seminar
			ans.append(basicReq(takenClasses, 'ENGIN.93', 'E 93', "Part of the freshman year requirement of Engineering 93-Energy Engineering Seminar"))
			#CE C30/ME C85-Introduction to Solid Mechanics
			ans.append(twoChoiceReq(takenClasses,"Introduction to Solid Mechanics", 'CHMENG.C30', 'CE C30', 'MECENG.C85', 'ME C85', "The sophomore year Introduction to Solid Mechanics requirement of either CE C30 or ME C85"))
			#Energy and Resources Group100-Energy and Society (First H/SS course)
			ans.append(basicReq(takenClasses, 'ENERES.100', 'Energy and Society', "Part of the sophomore year requirement of Energy and Resources Group100-Energy and Society"))
			#Engineering Prep Course 1 and 2
			#One must be from List A; the second from list A or B. List A: El Eng 40 (or 100) or Engin 45; List B: Civ Eng 11 or 70, Chem 1B or 3A; El Eng 20N; Physics 7C
			a={'ELENG.40':'EE 40','ELENG.100':'EE 100','ENGIN.45':'E 45'}
			b={'CIVENG.11':'Civ Eng 11','CIVENG.70':'Civ Eng 70','CHEM.1B':'Chem 1B','CHEM.3A':'Chem 3A','ELENG.20N':'EE 20N','PHYSICS.7C':'Physics 7C'}
			takenA=[]
			notTakenA=[]
			for key in a:
				if key in takenClasses:
					takenA.append( a[key])
				else:
					notTakenA.append(a[key])
			takenB=[]
			notTakenB=[]
			for key in b:
				if key in takenClasses:
					takenB.append(b[key])
				else:
					notTakenB.append(b[key])
			if ((len(takenA)>=2)or ((len(takenA)>=1) and (len(takenB)>=1))):
				ans.append({'reqName':'Engineering Prep Course 1 and 2', 'reqCompleted':True, 'reqDescription':"One must be from List A; the second from list A or B. List A: El Eng 40 (or 100) or Engin 45; List B: Civ Eng 11 or 70, Chem 1B or 3A; El Eng 20N; Physics 7C",'courseDone':(takenA+takenB), 'courseLeft':(notTakenA+notTakenB)})
			else:
				ans.append({'reqName':'Engineering Prep Course 1 and 2', 'reqCompleted':False, 'reqDescription':"One must be from List A; the second from list A or B. List A: El Eng 40 (or 100) or Engin 45; List B: Civ Eng 11 or 70, Chem 1B or 3A; El Eng 20N; Physics 7C",'courseDone':(takenA+takenB), 'courseLeft':(notTakenA+notTakenB)})
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Mechanical Engineering 40-Thermodynamics or Engineering 115-Engineering Thermodynamics
			ans.append(twoChoiceReq(takenClasses,"Thermodynamics", 'MECENG.40', 'ME 40', 'ENGIN.115', 'E 115', "The sophomore year Thermodynamics requirement of either ME 40 or E 115"))
			#CE 100-Elementary Fluid Mechanics or ME 106-Fluid Mechanics
			ans.append(twoChoiceReq(takenClasses,"Fluid Mechanics", 'MECENG.106', 'ME 106', 'CHMENG.100', 'CE 100', "The junior year Fluid Mechanics requirement of either ME 106 or CE 100"))
			#Economics Course. Choose one from the following list: Civ Eng 156, ENG 120; Env Econ *147, *C151, *153,*154; ERG C180; *ESPM 102D; *PEIS 101 or an Economics course chosen in consultation with faculty adviser.
			econ={'CIVENG.156':'Civ Eng 156','ENGIN.120':' E 120','ENVECON.147':'Env Econ 147','ENVECON.C151':'Env Econ C151','ENVECON.153':'Env Econ 153','ENVECON.154':'Env Econ 154','ENERES.C180':'ERG C180','ESPM.102D':'ESPM 102D','POLECON.101':'PEIS 101'}
			"""advancement"""
			ans.append(manyChoiceReq(takenClasses, 'Economics Course', econ, "The junior year requirement of an Economics Course **Can be any Economics course chosen in consultation with faculty adviser**"))
			#Elec. Eng. 137A-Introduction to Electric Power Systems
			ans.append(basicReq(takenClasses, 'ELENG.137A', 'EE 137A', "The junior year Introduction to Electric Power Systems requirement"))
			#Math/Stat/Analysis Course. Choose one from the following list: Civ Eng 93, Comp Sci 70, Engin 117, IEOR 172, Math 55 or Stat 134
			math={'CIVENG.93':'Civ Eng 93','COMPSCI.70':'Comp Sci 70','ENGIN.117':'E 117','INDENG.172':'IEOR 172','MATH.55':'Math 55','STAT.134':'Stat 134'}
			ans.append(manyChoiceReq(takenClasses, 'Math/Stat/Analysis Course', math, "The junior year requirement of a Math/Stat/Analysis Course"))
			#ME 109-Heat Transfer
			ans.append(basicReq(takenClasses, 'MECENG.109', 'ME 109', "The junior year Heat Transfer requirement"))
			#MSE 136-Materials in Energy Technologies
			ans.append(basicReq(takenClasses, 'MATSCI.136', 'MSE 136', "The junior year Materials in Energy Technologies requirement"))
			#Nuc Eng 161-Nuclear Power Engineering
			ans.append(basicReq(takenClasses, 'NUCENG.161', 'NucE 161', "The junior year Nuclear Power Engineering requirement"))
			#CE 108-Air Pollutant Emissions and Control or CE 111-Environmental Engineering
			ans.append(twoChoiceReq(takenClasses, 'Environment', 'CHMENG.108', 'CE 108', 'CHMENG.111', 'CE 111',"The senior year Air Pollutant Emissions and Control or Environmental Engineering requirement"))
			#CE 107-Climate Change Mitigation or Geography 142-Climate Dynamics
			ans.append(twoChoiceReq(takenClasses, 'Climate', 'CHMENG.107', 'CE 107', 'GEOG.142', 'Geography 142',"The senior year Climate requirement of one of two classes"))
			#Engineering 194-Research Capstone Course
			ans.append(basicReq(takenClasses, 'ENG.194', 'E 194', "The senior year Research Capstone Course requirement"))
			#Elec. Eng. 134-Fundamentals of Photovoltaic Devices
			ans.append(basicReq(takenClasses, 'ELENG.134', 'EE 134', "The senior year Fundamentals of Photovoltaic Devices requirement"))
			#Sustainability Course. Choose one from the following list: Civ Eng 111, 113N, 115; City & Reg. Planning *119; ERG 101.
			sustain={'CIVENG.111':'CivEng 111','CIVENG.113N':'CivEng 113N','CIVENG.115':'CivEng 115','CYPLAN.119':'City & Reg. Planning 119','ENERES.101':'ERG 101'}
			#Technical elective to be chose in consultation with faculty adviser
			"""advancement"""
			ans.append({'reqName':'Technical elective', 'reqCompleted':True, 'reqDescription':"Can be any agreed upon class with your advisor so we will assume that this requirement is fulfilled because we have no way of checking",'courseDone':[], 'courseLeft':[]})
			return ans
		# Engineering Math and Statistics
		elif(major=='ENGMS'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Two lower division courses in engineering, mathematics, or statistics, chosen in consultation with your faculty advisor; options include CS 61A, CS 61B, CS 61C, CS 70, CE C30/ME C85, E7, E28, E 45, Math 55, but other courses may also be used. Courses used to satisfy the two computer science course requirement may NOT also be for lower division technical electives. They can only be used to complete one requirement.
			tech={'COMPSCI.61A':'CompSci 61A','COMPSCI.61B':'CompSci 61B','COMPSCI.61C':'CompSci 61C','COMPSCI.70':'CompSci 70','CHMENG.C30':'ChemE C30','MECENG.C85':'MecE C85','ENGIN.7':'E 7','ENGIN.28':'E 28','ENGIN.45':'E 45','MATH.55':'Math 55'}
			techTaken=[]
			techNotTaken=[]
			csone=False
			cstwo=('ENGIN.177' in takenClasses)
			for key in tech:
				if (key in takenClasses):
					if ((key in ['COMPSCI.61A','ENGIN.7'])and (not csone)):
						csone=True
						techTaken.append(tech[key]+' (used for Introduction to Applied Computing requirement)')
					elif (key in ['COMPSCI.61B'] and (not cstwo)):
						cstwo=True
						techTaken.append(tech[key]+' (used for Second Computer Science Course requirement)')
					else:
						techTaken.append(tech[key])
				else:
					techNotTaken.append(tech[key])
			"""advancement"""
			if('ENGIN.177' in takenClasses) and ('COMPSCI.61B' in takenClasses):
				techTaken.append('E 177')
			print len(techTaken)
			if((len(techTaken)>=4)or (((not csone)or (not cstwo))and (len(techTaken)>=3)) or ((not csone) and (not cstwo) and (len(techTaken)>=2))):
				ans.append({'reqName':'Lower Division Technical Electives', 'reqCompleted':True, 'reqDescription':"Part of the freshman and sophmore year Technical elective requirement of two classes **Can be other cclasses agreed upon with advisor**",'courseDone':techTaken, 'courseLeft':techNotTaken})
			else:
				ans.append({'reqName':'Lower Division Technical Electives', 'reqCompleted':False, 'reqDescription':"Part of the freshman and sophmore year Technical elective requirement of two classes **Can be other cclasses agreed upon with advisor**",'courseDone':techTaken, 'courseLeft':techNotTaken})
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Second Computer Science Course (E177-Advanced Programming with MATLAB or CS 61B-Data Sturctures)
			ans.append(twoChoiceReq(takenClasses,'Second Computer Science Course', 'ENGIN.177', 'ME 177', 'COMPSCI.61B', 'CompSci 61B', "The sophomore year computer science requirement of E177 or CS 61B"))
			#Mathematics 110-Linear Algebra
			ans.append(basicReq(takenClasses, 'MATH.100', 'Math 100', "The junior year Linear Algebra requirement"))
			#Mathematics 104-Introduction to Analysis
			ans.append(basicReq(takenClasses, 'MATH.104', 'Math 104', "The junior year Introduction to Analysis requirement"))
			#Mathematics 105-Second course in Analysis or Mathematics 185-Introduction to Theory of Probability
			ans.append(twoChoiceReq(takenClasses,'Mathematics', 'MATH.105', 'Math 105', 'MATH.185', 'Math 185', "The junior year requirement of Math 105 or 185"))
			#Mathematics 128A-Numerical Analysis
			ans.append(basicReq(takenClasses, 'MATH.128A', 'Math 128A', "The junior year Numerical Analysis requirement"))
			#Statistics 134-Concepts of Probability
			ans.append(basicReq(takenClasses, 'STAT.134', 'Stats 134', "The junior year Concepts of Probability requirement"))
			#Technical electives must include 16 units of upper division engineering courses, selected with the help of your faculty adviser in order to provide depth in an area of engineering with high mathematical content--typically, most of these courses will come from a single engineering department, but courses that complement each other from different departments are also permissible. NOTE: IEOR 172 is an alternate course to Statistics 134. Students may not receive credit for both Statistics 134 and IEOR 172. IEOR 172 cannot be used to fulfill engineering unit requirements; it can only be used as a substitution for Stat 134.
			#Three additional upper division technical courses as follows: One in mathematics, one in statistics, and one from either math or statistics from among: Math 105, 113, 118, 123, 125A, 126, 130, 135, 140, 142, 170, 185, 189, and E117; Statistics 135, 150, 151A, 151B, 152, 153, 154, 157, 158.
			math=0
			stats=0
			math={'MATH.105':'Math 105','MATH.113':'Math 113','MATH.118':'Math 118','MATH.123':'Math 123','MATH.125A':'Math 125A','MATH.126':'Math 126','MATH.130':'Math 130','MATH.135':'Math 135','MATH.140':'Math 140','MATH.142':'Math 142','MATH.170':'Math 170','MATH.185':'Math 185','MATH.189':'Math 189','ENGIN.117':'E 117'}
			stats={'STAT.135':'Stats 135','STAT.150':'Stats 150','STAT.151A':'Stats 151A','STAT.151B':'Stats 151B','STAT.152':'Stats 152','STAT.153':'Stats 153','STAT.154':'Stats 154','STAT.157':'Stats 157','STAT.158':'Stats 158'}
			upperTaken=[]
			upperNotTaken=[]
			for key in  math:
				if (key in takenClasses):
					if ((key is 'MATH.105') and ('MATH.185' in takenClasses)):
						math+=1
						upperTaken.append(math[key])
					elif (key is 'MATH.105'):
						upperTaken.append(math[key])
					elif (key is 'MATH.185'):
						upperTaken.append(math[key])
					else:
						math+=1
						upperTaken.append(math[key])
				else:
					upperNotTaken.append(math[key])
			for key in stats:
				if (key in takenClasses):
					stats+=1
					upperTaken.append(stats[key])
				else:
					upperNotTaken.append(stats[key])
			"""advancement"""
			if(math>=1 and stats>=1 and (math>1 or stats>1)):
				ans.append({'reqName':'Upper Division Technical Courses', 'reqCompleted':True, 'reqDescription':"Three additional upper division technical courses as follows: One in mathematics, one in statistics, and one from either math or statistics from among: Math 105, 113, 118, 123, 125A, 126, 130, 135, 140, 142, 170, 185, 189, and E117; Statistics 135, 150, 151A, 151B, 152, 153, 154, 157, 158.",'courseDone':upperTaken, 'courseLeft':upperNotTaken})
			else:
				ans.append({'reqName':'Upper Division Technical Courses', 'reqCompleted':False, 'reqDescription':"Three additional upper division technical courses as follows: One in mathematics, one in statistics, and one from either math or statistics from among: Math 105, 113, 118, 123, 125A, 126, 130, 135, 140, 142, 170, 185, 189, and E117; Statistics 135, 150, 151A, 151B, 152, 153, 154, 157, 158.",'courseDone':upperTaken, 'courseLeft':upperNotTaken})
			return ans
		# Engineering Physics
		elif(major=='ENGP'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Chemistry 1B-General Chemistry or Chemistry 4B-General Chemistry
			ans.append(twoChoiceReq(takenClasses,'General Chemistry', 'CHEM.1B', 'Chem 1B', 'CHEM.4B', 'Chem 4B', "The freshman year requirement of General Chemistry"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Two courses from the following lower division technical electives: Astronomy 7A, 7B; Biology 1A, 1B; CE C30/ME C85; Chemistry 3A; E 45; EE 40 (or 100);
			lower={'ASTRON.7A':'Astronomy 7A','ASTRON.7B':'Astronomy 7B','BIOLOGY.1A':'Biology 1A','BIOLOGY.1B':'Biology 1B','CHMENG.C30':'CE C30','MECENG.C85':'ME C85','CHEM.3SA':'Chemistry 3A','ENGIN.45':'E 45','ELENG.40':'EE 40','ELENG.100':'EE 100'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Lower Division Technical Electives', lower, "The sophomore year lower division technical elective requirement of two classes", 2))
			#15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K.
			num=0
			for item in takenClasses:
				if ((('ENG' in item)or ('COMPSCI' in item)or('MATSCI'in item)or ('NSE' in item))and (not (('ENGLISH' in item)or ('.24' in item)or ('.39' in item)or ('.84' in item)or ('BIOENG.100' in item)or ('COMPSCI.C79' in item)or ('COMPSCI.195' in item)or ('COMPSCI.H195' in item)or ('ENGIN.125' in item)or ('ENGIN.130AC' in item)or ('ENGIN.140' in item)or ('INDENG.172' in item)or ('INDENG.190' in item)or ('INDENG.191' in item)or ('MECENG.191AC' in item)or ('MECENG.190K' in item)or ('MECENG.191K' in item)))):
					num+=units(item)
			if (num>=15):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K.",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K."+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#A minimum of 14 units of upper division physics;
			num=0
			for item in takenClasses:
				if(re.match(r'PHYSICS.1\d\d',item)):
					num+=units(item)
			if (num>=14):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"14 units of upper division physics",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"14 units of upper division physics"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#At least 40 units of approved upper division technical subjects (mathematics, statistics, science, and engineering).
			num=0
			for item in takenClasses:
				if(not re.search(r'POLSCI.1\d\d',item))and((re.search(r'PHYSICS.1\d\d',item))or(re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'MATH.1\d\d',item))or(re.search(r'SCI.1\d\d',item))or(re.search(r'STAT.1\d\d',item))or(re.search(r'CHM.1\d\d',item))or(re.search(r'CHEM.1\d\d',item))or(re.search(r'BIOLOGY.1\d\d',item))or(re.search(r'ASTRON.1\d\d',item))or(re.search(r'BIO.1\d\d',item)) or(re.search(r'BI.1\d\d',item))or (re.search(r'SC.1\d\d',item))):
					num+=units(item)
			if (num>=40):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 40 units of approved upper division technical subjects (mathematics, statistics, science, and engineering)",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 40 units of approved upper division technical subjects (mathematics, statistics, science, and engineering)"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#E 115-Engineering Thermodynamics or Physics 112-Introduction to Statistical and Thermal Physics
			ans.append(twoChoiceReq(takenClasses,"Thermal Physics", 'ENGIN.115', 'E 115', 'PHYSICS.112', 'Physics 112', "The junior year thermal physics requirement of either E 115 or Physics 112"))
			#Mathematics 104-Introduction to Analysis and Mathematics 185-Introduction to Complex Analysis, or Mathematics 121A and 121B-Mathematical Tools for the Physical Sciences
			math={'MATH.104':'Math 104','MATH.185':'Math 185','MATH.121A':'Math 121A','MATH.121B':'Math 121B'}
			mathTaken=[]
			mathNotTaken=[]
			for key in math:
				if (key in takenClasses):
					mathTaken.append(math[key])
				else:
					mathNotTaken.append(math[key])
			if ((('MATH.104' in takenClasses)and('MATH.185' in takenClasses))or(('MATH.121A' in takenClasses)and('MATH.121B' in takenClasses))):
				ans.append({'reqName':'Mathematics', 'reqCompleted':True, 'reqDescription':"Part of the junior year Mathematics requirement",'courseDone':mathTaken, 'courseLeft':mathNotTaken})
			else:
				ans.append({'reqName':'Mathematics', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':mathTaken, 'courseLeft':mathNotTaken})
			#ME 104-Engineering Mechanics or Physics 105-Analytic Mechanics
			ans.append(twoChoiceReq(takenClasses, 'Mechanics', 'MECENG.104', 'ME 104', 'PHYSICS.105', 'Physics 105', "The junior year Mechanics requirement of either ME 104 or Physics 105"))
			#Physics 137A and 137B-Quantum Mechanic
			ans.append(twoReq(takenClasses, 'Quantum Mechanics', 'PHYSICS.137A', 'Physics 137A', 'PHYSICS.137B', 'Physics 137B', "The junior year Quantum Mechanics requirement of botth Physics 137A and 137B"))
			#EE 143-Microfabrication Technology, or NE 104(6)-Nuclear Instrumentation Lab, or Physics 111A-Modern Physics and Advanced Electrical Lab
			rand={'ELENG.143':'EE 143','NUCENG.104':'NE 104','PHYSICS.111A':'Physics 111A'}
			ans.append(manyChoiceReq(takenClasses, 'Anvanced Lab', rand, "The senior year requirement of EE 143-Microfabrication Technology, or NE 104-Nuclear Instrumentation Lab, or Physics 111A-Modern Physics and Advanced Electrical Lab"))
			#ME 185-Introduction to Continuum Mechanics or ME 106-Fluid Mechanics
			ans.append(twoChoiceReq(takenClasses, 'Advanced Mechanics', 'MECENG.185', 'ME 185', 'MECENG.106', 'ME 106', "The senior year Mechanics requirement of either ME 184 or ME 106"))
			#Students opting to take EE 117 must take either EE 118 (formerly EE 119) or BioE 164. Students opting to take the Physics 110A must take 110B.
			electro={'ELENG.117':'EE 117','ELENG.118':'EE 118','BIOENG.164':'BioE 164','PHYSICS.110A':'Physics 110A','PHYSICS.110B':'Physics 110B'}
			eTaken=[]
			eNotTaken=[]
			for key in electro:
				if (key in takenClasses):
					eTaken.append(electro[key])
				else:
					eNotTaken.append(electro[key])
			if ((('ELENG.117' in takenClasses)and(('ELENG.118' in takenClasses)or('BIOENG.164' in takenClasses)))or(('PHYSICS.110A' in takenClasses)and('PHYSICS.110B' in takenClasses))):
				ans.append({'reqName':'Electromagnetism and Optics', 'reqCompleted':True, 'reqDescription':"The senior year requirement where students select between EE 117 and Physics 110A.Students opting to take EE 117 must take either EE 118 (formerly EE 119) or BioE 164. Students opting to take the Physics 110A must take 110B.",'courseDone':eTaken, 'courseLeft':eNotTaken})
			else:
				ans.append({'reqName':'Electromagnetism and Optics', 'reqCompleted':False, 'reqDescription':"The senior year requirement where students select between EE 117 and Physics 110A.Students opting to take EE 117 must take either EE 118 (formerly EE 119) or BioE 164. Students opting to take the Physics 110A must take 110B.",'courseDone':eTaken, 'courseLeft':eNotTaken})
			#MSE 111-Electric and Magnetic Properties of Materials or Physics 141A-Solid State Physics
			ans.append(twoChoiceReq(takenClasses, 'Material Physics', 'MATSCI.111', 'MSE 111', 'PHYSICS.141A', 'Physics 141A', "The senior year Materials requirement of either MSE 111 or Physics 141A"))
			return ans
		# Industrial Engineering & Operations Research
		elif(major=='INDENG'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Chem 1A/1AL
			ans.append(twoReq(takenClasses,'Chemistry', 'CHEM.1A', 'Chem 1A','CHEM.1AL', 'Chem 1AL', "The freshman year Chemistry requirement of Chem 1A and 1AL"))
			#CS (9C, 9F or 9G)
			prog={'COMPSCI.9C':'CS 9C','COMPSCI.9F':'CS 9F','COMPSCI.9G':'CS 9G'}
			ans.append(manyChoiceReq(takenClasses, 'Programming Language', prog, "Requirement of Computer Science 9C,F, or G"))
			#UCB  Engineering 7
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Engineering Breadth Electives: 9 units (minimum) Must include 9 units of coursework from the approved list: Bioe 102; CE 11, C30, 60, 70, 155; EE 40, 42,100; E 10, 28, 45, 115; MSE 111; ME, 40, C85, 132
			engbre={'BIOENG.102':'BioE 102', 'CIVENG.11':'CivEng 11','CIVENG.C30':'CivEng C30','CIVENG.60':'CivEng 60','CIVENG.70':'CivEng 70','CIVENG.155':'CivEng 155','ELENG.40':'EE 40','ELENG.42':'EE 42','ELENG.100':'EE 100','ENGIN.10':'E 10','ENGIN.28':'E 28','ENGIN.45':'E 45','ENGIN.115':'E 115', 'MATSCI.111':'MatSci 111','MECENG.40':'MecEng 40','MECENG.C85':'MecEng C85','MECENG.132':'MecEng 132'}
			engTaken=[]
			engNotTaken=[]
			num=0
			for key in engbre:
				if key in takenClasses:
					num+=units(key)
					engTaken.append(engbre[key])
				else:
					engNotTaken.append(engbre[key])
			if num>=9:
				ans.append({'reqName':'Engineering Breadth Electives', 'reqCompleted':True, 'reqDescription':"Must include 9 units of coursework from the approved list: Bioe 102; CE 11, C30, 60, 70, 155; EE 40, 42,100; E 10, 28, 45, 115; MSE 111; ME, 40, C85, 132",'courseDone':engTaken, 'courseLeft':engNotTaken})
			else:
				ans.append({'reqName':'Engineering Breadth Electives', 'reqCompleted':False, 'reqDescription':"Must include 9 units of coursework from the approved list: Bioe 102; CE 11, C30, 60, 70, 155; EE 40, 42,100; E 10, 28, 45, 115; MSE 111; ME, 40, C85, 132",'courseDone':engTaken, 'courseLeft':engNotTaken})
			#IEOR Electives : 6 courses from the list below IEOR 115, 130,140, 150, 151, 153, 166, 170, 171
			ieorelec={'INDENG.115':'IEOR 115','INDENG.130':'IEOR 130','INDENG.140':'IEOR 140','INDENG.150':'IEOR 150','INDENG.151':'IEOR 151','INDENG.153':'IEOR 153','INDENG.166':'IEOR 166','INDENG.170':'IEOR 170','INDENG.171':'IEOR 171'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'IEOR Electives', ieorelec,"6 courses from the list below IEOR 115, 130,140, 150, 151, 153, 166, 170, 171", 6))
			#E 120
			ans.append(basicReq(takenClasses, 'ENGIN.120', 'E 120', "The E 120 requirement"))
			#IEOR 172 or Stat 134
			ans.append(twoChoiceReq(takenClasses,'Probability', 'INDENG.172', 'IEOR 172','STAT.134', 'Stats 134', "The Probability requirement of IEOR 172 or Stat 134"))
			#IEOR 131
			ans.append(basicReq(takenClasses, 'INDENG.131', 'IEOR 131', "The IEOR 131 requirement"))
			#IEOR 160
			ans.append(basicReq(takenClasses, 'INDENG.160', 'IEOR 160', "The IEOR 160 requirement"))
			#IEOR 161
			ans.append(basicReq(takenClasses, 'INDENG.161', 'IEOR 161', "The IEOR 161 requirement"))
			#IEOR 162
			ans.append(basicReq(takenClasses, 'INDENG.162', 'IEOR 162', "The IEOR 162 requirement"))
			#IEOR 165
			ans.append(basicReq(takenClasses, 'INDENG.165', 'IEOR 165', "The IEOR 165 requirement"))
			#IEOR 180
			ans.append(basicReq(takenClasses, 'INDENG.165', 'IEOR 165', "The IEOR 165 requirement"))
			return ans
		# Materials Science & Engineering
		elif(major=='MATSCI'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#UCB  Engineering 7
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Chemistry 1B-General Chemistry or Chemistry 4B-General Chemistry
			ans.append(twoChoiceReq(takenClasses,'General Chemistry', 'CHEM.1B', 'Chem 1B', 'CHEM.4B', 'Chem 4B', "The freshman year requirement of General Chemistry"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Technical electives must include 24 units of course work of which a minimum of 21 units must be upper division, and The 21 units of upperdivision courses cannot include: BioE 100; CS 195, H195; Engin 125; IEOR 190 series; ME 191AC, 191K.
			num=0
			notlist={'BIOENG.100', 'COMPSCI.195','COMPSCI.H195', 'ENGIN.125',  'INDENG.190A','INDENG.190B','INDENG.190C','INDENG.190D','INDENG.190E','INDENG.190F','INDENG.190G', 'MECENG.191AC', 'MECENG.191K'}
			for item in takenClasses:
				if(not item in notlist) and(not re.search(r'POLSCI.1\d\d',item))and((re.search(r'PHYSICS.1\d\d',item))or(re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'MATH.1\d\d',item))or(re.search(r'SCI.1\d\d',item))or(re.search(r'STAT.1\d\d',item))or(re.search(r'CHM.1\d\d',item))or(re.search(r'CHEM.1\d\d',item))or(re.search(r'BIOLOGY.1\d\d',item))or(re.search(r'ASTRON.1\d\d',item))or(re.search(r'BIO.1\d\d',item)) or(re.search(r'BI.1\d\d',item))or (re.search(r'SC.1\d\d',item))):
					num+=units(item)
			if (num>=21):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"21 units of upperdivision courses cannot include: BioE 100; CS 195, H195; Engin 125; IEOR 190 series; ME 191AC, 191K **Approved by Advisor",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"21 units of upperdivision courses cannot include: BioE 100; CS 195, H195; Engin 125; IEOR 190 series; ME 191AC, 191K **Approved by Advisor"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#must include at least one (1) MSE 120 series course. 
			techtwo={'MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.125':'MatSci 125'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective Two', techtwo, "The senior year Technical Elective requirement of 3 units from the MSE 120 series course"))
			#E 115-Engineering Thermodynamics	
			ans.append(basicReq(takenClasses, 'ENGIN.115', 'E 115', "The junior year Engineering Thermodynamics requirement"))
			#MSE 102-Bonding Crystallography and Crystal Defects	
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 103-Phase Transformation and Kinetics
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The junior year Phase Transformation and Kinetics requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#E 117 Methods of Engineering Analysis
			ans.append(basicReq(takenClasses, 'ENGIN.117', 'E 117', "The junior year Methods of Engineering Analysis requirement"))
			#MSE 111-Properties of Electronic Materials
			ans.append(basicReq(takenClasses, 'MATSCI.111', 'MatSci 111', "The senior year Properties of Electronic Materials requirement"))
			#MSE 130-Experimental Materials Science	
			ans.append(basicReq(takenClasses, 'MATSCI.130', 'MatSci 130', "The senior year Experimental Materials Science requirement"))
			#MSE 112-Corrosion
			ans.append(basicReq(takenClasses, 'MATSCI.112', 'MatSci 112', "The senior year Corrosion requirement"))
			#MSE 113-Mechanical Behavior of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.113', 'MatSci 113', "The senior year Mechanical Behavior of Materials requirement"))
			#MSE 151-Polymeric Materials
			ans.append(basicReq(takenClasses, 'MATSCI.151', 'MatSci 151', "The senior year Polymeric Materials requirement"))
			return ans
		# Mechanical Engineering
		elif(major=='MECENG'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#UCB  Engineering 7
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#UCB Engineering 10
			ans.append(basicReq(takenClasses, 'ENGIN.10', 'E 10', "The sophomore year Engineering Design and Analysis requirement"))
			#E 28-Graphics Communication in Engineering
			ans.append(basicReq(takenClasses, 'ENGIN.28', 'E 28', "The sophomore year Graphics Communication in Engineering requirement"))
			#ME 40-Thermodynamics
			ans.append(basicReq(takenClasses, 'MECENG.40', 'MecEng 40', "The sophomore year Thermodynamics requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#ME 104-Engineering Mechanics II (Dynamics)
			ans.append(basicReq(takenClasses, 'MECENG.104', 'MecEng 104', "The junior year Engineering Mechanics II requirement"))
			#ME 106-Fluid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.106', 'MecEng 106', "The junior year Fluid Mechanics requirement"))
			#ME 108-Introduction to Engineering Materials
			ans.append(basicReq(takenClasses, 'MECENG.108', 'MecEng 108', "The junior year Introduction to Engineering Materials requirement"))
			#ME 109-Heat Transfer
			ans.append(basicReq(takenClasses, 'MECENG.109', 'MecEng 109', "The junior year Heat Transfer requirement"))
			#ME 132-Dynamic Systems and Feedback
			ans.append(basicReq(takenClasses, 'MECENG.132', 'MecEng 132', "The junior year Dynamic Systems and Feedback requirement"))
			#ME 102A-Experimentation and Measurement
			ans.append(basicReq(takenClasses, 'MECENG.102A', 'MecEng 102A', "The senior year Experimentation and Measurement requirement"))
			#ME 102B-Mechanical Engineering Design
			ans.append(basicReq(takenClasses, 'MECENG.102B', 'MecEng 102B', "The senior year Mechanical Engineering Design requirement"))
			#ME 107-Mechanical Engineering Laboratory
			ans.append(basicReq(takenClasses, 'MECENG.107', 'MecEng 107', "The senior year Mechanical Engineering Laboratory requirement"))
			#Tech Elec:15 units from list
			tech={'ENGIN.117':'E 117','MECENG.130':'ME130' ,'MECENG.170':'ME170' ,'ENGIN.128':'E 128','MECENG.131':'ME 131' ,'MECENG.171':'ME 171', 'ENGIN.177':'E 177','MECENG.133':'ME 133','MECENG.173':'ME 173', 'ENGIN.191':'E 191','MECENG.C134':'ME C134','MECENG.175':'ME 175','MECENG.101': 'ME 101','MECENG.135':'ME 135','MECENG.C176':'ME C176' ,'MECENG.110': 'ME 110' ,'MECENG.138':'ME 138' ,'MECENG.C180':'ME C180' , 'MECENG.C115':'ME C115','MECENG.140':'ME 140' , 'MECENG.185':'ME 185', 'MECENG.C117':'ME C117','MECENG.146':'ME 146','MECENG.190A':'ME 190A','MECENG.118': 'ME 118','MECENG.151':'ME 151','MECENG.190L':'ME 190L','MECENG.119': 'ME 119' ,'MECENG.163':'ME 163' ,'MECENG.190M':'ME 190M' ,'MECENG.120':'ME 120' ,'MECENG.164':'ME164','MECENG.190Y':'ME 190Y' , 'MECENG.122': 'ME 122','MECENG.165': 'ME 165', 'MECENG.127':'ME 127','MECENG.167':'ME 167', 'MECENG.128': 'ME 128' ,'MECENG.168':'ME 168'}
			techTaken=[]
			techNotTaken=[]
			num=0
			for key in tech:
				if key in takenClasses:
					num+=units(key)
					techTaken.append(tech[key])
				else:
					techNotTaken.append(tech[key])
			if num>=15:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Must include 15 units of coursework from the approved list of upper-divison ME courses",'courseDone':techTaken, 'courseLeft':techNotTaken})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"Must include 15 units of coursework from the approved list of upper-divison ME courses",'courseDone':techTaken, 'courseLeft':techNotTaken})
			#Tech Elec: 1 design course
			des={'ENGIN.128':'E128','MECENG.101':'ME 101','MECENG.110':'ME 110','MECENG.C117':'ME C117','MECENG.119':'ME 119','MECENG.130':'ME 130','MECENG.135':'ME 135','MECENG.146':'ME 146','MECENG.165':'ME 165','MECENG.C176':'ME C176'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', des, "One design course required from list"))
			#Tech Elec: 1 quant course
			quant={'ENGIN.117':'E 117','ENGIN.177':'E 177','MATH.128A':'MATH 128A','MECENG.120':'ME 120','MECENG.C180':'ME C180'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', quant, "One quant course required from list"))
			#Tech Elec: 18 units total
			lower={'MCELLBI.11':'MCB 11','MCELLBI.32':'MCB 32','STAT.20':'Stats 20','ENGIN.45':'E 45','CIVENG.70':'CE 70','ASTRO.7A':'Astro 7A','BIOLOGY.1A': 'Bio 1A', 'BIOLOGY.1B': 'Bio 1B', 'CHEM.1B': 'Chem 1B', 'CHEM.5': 'Chem 5'}
			for key in lower:
				if key in takenClasses:
					num+=units(key)
					techTaken.append(lower[key])
				else:
					techNotTaken.append(lower[key])
			if num>=18:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Must include 18 units of coursework from the approved list",'courseDone':techTaken, 'courseLeft':techNotTaken})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"Must include 18 units of coursework from the approved list",'courseDone':techTaken, 'courseLeft':techNotTaken})
			return ans
		# Nuclear Engineering
		elif(major=='NUCENG'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#UCB Engineering 10
			ans.append(basicReq(takenClasses, 'ENGIN.10', 'E 10', "The sophomore year Engineering Design and Analysis requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#E 115-Engineering Thermodynamics	
			ans.append(basicReq(takenClasses, 'ENGIN.115', 'E 115', "The junior year Engineering Thermodynamics requirement"))
			#E 117
			ans.append(basicReq(takenClasses, 'ENGIN.117', 'E 117', "The junior year Methods of Engineering Analysis requirement"))
			#NE 101-Nuclear Reactions and Radiation
			ans.append(basicReq(takenClasses, 'NUCENG.101', 'NucEng 101', "The junior year Nuclear Reactions and Radiation requirement"))
			#NE 150-Nuclear Reactor Theory
			ans.append(basicReq(takenClasses, 'NUCENG.150', 'NucEng 150', "The junior year Nuclear Reactor Theory requirement"))
			#NE 104-Radiation Detection Lab
			ans.append(basicReq(takenClasses, 'NUCENG.104', 'NucEng 104', "The junior year Radiation Detection Lab requirement"))
			#NE 170-Nuclear Engineering Design
			ans.append(basicReq(takenClasses, 'NUCENG.170', 'NucEng 170', "The senior year Nuclear Engineering Design requirement"))
			#32 technical elective units must include at least 17 units of upper division Nuc. Eng.Courses. 
			nereq={'NUCENG.101','NUCENG.104','NUCENG.150','NUCENG.170'}
			num=0
			for item in takenClasses:
				if((re.search(r'NUCENG.1\d\d',item))and(not item in nereq)):
					num+=units(item)
			if (num>=17):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 17 units of upper division NE courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 17 units of upper division NE courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			#Remaining technical elective units must be fulfilled by taking upper division courses in engineering and science, but cannot include BioE 100, E110, 124, 140, 193 or 195.
			num=0
			notlist={'BIOENG.100', 'ENGIN.140','ENGIN.124','ENGIN.193', 'ENGIN.195' }
			for item in takenClasses:
				if(not item in notlist) and(not re.search(r'POLSCI.1\d\d',item))and((re.search(r'PHYSICS.1\d\d',item))or(re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'MATH.1\d\d',item))or(re.search(r'SCI.1\d\d',item))or(re.search(r'STAT.1\d\d',item))or(re.search(r'CHM.1\d\d',item))or(re.search(r'CHEM.1\d\d',item))or(re.search(r'BIOLOGY.1\d\d',item))or(re.search(r'ASTRON.1\d\d',item))or(re.search(r'BIO.1\d\d',item)) or(re.search(r'BI.1\d\d',item))or (re.search(r'SC.1\d\d',item))):
					num+=units(item)
			if (num>=32):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"32 units of upperdivision courses cannot include: BioE 100, E110, 124, 140, 193 or 195 **Approved by Advisor",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"32 units of upperdivision courses cannot include:  BioE 100, E110, 124, 140, 193 or 195 **Approved by Advisor"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			return ans
		# Bioengineering and Materials Science & Engineering
		elif(major=='BIOMATSCI'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Chemistry 3A and 3AL , or Chem 112A
			if(('CHEM.3A' in takenClasses) and ('CHEM.3AL' in takenClasses)):
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':['Chem 3A', 'Chem 3AL'], 'courseLeft':['Chem 112A']})
			elif('CHEM.112A' in takenClasses):
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':['Chem 112A'], 'courseLeft':['Chem 3A', 'Chem 3AL']})
			else:
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 3A', 'Chem 3AL','Chem 112A']})
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#BioE 10
			ans.append(basicReq(takenClasses, 'BIOENG.10', 'BioE 10', "The freshman year requirement of BioE"))
			#Freshman Seminar: BioE 24
			ans.append(basicReq(takenClasses, 'BIOENG.24', 'BioE 24',  "The freshman year bioengineering seminar requirement of BioE 24"))
			#Biology 1A & 1AL , General Biology
			ans.append(twoReq(takenClasses,'General Biology', 'BIOLOGY.1A', 'Bio 1A', 'BIOLOGY.1AL', 'Bio 1AL', "The sophomore year biology requirement of both Bio 1A and 1AL"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#BioE 102-Biomechanics
			ans.append(basicReq(takenClasses, 'BIOENG.102', 'BioE 102', "The junior year Biomechanics requirement"))
			#BioE 104-Biological Transport Phenomena
			ans.append(basicReq(takenClasses, 'BIOENG.104', 'BioE 104', "The junior year Biological Transport Phenomena requirement"))
			#Chemistry 120B-Physical Chemistry OR E115
			ans.append(twoChoiceReq(takenClasses, 'Chemistry', 'CHEM.120B', 'Chem 120B', 'ENGIN.115', 'E 115', "The junior year Physical Chemistry requirement of Chem 120B or E 115"))
			#BioE110-Biomedical Physiology for Engineers or BioE 113-Stem Cells and Technologies
			ans.append(twoChoiceReq(takenClasses, 'Biomedical Technology', 'BIOENG.110', 'BioE 110', 'BIOENG.113', 'BioE 113', "The junior year Biomedical Technology requirement of BioE 110 or 113"))
			#Molecular and Cell Biology C100A Biophysical Chemistry OR MCB 102 - Survey of the Principles of Biochemistry and Molecular Biology
			ans.append(twoChoiceReq(takenClasses, 'Biochemistry', 'MCELLBI.C100A', 'MCB C100A', 'MCELLBI.102', 'MCB 102', "The junior year Biochemistry requirement of MCB C100A or 102"))
			#MSE 102-Bonding Crystallography and Crystal Defects	
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#BioE 115-Cell Biology Lab for Engineers OR MSE 130-Experimental Materials Science
			ans.append(twoChoiceReq(takenClasses, 'Labs', 'BIOENG.115', 'BioE 115', 'MATSCI.130', 'MatSci 130', "The senior year Lab requirement of BioE 115 or MatSci 130"))
			#BioE 116-Cell and Tissue Engineering, BioE C117-Structural Aspects of Biomaterials or BioE 111-Functional Biomaterials
			biomat={'BIOENG.116':'BioE 116','BIOENG.C117':'BioE C117','BIOENG.111':'BioE 111'}
			ans.append(manyChoiceReq(takenClasses, 'BioMaterials', biomat, "The senior year BioMaterials requirement of one class"))
			#BioE C118-Biological Performance of Materials	
			ans.append(basicReq(takenClasses, 'BIOENG.C118', 'BioE C118', "The senior year Biological Performance of Materials requirement"))
			#MSE 111-Properties of Electronic Materials,MSE 112-Corrosion, OR MSE 113-Mechanical Behavior of Engineering Materials, BioE 121-Introduction to Micro and Nanobiotechnology: BioMEMS OR BioE 150-Introduction to Bionanoscience and Bionanotechnology	
			matsci={'MATSCI.111':'MatSci 111','MATSCI.112':'MatSci 112','MATSCI.113':'MatSci 113'}
			ans.append(manyChoiceReq(takenClasses, 'Materials', matsci, "The senior year Materials requirement of one class"))
			ans.append(twoChoiceReq(takenClasses, 'Nanoteachnology', 'BIOENG.121', 'BioE 121', 'BIOENG.150', 'BioE 150', "The senior year Lab requirement of BioE 121 or BioE 150"))
			#MSE 151-Polymeric Materials
			ans.append(basicReq(takenClasses, 'MATSCI.151', 'MatSci 151', "The senior year Polymeric Materials requirement"))
			#Bioengineering Design Project or Research: BioE 121L, 140L, 168L, 192, H194, 196.
			biodes={'BIOENG.121L':'BioE 121L','BIOENG.140L':'BioE 140L','BIOENG.168L':'BioE 168L','BIOENG.192':'BioE 192','BIOENG.H194':'BioE H194','BIOENG.196':'BioE 196'}
			ans.append(manyChoiceReq(takenClasses, 'Bioengineering Design Project or Research', biodes, "The senior year Bioengineering Design Project or Research requirement of one class"))
			#Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement
			if ('MATSCI.111' in takenClasses) and (('MATSCI.112'in takenClasses) or ('MATSCI.113'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['MATSCI.111'], 'courseLeft':[]})
			elif('MATSCI.112' in takenClasses) and (('MATSCI.111'in takenClasses) or ('MATSCI.113'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['MATSCI.112'], 'courseLeft':[]})
			elif('MATSCI.113' in takenClasses) and (('MATSCI.111'in takenClasses) or ('MATSCI.112'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['MATSCI.113'], 'courseLeft':[]})
			elif('MATSCI.103' in takenClasses):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['MATSCI.103'], 'courseLeft':[]})
			elif ('BIOENG.111' in takenClasses) and (('BIOENG.116'in takenClasses) or ('BIOENG.C117'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.111'], 'courseLeft':[]})
			elif('BIOENG.116' in takenClasses) and (('BIOENG.111'in takenClasses) or ('BIOENG.C117'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.116'], 'courseLeft':[]})
			elif('BIOENG.C117' in takenClasses) and (('BIOENG.111'in takenClasses) or ('BIOENG.116'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.C117'], 'courseLeft':[]})
			elif('BIOENG.121' in takenClasses) and('BIOENG.150' in takenClasses):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.121'], 'courseLeft':[]})
			elif('BIOENG.H194' in takenClasses) and(('BIOENG.121L' in takenClasses)or('BIOENG.140L' in takenClasses)or('BIOENG.168L' in takenClasses)or('BIOENG.192' in takenClasses)or('BIOENG.196' in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.H194'], 'courseLeft':[]})
			elif('BIOENG.113' in takenClasses):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.113'], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':[], 'courseLeft':['BioE 111','BioE 113','BioE 116','BioE C117','BioE 121', 'BioE H194','MatSci 103','MatSci 111', 'MatSci 112', 'MatSci 113']})
			return ans
		# Electrical Engineering & Computer Sciences and Materials Science & Engineering
		elif(major=='EECSMATSCI'):
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Computer Science 61B, Data Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61B', 'CS 61B', "The sophomore year Programming Data Structures requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#EE 40-Introduction to Microelectronic Circuits
			ans.append(basicReq(takenClasses, 'ELENG.40', 'EE 40',  "The sophomore year Electrical Engineering requirement"))
			#CS 61C-Machine Structures or EE 20N-Structure and Interpretation of Systems and Signals
			ans.append(twoChoiceReq(takenClasses, 'Systems','ELENG.20N', 'EE 20N', 'COMPSCI.61C','CS 61C', "The junior year Systems requirement of EE 20N or CS 61C"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#E 115-Engineering Thermodynamics or Physics 112-Statistical and Thermal Physics
			ans.append(twoChoiceReq(takenClasses, 'Thermal Physics', 'ENGIN.115', 'E 115', 'TPHYSICS.112', 'Physics 115', "The junior year Thermal Physics requirement of E 115 or Physics 112"))
			#EE 105-Macroelectronic Devices and Circuits
			ans.append(basicReq(takenClasses, 'ELENG.105', 'EE 105', "The senior year Macroelectronic Devices and Circuits requirement"))
			#EE 126-Probability and Random Processes, Statistics 25-Introduction to Probability and Statistics for Engineers, or Statistics 134-Concepts of Probability
			probs={'ELENG.126':'EE 126','STAT.25':'Stats 25','STAT.134':'Stats 134'}
			ans.append(manyChoiceReq(takenClasses, 'Probability', probs , "The junior year Probability requirement of one of the given classes"))
			#MSE 102-Bonding Crystallography and Crystal Defects	
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 103-Phase Transformation and Kinetics
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The junior year Phase Transformation and Kinetics requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#Physics 137A-Quantum Mechanics
			ans.append(basicReq(takenClasses, 'PHYSICS.137A', 'Physics 137A', "The junior year Quantum Mechanics requirement"))
			#EE 117-Electromagnetic Fields and Waves
			ans.append(basicReq(takenClasses, 'ELENG.117', 'EE 117', "The senior year Electromagnetic Fields and Waves requirement"))
			#EE 140-Linear Integrated Circuits or EE 141-Digital Integrated Circuits
			ans.append(twoChoiceReq(takenClasses, 'Integrated Circuits', 'ELENG.140', 'EE 140', 'ELENG.141', 'EE 141', "The senior year Integrated Circuits requirement of EE 140 or 141"))
			#MSE 111-Properties of Electronic Materials
			ans.append(basicReq(takenClasses, 'MATSCI.111', 'MatSci 111', "The senior year Properties of Electronic Materials requirement"))
			#MSE 130-Experimental Materials Science	
			ans.append(basicReq(takenClasses, 'MATSCI.130', 'MatSci 130', "The senior year Experimental Materials Science requirement"))
			#Physics 141A-Solid State Physics
			ans.append(basicReq(takenClasses, 'PHYSICS.141A', 'Physics 141A', "The senior year Solid State Physics requirement of Physics 141A"))
			#Technical electives must include two courses: one course from the following: CS 150; EE 119, 143; and at least three 3 units from the MSE 120 series courses(Not 124,126,127,128,129).
			techone={'COMPSCI.150':'CS 150','ELENG.119':'EE 119','ELENG.143':'EE 143'}
			#all MSE 120 series course are 3+ units
			techtwo={'MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.125':'MatSci 125'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective One', techone, "The senior year Technical Elective requirement of CS 150, EE 119, or EE 143"))
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective Two', techtwo, "The senior year Technical Elective requirement of 3 units from the MSE 120 series course"))
			return ans
		# Electrical Engineering & Computer Sciences and Nuclear Engineering
		elif(major=='EECSNUCENG'):
			#Chemistry 1A and 1AL-General Chemistry or Chemistry 4A-General Chemistry and Quantitative Analysis
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#NE 92-Issues in Nuclear Science and Technology
			ans.append(basicReq(takenClasses, 'NUCENG.92', 'NucEng 92', "The freshman year Issues in Nuclear Science and Technology requirement"))
			#CS 61A-Structure and Interpretation of Computer Programs
			ans.append(basicReq(takenClasses, 'COMPSCI.61A', 'CS 61A', "The freshman year Structure and Interpretation of Computer Programs requirement"))
			#CS 61B-Data Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61B', 'CS 61B', "The freshman year Data Structures requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#EE 40-Introduction to Microelectronic Circuits
			ans.append(basicReq(takenClasses, 'ELENG.40', 'EE 40',  "The sophomore year Electrical Engineering requirement"))
			#EE 20N-Structure and Interpretation of Systems and Signals
			ans.append(basicReq(takenClasses, 'ELENG.20N', 'EE 20N', "The sophomore year Structure and Interpretation of Systems and Signals requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#E 115-Engineering Thermodynamics
			ans.append(basicReq(takenClasses, 'ENGIN.115', 'E 115', "The junior year Engineering Thermodynamics requirement"))
			#EE 120-Signals and Systems
			ans.append(basicReq(takenClasses, 'ELENG.120', 'EE 120', "The junior year Signals and Systems requirement"))
			#EE 126-Probability and Random Processes, Statistics 25-Introduction to Probability and Statistics for Engineers, or Statistics 134-Concepts of Probability
			probs={'ELENG.126':'EE 126','STAT.25':'Stats 25','STAT.134':'Stats 134'}
			ans.append(manyChoiceReq(takenClasses, 'Probability', probs , "The junior year Probability requirement of one of the given classes"))
			#NE 101-Nuclear Reactions and Radiation
			ans.append(basicReq(takenClasses, 'NUCENG.101', 'NucEng 101', "The junior year Nuclear Reactions and Radiation requirement"))
			#NE 150-Nuclear Reactor Theory
			ans.append(basicReq(takenClasses, 'NUCENG.150', 'NucEng 150', "The junior year Nuclear Reactor Theory requirement"))
			#NE 104-Radiation Detection Lab
			ans.append(basicReq(takenClasses, 'NUCENG.104', 'NucEng 104', "The junior year Radiation Detection Lab requirement"))
			#EE 105-Macroelectronic Devices and Circuits
			ans.append(basicReq(takenClasses, 'ELENG.105', 'EE 105', "The senior year Macroelectronic Devices and Circuits requirement"))
			#EE 117-Electromagnetic Fields and Waves
			ans.append(basicReq(takenClasses, 'ELENG.117', 'EE 117', "The senior year Electromagnetic Fields and Waves requirement"))
			#NE 170A-Nuclear Engineering Design
			ans.append(basicReq(takenClasses, 'NUCENG.170A', 'NucEng 170A', "The senior year Nuclear Engineering Design requirement"))
			#Technical Electives:
			#At least 9 units of upper-division nuclear engineering courses from NE 107, 162, 120, 124, 155, 161, 167, 175, 155, 107, 130, 180
			techne={'NUCENG.107':'NucEng 107','NUCENG.162':'NucEng 162','NUCENG.120':'NucEng 120','NUCENG.124':'NucEng 124','NUCENG.155':'NucEng 155','NUCENG.161':'NucEng 161','NUCENG.167':'NucEng 167','NUCENG.175':'NucEng 175','NUCENG.155':'NucEng 155','NUCENG.107':'NucEng 107','NUCENG.130':'NucEng 130','NUCENG.180':'NucEng 180'}
			num=0
			neTaken=[]
			neNotTaken=[]
			for key in techne:
				if key in takenClasses:
					neTaken.append(techne[key])
					num+=units(key)
				else:
					neNotTaken.append(techne[key])
			if num>=9:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 9 units of upper-division nuclear engineering courses from NE 107, 162, 120, 124, 155, 161, 167, 175, 155, 107, 130, 180",'courseDone':neTaken, 'courseLeft':neNotTaken})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 9 units of upper-division nuclear engineering courses from NE 107, 162, 120, 124, 155, 161, 167, 175, 155, 107, 130, 180."+"You have only taken"+str(num),'courseDone':neTaken, 'courseLeft':neNotTaken})
			#At least 8 units of upper division El Eng courses from  EE 118, 119, 239, 130, 131, 140, 141, 143,113, 114, 128, 134, 137A, 137B
			techee={'ELEN.118':'EE 118','ELEN.119':'EE 119','ELEN.239':'EE 239','ELEN.130':'EE 130','ELEN.131':'EE 131','ELEN.140':'EE 140','ELEN.141':'EE 141','ELEN.143':'EE 143','ELEN.113':'EE 113','ELEN.114':'EE 114','ELEN.128':'EE 128','ELEN.134':'EE 134','ELEN.137A':'EE 137A','ELEN.137B':'EE 137B'}
			num=0
			eeTaken=[]
			eeNotTaken=[]
			for key in techee:
				if key in takenClasses:
					eeTaken.append(techee[key])
					num+=units(key)
				else:
					eeNotTaken.append(techee[key])
			if num>=8:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 8 units of upper division El Eng courses from  EE 118, 119, 239, 130, 131, 140, 141, 143,113, 114, 128, 134, 137A, 137B",'courseDone':neTaken, 'courseLeft':neNotTaken})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 8 units of upper division El Eng courses from  EE 118, 119, 239, 130, 131, 140, 141, 143,113, 114, 128, 134, 137A, 137B"+"You have only taken"+str(num),'courseDone':neTaken, 'courseLeft':neNotTaken})
			return ans
		# Materials Science & Engineering and Mechanical Engineering
		elif(major=='MATMECENG'):
			#Chemistry 1A and 1AL-General Chemistry or Chemistry 4A-General Chemistry and Quantitative Analysis
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#UCB Engineering 10
			ans.append(basicReq(takenClasses, 'ENGIN.10', 'E 10', "The sophomore year Engineering Design and Analysis requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#ME 40-Thermodynamics
			ans.append(basicReq(takenClasses, 'MECENG.40', 'MecEng 40', "The sophomore year Thermodynamics requirement"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#ME 104-Engineering Mechanics II (Dynamics)
			ans.append(basicReq(takenClasses, 'MECENG.104', 'MecEng 104', "The junior year Engineering Mechanics II requirement"))
			#ME 106-Fluid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.106', 'MecEng 106', "The junior year Fluid Mechanics requirement"))
			#ME 108-Introduction to Engineering Materials
			ans.append(basicReq(takenClasses, 'MECENG.108', 'MecEng 108', "The junior year Introduction to Engineering Materials requirement"))
			#ME 109-Heat Transfer
			ans.append(basicReq(takenClasses, 'MECENG.109', 'MecEng 109', "The junior year Heat Transfer requirement"))
			#ME 132-Dynamic Systems and Feedback
			ans.append(basicReq(takenClasses, 'MECENG.132', 'MecEng 132', "The junior year Dynamic Systems and Feedback requirement"))
			#MSE 102-Bonding Crystallography and Crystal Defects	
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 103-Phase Transformation and Kinetics
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The junior year Phase Transformation and Kinetics requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#ME 102A-Experimentation and Measurement
			ans.append(basicReq(takenClasses, 'MECENG.102A', 'MecEng 102A', "The senior year Experimentation and Measurement requirement"))
			#ME 102B-Mechanical Engineering Design
			ans.append(basicReq(takenClasses, 'MECENG.102B', 'MecEng 102B', "The senior year Mechanical Engineering Design requirement"))
			#ME 107-Mechanical Engineering Laboratory
			ans.append(basicReq(takenClasses, 'MECENG.107', 'MecEng 107', "The senior year Mechanical Engineering Laboratory requirement"))
			#MSE 112-Corrosion
			ans.append(basicReq(takenClasses, 'MATSCI.112', 'MatSci 112', "The senior year Corrosion requirement"))
			#MSE 130-Experimental Materials Science	
			ans.append(basicReq(takenClasses, 'MATSCI.130', 'MatSci 130', "The senior year Experimental Materials Science requirement"))
			#A total of 12 upper division technical elective units are required. 
			num=0
			req={'MECENG.104','MECENG.106','MECENG.107','MECENG.108','MECENG.109', 'MECENG.132', 'MECENG.102A','MECENG.102B','MATSCI.102','MATSCI.103','MATSCI.104','MATSCI.112','MATSCI.130'}
			for item in takenClasses:
				if(not item in req) and(not re.search(r'POLSCI.1\d\d',item))and((re.search(r'PHYSICS.1\d\d',item))or(re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'MATH.1\d\d',item))or(re.search(r'SCI.1\d\d',item))or(re.search(r'STAT.1\d\d',item))or(re.search(r'CHM.1\d\d',item))or(re.search(r'CHEM.1\d\d',item))or(re.search(r'BIOLOGY.1\d\d',item))or(re.search(r'ASTRON.1\d\d',item))or(re.search(r'BIO.1\d\d',item)) or(re.search(r'BI.1\d\d',item))or (re.search(r'SC.1\d\d',item))):
					num+=units(item)
			if (num>=12):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 12 units of approved upper division technical subjects (mathematics, statistics, science, and engineering)",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 12 units of approved upper division technical subjects (mathematics, statistics, science, and engineering)"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#These must include 6 units of upper-division Mechanical Engineering courses, one of which must be from the following list: ME 101,110,C117,119,128,130,135,146,165,C176 or Engin 128.  
			mereq={'MECENG.104','MECENG.106','MECENG.107','MECENG.108','MECENG.109', 'MECENG.132', 'MECENG.102A','MECENG.102B'}
			metech={'MECENG.101':'MecEng 101','MECENG.110':'MecEng 110','MECENG.C117':'MecEng C117','MECENG.119':'MecEng 119','MECENG.128':'MecEng 128','MECENG.130':'MecEng 130','MECENG.135':'MecEng 135','MECENG.146':'MecEng 146','MECENG.165':'MecEng 165','MECENG.C176':'MecEng C176','ENGIN.128':'E 128'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', metech, "Technical electives must include one class from the list"))
			num=0
			for item in takenClasses:
				if((re.search(r'MECENG.1\d\d',item))and(not item in mereq)):
					num+=units(item)
			if (num>=6):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 6 units of upper-division Mechanical Engineering courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"6 units of upper-division Mechanical Engineering courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			#In addition, 3 units must be from the MSE 120 series.
			me120={'MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.125':'MatSci 125'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', me120, "3 units of the technical electives must be from the MSE 120 series"))
			#ME 108-Introduction to Engineering Materials or MSE 113-Mechanical Behavior of Engineering Materials
			ans.append(twoChoiceReq(takenClasses,'Materials', 'MECENG.108', 'MecEng 108','MATSCI.113','MatSci 113', "The junior year Materials requirement of ME 108 or MSE 113"))
			#E 28-Graphics Communication in Engineering
			ans.append(basicReq(takenClasses, 'ENGIN.28', 'E 28', "The sophomore year Graphics Communication in Engineering requirement"))
			return ans
		# Materials Science & Engineering and Nuclear Engineering
		elif(major=='MATNUCENG'):
			#Chemistry 1A and 1AL-General Chemistry or Chemistry 4A-General Chemistry and Quantitative Analysis
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#NE 92-Issues in Nuclear Science and Technology
			ans.append(basicReq(takenClasses, 'NUCENG.92', 'NucEng 92', "The freshman year Issues in Nuclear Science and Technology requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#NE 101-Nuclear Reactions and Radiation
			ans.append(basicReq(takenClasses, 'NUCENG.101', 'NucEng 101', "The junior year Nuclear Reactions and Radiation requirement"))
			#NE 150-Nuclear Reactor Theory
			ans.append(basicReq(takenClasses, 'NUCENG.150', 'NucEng 150', "The junior year Nuclear Reactor Theory requirement"))
			#NE 104-Radiation Detection Lab
			ans.append(basicReq(takenClasses, 'NUCENG.104', 'NucEng 104', "The junior year Radiation Detection Lab requirement"))
			#E 115-Engineering Thermodynamics	
			ans.append(basicReq(takenClasses, 'ENGIN.115', 'E 115', "The junior year Engineering Thermodynamics requirement"))
			#MSE 102-Bonding Crystallography and Crystal Defects	
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 103-Phase Transformation and Kinetics
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The junior year Phase Transformation and Kinetics requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#Technical electives must include at least 9 units of upper division NE courses and at least 3 units from the MSE 120 series courses.
			nereq={'NUCENG.101','NUCENG.104','NUCENG.150','NUCENG.120','NUCENG.170A'}
			num=0
			for item in takenClasses:
				if((re.search(r'NUCENG.1\d\d',item))and(not item in nereq)):
					num+=units(item)
			if (num>=9):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 9 units of upper division NE courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 9 units of upper division NE courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			me120={'MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.125':'MatSci 125'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', me120, "3 units of the technical electives must be from the MSE 120 series"))
			#MSE 111-Properties of Electronic Materials
			ans.append(basicReq(takenClasses, 'MATSCI.111', 'MatSci 111', "The senior year Properties of Electronic Materials requirement"))
			#MSE 112-Corrosion
			ans.append(basicReq(takenClasses, 'MATSCI.112', 'MatSci 112', "The senior year Corrosion requirement"))
			#MSE 113-Mechanical Behavior of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.113', 'MatSci 113', "The senior year Mechanical Behavior of Materials requirement"))
			#MSE 130-Experimental Materials Science	
			ans.append(basicReq(takenClasses, 'MATSCI.130', 'MatSci 130', "The senior year Experimental Materials Science requirement"))
			#NE 120-Nuclear Materials
			ans.append(basicReq(takenClasses, 'NUCENG.120', 'NucEng 120', "The senior year Nuclear Materials requirement"))
			#NE 170A-Nuclear Engineering Design
			ans.append(basicReq(takenClasses, 'NUCENG.170A', 'NucEng 170A', "The senior year Nuclear Engineering Design requirement"))
			return ans
		# Mechanical Engineering and Nuclear Engineering
		elif(major=='MECNUCENG'):
			#Chemistry 1A and 1AL-General Chemistry or Chemistry 4A-General Chemistry and Quantitative Analysis
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Engineering 10-Engineering Design and Analysis or Nuclear Engineering 92-Issues in Nuclear Science and Technology
			ans.append(twoChoiceReq(takenClasses,'Design', 'ENGIN.10', 'E 10','NUCENG.92','NucEng 92', "The freshman year requirement of E 10 or NucEng 92"))
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#E 28-Graphics Communication and Engineering
			ans.append(basicReq(takenClasses, 'ENGIN.28', 'E 28', "The sophomore year Graphics Communication and Engineering requirement of E 28"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#ME 40-Thermodynamics
			ans.append(basicReq(takenClasses, 'MECENG.40', 'MecEng 40', "The sophomore year Thermodynamics requirement"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The junior year Electrical Engineering requirement of one of two classes"))
			#ME 104-Engineering Mechanics II (Dynamics)
			ans.append(basicReq(takenClasses, 'MECENG.104', 'MecEng 104', "The junior year Engineering Mechanics II requirement"))
			#ME 106-Fluid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.106', 'MecEng 106', "The junior year Fluid Mechanics requirement"))
			#ME 108-Introduction to Engineering Materials
			ans.append(basicReq(takenClasses, 'MECENG.108', 'MecEng 108', "The junior year Introduction to Engineering Materials requirement"))
			#ME 109-Heat Transfer
			ans.append(basicReq(takenClasses, 'MECENG.109', 'MecEng 109', "The junior year Heat Transfer requirement"))
			#ME 132-Dynamic Systems and Feedback
			ans.append(basicReq(takenClasses, 'MECENG.132', 'MecEng 132', "The junior year Dynamic Systems and Feedback requirement"))
			#NE 101-Nuclear Reactions and Radiation
			ans.append(basicReq(takenClasses, 'NUCENG.101', 'NucEng 101', "The junior year Nuclear Reactions and Radiation requirement"))
			#NE 150-Nuclear Reactor Theory
			ans.append(basicReq(takenClasses, 'NUCENG.150', 'NucEng 150', "The junior year Nuclear Reactor Theory requirement"))
			#ME 102A-Experimentation and Measurement
			ans.append(basicReq(takenClasses, 'MECENG.102A', 'MecEng 102A', "The senior year Experimentation and Measurement requirement"))
			#ME 102B-Mechanical Engineering Design
			ans.append(basicReq(takenClasses, 'MECENG.102B', 'MecEng 102B', "The senior year 102B-Mechanical Engineering Design requirement"))
			#ME 107-Mechanical Engineering Laboratory
			ans.append(basicReq(takenClasses, 'MECENG.107', 'MecEng 107', "The senior year Mechanical Engineering Laboratory requirement"))
			#NE 104-Radiation Detection Lab
			ans.append(basicReq(takenClasses, 'NUCENG.104', 'NucEng 104', "The senior year Radiation Detection Lab requirement"))
			#NE 170A-Nuclear Engineering Design
			ans.append(basicReq(takenClasses, 'NUCENG.170A', 'NucEng 170A', "The senior year Nuclear Engineering Design requirement"))
			#Technical elective units include at least 6 units of upper-division elective Mechanical Engineering courses and 
			#6 units of upper division Nuclear Engineering courses
			#Not ME(104,106,108,109,132,102A,102B,107) NE(101,150,104,170A)
			nereq={'NUCENG.101','NUCENG.104','NUCENG.150','NUCENG.170A'}
			num=0
			for item in takenClasses:
				if((re.search(r'NUCENG.1\d\d',item))and(not item in nereq)):
					num+=units(item)
			if (num>=6):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 6 units of upper division NE courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 6 units of upper division NE courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			mereq={'MECENG.104','MECENG.106','MECENG.107','MECENG.108','MECENG.109', 'MECENG.132', 'MECENG.102A','MECENG.102B'}
			num=0
			for item in takenClasses:
				if((re.search(r'MECENG.1\d\d',item))and(not item in mereq)):
					num+=units(item)
			if (num>=6):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 6 units of upper-division Mechanical Engineering courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"6 units of upper-division Mechanical Engineering courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			
			return ans
		#Should not occur but in the case that the major given does not match
		else:
			raise MyError(major+"is not a valid major at UC Berkeley College of Engineering")

	# College of Chemistry
	elif (college=='Chemistry'):
		# College Requirements



		# Bachelor of Science Degree in Chemistry
		if(major=='BSCHEM'):


			return ans
		# Chemical Engineering
		elif(major=='CHEMENG'):


			return ans
		# Chemical Biology
		elif(major=='CHEMBIO'):



			return ans
		# Bachelor of Arts Degree in Chemistry
		elif(major=='BACHEM'):



			return ans
		# Chemical Engineering and Materials Science and Engineering
		elif(major=='CHEMMATSCI'):



			return ans
		# Chemical Engineering and Nuclear Engineering
		elif(major=='CHEMNUCENG'):
			


			return ans
		#Should not occur but in the case that the major given does not match
		else:
			raise MyError(major+"is not a valid major at UC Berkeley College of Engineering")

	# College of Natural Resources
	elif (college=='NaturalResources'):
		# College Requirements






		return ans
	# College of Letters and Sciences
	elif (college=='LettersAndSciences'):
		# College Requirements








		return ans
	# Haas School of Business
	elif (college=='Haas'):
		# College Requirements




		# Undergraduate Business Administration
		if (major=='UGBA'):

			return ans
		#Should not occur but in the case that the major given does not match
		else:
			raise MyError(major+"is not a valid major at UC Berkeley Haas School of Business")


	# College of Environmental Design
	elif (college=='EnvironmentalDesign'):
		# College Requirements











		return ans
	# Should not occur but in the case that the college given does not match
	else:
		raise MyError(college+'is not a valid college at UC Berkeley')

	return ans
	
	
	
	
## Import the python xUnit framework
import unittest

class TestRequirements(unittest.TestCase):
	def testBasicReq1(self):
		ans=basicReq([],'ELENG.20','EE 20',"Engineering class")
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testBasicReq2(self):
		ans=basicReq([],'ELENG.20','EE 20',"Engineering class")
		self.assertEqual([],ans['courseDone'])
		self.assertEqual(['EE 20'],ans['courseLeft'])
		self.assertTrue( not ans['reqCompleted'])
		self.assertEqual('EE 20',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testBasicReq3(self):
		ans=basicReq(['ELENG.20','ELENG.40'],'ELENG.20','EE 20',"Engineering class")
		self.assertEqual(['EE 20'],ans['courseDone'])
		self.assertEqual([],ans['courseLeft'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('EE 20',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testUnits1(self):
		self.assertEqual(4,units('COMPSCI.61B'))
	#def testUnits2(self):
	#	self.assertEqual(3,units('MATSCI.120'))
	def testTwoReq1(self):
		ans=twoReq([],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testTwoReq2(self):
		ans=twoReq([],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertEqual([],ans['courseDone'])
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue( not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoReq3(self):
		ans=twoReq(['ELENG.20','ELENG.40'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertEqual([],ans['courseLeft'])
		self.assertIn('EE 20',ans['courseDone'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoReq4(self):
		ans=twoReq(['ELENG.20'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 20',ans['courseDone'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoChoiceReq1(self):
		ans=twoChoiceReq([],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testTwoChoiceReq2(self):
		ans=twoChoiceReq(['ELENG.20'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 20',ans['courseDone'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoChoiceReq3(self):
		ans=twoChoiceReq(['ELENG.40'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 40',ans['courseDone'])
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoChoiceReq4(self):
		ans=twoChoiceReq(['ELENG.40','ELENG.20'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 40',ans['courseDone'])
		self.assertIn('EE 20',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoChoiceReq5(self):
		ans=twoChoiceReq([],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testManyChoiceReq1(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=manyChoiceReq([],'Electronics',listelec,"Engineering class")
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testManyChoiceReq2(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=manyChoiceReq(['ELENG.40'],'Electronics',listelec,"Engineering class")
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testManyChoiceReq3(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=manyChoiceReq(['ELENG.40','ELENG.100'],'Electronics',listelec,"Engineering class")
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseDone'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testManyChoiceReq4(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=manyChoiceReq([],'Electronics',listelec,"Engineering class")
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testDoSomeManyChoiceReq1(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=doSomeManyChoiceReq([],'Electronics',listelec,"Engineering class",2)
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testDoSomeManyChoiceReq2(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=doSomeManyChoiceReq(['ELENG.40'],'Electronics',listelec,"Engineering class",2)
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testDoSomeManyChoiceReq3(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=doSomeManyChoiceReq(['ELENG.40','ELENG.100'],'Electronics',listelec,"Engineering class",2)
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseDone'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testDoSomeManyChoiceReq4(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=doSomeManyChoiceReq([],'Electronics',listelec,"Engineering class",2)
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
		
class TestUniversity(unittest.TestCase):
	def testAC1(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertTrue( not ans[0]['reqCompleted'])
	def testAC2(self):
		ans= remainingRequirements(['GWS.100AC'], 'Engineering', 'EECS')
		self.assertTrue( ans[0]['reqCompleted'])
	def testAC3(self):
		ans= remainingRequirements(['ELENG.40','GWS.100AC'], 'Engineering', 'EECS')
		self.assertTrue( ans[0]['reqCompleted'])
	def testUnits1(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertTrue( not ans[1]['reqCompleted'])
	def testUnits1(self):
		ans= remainingRequirements(['ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20'], 'Engineering', 'EECS')
		self.assertTrue(ans[1]['reqCompleted'])

class TestEngineering(unittest.TestCase):
	def testReadComp1(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertTrue( not ans[5]['reqCompleted'])
	def testReadComp2(self):
		ans= remainingRequirements(['ENGLISH.R1A'], 'Engineering', 'EECS')
		self.assertTrue( not ans[5]['reqCompleted'])
		self.assertIn('You have completed R1A',ans[5]['reqDescription'])
	def testReadComp3(self):
		ans= remainingRequirements(['ENGLISH.R1B'], 'Engineering', 'EECS')
		self.assertTrue( not ans[5]['reqCompleted'])
		self.assertIn('You have completed R1B',ans[5]['reqDescription'])
	def testReadComp4(self):
		ans= remainingRequirements(['ENGLISH.R1B','ENGLISH.R1A'], 'Engineering', 'EECS')
		self.assertTrue(ans[5]['reqCompleted'])
	def testEECS1(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertEqual(23,len(ans))
	def testEECS2(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertTrue( not ans[14]['reqCompleted'])
		self.assertIn('You have only taken 0',ans[14]['reqDescription'])
	def testEECS3(self):
		ans= remainingRequirements(['ELENG.40','ELENG.40','ELENG.40','COMPSCI.61A','COMPSCI.61A','COMPSCI.61A'], 'Engineering', 'EECS')
		self.assertTrue(not ans[14]['reqCompleted'])
		self.assertIn('You have only taken 0',ans[14]['reqDescription'])
	def testEECS4(self):
		ans= remainingRequirements(['ELENG.140','ELENG.140','ELENG.140','COMPSCI.161A','COMPSCI.161A','COMPSCI.161A'], 'Engineering', 'EECS')
		self.assertTrue(ans[14]['reqCompleted'])
	def testBIOENG1(self):
		ans= remainingRequirements([], 'Engineering', 'BIOENG')
		self.assertEqual(5+2+20,len(ans))
	def testBIOENG2(self):
		ans= remainingRequirements([], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[9]['reqCompleted'])
	def testBIOENG3(self):
		ans= remainingRequirements(['CHEM.1A'], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[9]['reqCompleted'])
	def testBIOENG4(self):
		ans= remainingRequirements(['CHEM.1AL'], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[9]['reqCompleted'])
	def testBIOENG5(self):
		ans= remainingRequirements(['CHEM.1AL', 'CHEM.1A'], 'Engineering', 'BIOENG')
		self.assertTrue(ans[9]['reqCompleted'])
	def testBIOENG6(self):
		ans= remainingRequirements(['CHEM.4A'], 'Engineering', 'BIOENG')
		self.assertTrue(ans[9]['reqCompleted'])
	def testBIOENG7(self):
		ans= remainingRequirements([], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[10]['reqCompleted'])
	def testBIOENG8(self):
		ans= remainingRequirements(['CHEM.3A'], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[10]['reqCompleted'])
	def testBIOENG9(self):
		ans= remainingRequirements(['CHEM.3AL'], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[10]['reqCompleted'])
	def testBIOENG10(self):
		ans= remainingRequirements(['CHEM.3AL', 'CHEM.3A'], 'Engineering', 'BIOENG')
		self.assertTrue(ans[10]['reqCompleted'])
	def testBIOENG11(self):
		ans= remainingRequirements(['CHEM.112A'], 'Engineering', 'BIOENG')
		self.assertTrue(ans[10]['reqCompleted'])
	def testCIVENG1(self):
		ans= remainingRequirements([], 'Engineering', 'CIVENG')
		self.assertEqual(5+2+21,len(ans))
	def testCOENG1(self):
		ans= remainingRequirements([], 'Engineering', 'COENG')
		self.assertEqual(5+2+20,len(ans))
	def testCOENG2(self):
		ans= remainingRequirements(['BIOENG.153', 'ELENG.100','PHYSICS.110A','ENGIN.120'], 'Engineering', 'COENG')
		self.assertTrue(ans[21]['reqCompleted'])
	def testCOENG3(self):
		ans= remainingRequirements(['BIOENG.153', 'ELENG.100','PHYSICS.110A'], 'Engineering', 'COENG')
		self.assertTrue(not ans[21]['reqCompleted'])
	def testCOENG4(self):
		ans= remainingRequirements(['BIOENG.153', 'ELENG.100','PHYSICS.110A','ELENG.120'], 'Engineering', 'COENG')
		self.assertTrue(not ans[21]['reqCompleted'])
	def testENENG1(self):
		ans= remainingRequirements([], 'Engineering', 'ENENG')
		self.assertEqual(5+2+24,len(ans))
	def testENENG2(self):
		ans= remainingRequirements(['CIVENG.11','CIVENG.70'], 'Engineering', 'ENENG')
		self.assertTrue(not ans[15]['reqCompleted'])
	def testENENG3(self):
		ans= remainingRequirements(['ELENG.40','CIVENG.70'], 'Engineering', 'ENENG')
		self.assertTrue(ans[15]['reqCompleted'])
	def testENENG4(self):
		ans= remainingRequirements(['ELENG.40','ENGIN.45'], 'Engineering', 'ENENG')
		self.assertTrue(ans[15]['reqCompleted'])
	def testENGMS1(self):
		ans= remainingRequirements([], 'Engineering', 'ENGMS')
		self.assertEqual(5+2+16,len(ans))
	def testENGMS2(self):
		ans= remainingRequirements(['COMPSCI.61A','ENGIN.7','ENGIN.177','COMPSCI.61B'], 'Engineering', 'ENGMS')
		self.assertTrue(ans[12]['reqCompleted'])
	def testENGMS3(self):
		ans= remainingRequirements(['COMPSCI.61A','ENGIN.7','COMPSCI.61B'], 'Engineering', 'ENGMS')
		self.assertTrue(not ans[12]['reqCompleted'])
	def testENGMS4(self):
		ans= remainingRequirements(['COMPSCI.61A','ENGIN.177','COMPSCI.61B'], 'Engineering', 'ENGMS')
		self.assertTrue(not ans[12]['reqCompleted'])
	def testENGMS5(self):
		ans= remainingRequirements(['COMPSCI.61C','COMPSCI.70'], 'Engineering', 'ENGMS')
		self.assertTrue(ans[12]['reqCompleted'])
	def testENGP1(self):
		ans= remainingRequirements([], 'Engineering', 'ENGP')
		self.assertEqual(5+2+21,len(ans))
	def testINDENG1(self):
		ans= remainingRequirements([], 'Engineering', 'INDENG')
		self.assertEqual(5+2+18,len(ans))
	def testMATSCI1(self):
		ans= remainingRequirements([], 'Engineering', 'MATSCI')
		self.assertEqual(5+2+23,len(ans))
	def testMECENG1(self):
		ans= remainingRequirements([], 'Engineering', 'MECENG')
		self.assertEqual(5+2+24,len(ans))
	def testNUCENG1(self):
		ans= remainingRequirements([], 'Engineering', 'NUCENG')
		self.assertEqual(5+2+19,len(ans))
	def testBIOMATSCI1(self):
		ans= remainingRequirements([], 'Engineering', 'BIOMATSCI')
		self.assertEqual(5+2+28,len(ans))
	def testEECSMATSCI1(self):
		ans= remainingRequirements([], 'Engineering', 'EECSMATSCI')
		self.assertEqual(5+2+26,len(ans))
	def testEECSNUCENG1(self):
		ans= remainingRequirements([], 'Engineering', 'EECSNUCENG')
		self.assertEqual(5+2+24,len(ans))
	def testMATNUCENG1(self):
		ans= remainingRequirements([], 'Engineering', 'MATNUCENG')
		self.assertEqual(5+2+27,len(ans))
	def testMECNUCENG1(self):
		ans= remainingRequirements([], 'Engineering', 'MECNUCENG')
		self.assertEqual(5+2+27,len(ans))
	def testMATMECENG1(self):
		ans= remainingRequirements([], 'Engineering', 'MATMECENG')
		self.assertEqual(5+2+31,len(ans))

class TestChem(unittest.TestCase):
	def testBSCHEM1(self):
		self.assertEqual(1,1)



if len(sys.argv) > 1 and sys.argv[1] == "--test":
	# If we invoke with --test then we add a verbose and
	# pass the remaining arguments to unittest
	sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[2:]
	unittest.main()
else:
	main ()
