"""
Python scripts that parses collegemajor and create a valid json based on the Colleges database
"""

input = open('collegemajor','r')
output = open('colleges.json','w')

allMajors = []
major = {}
fields = {}
key = 1
prev = ''

major = {}
major["model"] = "darsplus.colleges"
for line in input:
    line = line.rstrip()
    if line == '':
        pass
    elif prev == '':
        fields["college"] = line
    else:
        currentMajor = major.copy()
        currentMajor["pk"] = key
        key = key + 1
        currentField = fields.copy()
        currentField["major"] = line
        currentMajor["fields"] = currentField
        allMajors += [currentMajor]
    prev = line

import json
output.write(json.dumps(allMajors))
output.close()
input.close()
