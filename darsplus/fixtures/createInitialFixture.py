"""
Combines all json files at current Fixture directory and output it to initial_data.json
Django is able to discover this default fixture and load iat aumatically
"""
import json
fixtureLists = ['colleges.json','courses.json']
output = open('initial_data.json','w')
allFixtures = []
for fixture in fixtureLists:
    input = open(fixture, 'r')
    inputjson = input.read()
    inputjson = eval(inputjson) #convert string into python literal
    allFixtures += inputjson
    input.close()
output.write(json.dumps(allFixtures))
output.close()
    
