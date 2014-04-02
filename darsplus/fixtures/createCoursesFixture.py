"""
Copies courseLoad in models.py
Should find a better way to avoid duplicating code
"""


# HTML Escape taken from https://wiki.python.org/moin/EscapingHtml

import cgi 

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    ",": "&#44;",
    }

def htmlEscape(text):
    return text.replace('&#44;', ',').replace('&amp;','&').replace('&apos;',"'")
    #return escape(text, html_escape_table)    

# End of HTML Escape


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
                currentFields["courseCode"] = htmlEscape(similarCourse)
                currentFields["courseName"] = htmlEscape(courseInfo[0])
                currentFields["courseDescription"] = htmlEscape(courseInfo[4])
                currentFields["courseLevel"] = htmlEscape(courseInfo[3])
                currentFields["minUnit"] = units[0]
                currentFields["maxUnit"] = units[1]
                currentFields["department"] = htmlEscape(department)
                currentCourse["fields"] = currentFields
                allCourses += [currentCourse]
                
    import json
    output.write(json.dumps(allCourses))
    output.close()


loadCourses()

