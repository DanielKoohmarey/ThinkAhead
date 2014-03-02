import csv
import pickle

courses = {}
with open('/home/urap/Documents/class_scraper/classes.csv', 'rb') as csvfile:
    course_reader = csv.reader(csvfile)
    for row in course_reader:
        if row[0] not in courses:
            courses[row[0]] = {}
        courses[row[0]][row[1]] = row[2:]
        
pickle.dump( courses, open( "courses.p", "wb" ) )
#To load:
#courses = pickle.load( open( "courses.p", "rb" ) )        