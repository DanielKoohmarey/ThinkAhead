"""
Copies courseLoad in models.py
Should find a better way to avoid duplicating code
"""

def loadCourses():
    """ Run this once to populate the database with Courses """
    output = open('courses.json','w')
    import pickle
    departments = pickle.load( open("../../courses.p", "rb") )
    
    allCourses = []
    courseEntry = {}
    pk = 1 #ID start from 1
    courseEntry['model'] = 'darsplus.courses'
    fields = {}
    output = open('courses.json','w')
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
            courses = course.split("/") # Some are in "HISTART C196W/HISTORY C196W/MEDIAST C196W/"
            for similarCourse in courses:
                currentCourse = courseEntry.copy()
                currentFields = fields.copy()
                currentCourse["pk"] = pk
                pk = pk + 1
                currentFields["courseCode"] = similarCourse
                currentFields["courseName"] = courseInfo[0]
                currentFields["courseDescription"] = courseInfo[4]
                currentFields["courseLevel"] = courseInfo[3]
                currentFields["minUnit"] = units[0]
                currentFields["maxUnit"] = units[1]
                currentFields["department"] = department
                currentCourse["fields"] = currentFields
                allCourses += [currentCourse]
    import json
    output.write(json.dumps(allCourses))
    output.close()
loadCourses()
