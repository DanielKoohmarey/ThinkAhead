# Sample server for testing of the User Counter warm-up app for CS169

# Note: initial code copied from http://www.codeproject.com/Articles/462525/Simple-HTTP-Server-and-Client-in-Python.
# Has been modified extensively.

#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import json
import sys
import tempfile
import time
import traceback
import re

from schemasByExample import Schema, SchemaValidator, schemaDocStyle



# We do not use a database in this sample implementation. Instead we store
# the table of users in memory, in a Python dictionary

class UserData:
    """
    If we were to use a database, this class provides the interface to a record.
    This would be an ActiveRecord for Ruby-on-Rails, or a Model class for Django
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.count    = 1

class UsersModel:
    """
    This is essentially the Model in a MVC architecture. It encapsulates the data,
    along with the main invariants
    """

    ## The success return code
    SUCCESS               =   1

    ## Cannot find the user/password pair in the database (for login only)
    ERR_BAD_CREDENTIALS   =  -1

    ## trying to add a user that already exists (for add only)
    ERR_USER_EXISTS       =  -2

    ## invalid user name (empty or longer than MAX_USERNAME_LENGTH) (for add, or login)
    ERR_BAD_USERNAME      =  -3

    ## invalid password name (longer than MAX_PASSWORD_LENGTH) (for add)
    ERR_BAD_PASSWORD      =  -4


    ## The maximum length of user name
    MAX_USERNAME_LENGTH = 128

    ## The maximum length of the passwords
    MAX_PASSWORD_LENGTH = 128
    
    def __init__(self):
        self._reset()


    def login(self, user, password):
        """
        This function checks the user/password in the database.

        @param user: (string) the username
        @param password: (string) the password

        * On success, the function updates the count of logins in the database.
        * On success the result is either the number of logins (including this one) (>= 1)
        * On failure the result is an error code (< 0) from the list below
           * ERR_BAD_CREDENTIALS

        """
        if user not in self.users:
            return UsersModel.ERR_BAD_CREDENTIALS

        data = self.users[user]
        if data.password != password:
            return UsersModel.ERR_BAD_CREDENTIALS
        data.count += 1
        return data.count


    def add(self, user, password):
        """
        This function checks that the user does not exists, the user name is not empty. (the password may be empty).

        @param user: (string) the username
        @param password: (string) the password

        * On success the function adds a row to the DB, with the count initialized to 1
        * On success the result is the count of logins
        * On failure the result is an error code (<0) from the list below
           * ERR_BAD_USERNAME, ERR_BAD_PASSWORD, ERR_USER_EXISTS


        """
        if user in self.users:
            return UsersModel.ERR_USER_EXISTS
        def valid_username(username):
            return username != "" and len(username) <= UsersModel.MAX_USERNAME_LENGTH

        def valid_password(password):
            return len(password) <= UsersModel.MAX_PASSWORD_LENGTH
        
        if not valid_username(user):
            return UsersModel.ERR_BAD_USERNAME
        if not valid_password(password):
            return UsersModel.ERR_BAD_PASSWORD
        
        self.users[user] = UserData(user, password)
        assert self.users[user].count == 1
        return self.users[user].count


    # Used from constructor and self test
    def _reset(self):
        self.users = dict()

    def TESTAPI_resetFixture(self):
        """
        This function is used only for testing, and should clear the database of all rows.

        It should always return SUCCESS (1)

        Used for testing
        """
        self._reset ()

# We keep a global instance of the UsersModel
g_users = UsersModel ()

class UsersController:
    """This is a controller for the main /users requests"""

    # The JSON schema expected for requests
    docRequest_login = """
    <ul>
        <li> The request must be a POST to /user/login with Content-Type "application/json"
        <li> The data in the request will be a JSON dictionary of the form given below
        <li> The two fields in the request are ASCII strings
    </ul>
    """
    schemaRequest_loginOrAdd = Schema({
        'user' : 'some_user_name',
        'password' : 'the_password'
    })


    # The JSON schema ensured for responses
    docResponse_login = """
    <ul>
       <li> The request must be a POST to /user/login or /user/add with Content-Type "application/json"
       <li> The response will be a JSON dictionary of the form given below
       <li> The errCode field is an integer with the same values as for the login/add method of UsersModel class
       <li> The count is present only if errCode is SUCCESS, and is the count of logins for the current user
       <li> The response will use HTTP status code 200 unless there is a catastrophic error outside
            the ones captured by the error codes (e.g., an unhandled exception).
            In that case a status code of 500 should be used.
    </ul>
    """
    schemaResp_loginOrAdd = Schema({
        'errCode' : 1
    }).when(errCode__eq=UsersModel.SUCCESS,
        doc='Additional fields on SUCCESS',
        update = {
            'count' : 15
        }
    )


    def do_POST(self, request):
        if request.path == "/users/login" or request.path == "/users/add":
            # Most of the code for "login" and "add" is the same
            rdata = request.getRequestData(requestName=request.path,
                                           requestSchema=UsersController.schemaRequest_loginOrAdd)
            if not rdata: return
            
            username = rdata["user"]
            password = rdata["password"]
            if request.path == "/users/login":
                rval = g_users.login(username, password)
            else:
                rval = g_users.add(username, password)
                
            if rval < 0:
                resp = {"errCode" : rval}
            else:
                resp = {"errCode" : UsersModel.SUCCESS, "count" : rval}
            request.sendResponse(data = Utils.jsonDumps(resp, objName='resp:'+request.path,
                                                  schema=UsersController.schemaResp_loginOrAdd))
        else:
            return request.send_error(404, "Unrecognized request")


class UserCounter_HTTPRequestHandler(BaseHTTPRequestHandler):
    """
    The custom HTTPRequestHandler class
    """

    # We serve the static files (client.html, etc.). This enables us to load the HTML from the
    # same domain (e.g., localhost:8000) that we send the requests to
    def do_GET(self):
        try:
            if self.path not in ["/client.html", "/client.css", "/client.js"]:
                self.send_error(404, 'file not found')
                return

            if self.path.endswith(".html"):
                mimetype='text/html'
            elif self.path.endswith(".css"):
                mimetype='text/css'
            elif self.path.endswith(".js"):
                mimetype='text/javascript'
            else:
                assert False
                
            from os import curdir, sep
            f = open(curdir + sep + self.path)
            self.sendResponse(status=200, contentType=mimetype, data = f.read())
            f.close()
        except Exception as e:
            self.send_error(500, 'error '+str(e))


    def do_POST(self):
        try:
            # A simple dispatcher based on the url path
            if self.path.find("/users/") == 0:
                UsersController().do_POST(self)
            elif self.path.find("/TESTAPI/") == 0:
                TESTAPI_Controller().do_POST(self)
            else:
                self.send_error(404, 'file not found')
                return
        except Exception as e:
            self.send_error(500, 'error '+str(e))


    ### Some generic HTTP processing functions
    def sendResponse(self, status=200, contentType='application/json', data=""):
        """
        A generic function for sending a HTTP response
        """
        self.send_response(status)
        self.send_header('Content-type', contentType)
        self.end_headers()
        if data:
            self.wfile.write(data)
    

    def getRequestData(self, requestName=None, requestSchema=None):
        """
        Return the JSON data from the request, as a dictionary
        """
        # We need to know how many bytes to read
        length = int(self.headers.getheader('content-length'))
        req = self.rfile.read(length)
    
        # The request must be a JSON request
        # Note: Python (at least) nicely tacks UTF8 information on this,
        #   we need to tease apart the two pieces.
        if not 'application/json' in self.headers.getheader('content-type').split(";"):
            self.send_error(500, 'wrong content-type on request')
            return { }
        return Utils.jsonLoads(req, objName="request:"+str(requestName),
                               schema=requestSchema) # throws on malformed JSON
    

class TESTAPI_Controller:
    """This is a controller for the special TESTAPI_ interface to the server."""

    docReq_resetFixture = """
    <ul>
    <li> The request must be a POST to /TESTAPI/resetFixture with Content-Type "application/json"
    <li> The data is an empty dictionary
    </ul>
    """

    docResp_resetFixture = """
    <ul>
    <li> Upon receiving this request the back-end should reset the databases to their empty state.
        For this project, this will consist of calling the UsersModel TESTAPI_resetFixture method.
    <li> The response should be a JSON dictionary with the contents described below
    <li> Note: <i>Real life projects do not contains such a public API.
         Instead the tests would be run on a special test database.
         We added this API so that we can test your backend easily even
         if do not have direct access to the database.</i>
    </ul>
    """
    schemaResp_resetFixture = Schema({
        'errCode': Schema(1,
                          doc="The error code",
                          valid=SchemaValidator.eq(1))
    })


    docReq_unitTests = """
    <ul>
    <li> The request must be a POST to /TESTAPI/unitTests with Content-Type "application/json"
    <li> The data is an empty dictionary
    </ul>
    """

    docResp_unitTests = """
    <ul>
    <li> Upon receiving this request the backend should run all of the unit tests,
        wait for them to complete, extract the number of tests, successes, failures,
        and the complete output of the tests and package that as part of the response
    <li> The response should contain a JSON dictionary with the fields described below
    <li> If there is a major error running the unit tests, then the response should at
         least contain the 'output' field with some error message.
         <p>
         One possible strategy for implementing this is to run the unit tests as separate
         shell command, redirecting the output to a file.
         Once the tests complete, you read the output and extract the necessary information.
    <li> Note: <i>Real life projects do not contains such a public API.
         Instead the tests would be run on a special test database.
         We added this API so that we can test your backend easily even if do not have
         direct access to the database.</i>
    </ul>
    """
    schemaResp_unitTests = Schema({
        'totalTests' : Schema(5, doc='how many unit tests were executed'),
        'nrFailed' : Schema(3, doc='how many unit tests failed'),
        'output'  : Schema(" ... ", doc='The output of running the tests')
    })

    def do_POST(self, request):
        # Note: This is added functionality to make unit testing easier
        if request.path == "/TESTAPI/resetFixture":
            g_users.TESTAPI_resetFixture()
            # To simplify the testing, make this be a JSON object
            request.sendResponse(data=Utils.jsonDumps({"errCode" : UsersModel.SUCCESS},
                                                objName="resetFixture_resp",
                                                schema=TESTAPI_Controller.schemaResp_resetFixture))
            return
        
        elif request.path == "/TESTAPI/unitTests":
            # We run the unit tests and collect the output into a temporary file
            # Conveniently, we have a Makefile target for all unit_tests
            # There are better ways of doing this in Python, but this is a more portable example

            (ofile, ofileName) = tempfile.mkstemp(prefix="userCounter")
            try:
                errMsg = ""     # We accumulate here error messages
                output = ""     # Some default values
                totalTests = 0
                nrFailed   = 0
                while True:  # Give us a way to break
                    # Find the path to the server installation
                    thisDir = os.path.dirname(os.path.abspath(__file__))
                    cmd = "make -C "+thisDir+" unit_tests >"+ofileName+" 2>&1"
                    Utils.log("Executing "+cmd)
                    code = os.system(cmd)
                    if code != 0:
                        # There was some error running the tests.
                        # This happens even if we just have some failing tests
                        errMsg = "Error running command (code="+str(code)+"): "+cmd+"\n"
                        # Continue to get the output, and to parse it

                    # Now get the output
                    try:
                        ofileFile = open(ofileName, "r")
                        output = ofileFile.read()
                        ofileFile.close ()
                    except:
                        errMsg += "Error reading the output "+traceback.format_exc()
                        # No point in continuing
                        break
                    
                    Utils.log("Got "+output)
                    # Python unittest prints a line like the following line at the end
                    # Ran 4 tests in 0.001s
                    m = re.search(r'Ran (\d+) tests', output)
                    if not m:
                        errMsg += "Cannot extract the number of tests\n"
                        break
                    totalTests = int(m.group(1))
                    # If there are failures, we will see a line like the following
                    # FAILED (failures=1)
                    m = re.search('rFAILED.*\(failures=(\d+)\)', output)
                    if m:
                        nrFailures = int(m.group(1))
                    break # Exit while

                # End while
                if errMsg:
                    Utils.log(errMsg, err=True)
                resp = { 'output' : errMsg + output,
                         'totalTests' : totalTests,
                         'nrFailed' : nrFailed }
                request.sendResponse(data = Utils.jsonDumps(resp,
                                                      objName="unitTests_resp",
                                                      schema=TESTAPI_Controller.schemaResp_unitTests))
                            
            finally:
                os.unlink(ofileName)
                
            
        else:
            return request.send_error(404, "Unrecognized request")
            

###
### Utilities
###
class Utils:
    """
    Utility functions
    """

    @staticmethod
    def log(msg, err=False):
        """
        Logging function
        """
        if err:
            msg = "ERROR: "+msg
        print msg

    @staticmethod
    def jsonDumps(data, objName="", schema=None):
        """
        Serialize data with JSON, optionally checking the schema
        @param data:
        @param objName:
        @param schema:
        @return:
        """
        if schema == None:
            msg = "No schema given for JSON serialization of "+objName
            Utils.log(msg, err=True)
            raise Exception(msg)  # Make sure we fail the request
        else:
            Schema.validate(schema, data, objName=objName)
        return json.dumps(data)

    @staticmethod
    def jsonLoads(dataStr, objName="", schema=None):
        """
        Deserialize data with JSON, optionally checking the schema
        @param dataStr:
        @param objName:
        @param schema:
        @return:
        """
        data = json.loads(dataStr)

        if schema == None:
            msg = 'No schema given for JSON deserialization of '+objName
            Utils.log(msg, err=True)
            raise Exception(msg) # Make sure we fail the request
        else:
            Schema.validate(schema, data, objName=objName)
        return data

    @staticmethod
    def schemaErrorReporter(msg, isWarning=False):
        # We abort for all schema violations
        Utils.log(msg)
        raise Exception(msg)


    @staticmethod
    def schemaDoc():
        """
        Generate the documentation for the schemas
        """
        def generateSection(outf, header="h2", anchor="", title=""):
            outf.write("<"+header+">")
            if anchor:
                outf.write("<a id='"+anchor+"'></a>")
            outf.write(title+"</"+header+">\n")


        def generateSchema(outf, header="h2", anchor="", title="", descr="", schema=None):
            generateSection(outf, header=header, anchor=anchor, title=title)
            outf.write(descr+"\n")
            html = Schema.htmlDoc(schema)
            outf.write(html+"\n")

        outf = sys.stdout


        outf.write(schemaDocStyle)

        outf.write("""
        <h1>JSON Schemas for CS169 Warmup Project</h1>

        This page documents the JSON schemas for the requests and responses for the CS169 Warmup project.
        <br>
        (This documentation was generated by <a href='schema_by_example.html'>Schema-By-Example</a> on %s)
    """ % (time.asctime()))
        generateSection(outf, header="h2", anchor='login',
                        title='/user/login and /user/add request')


        outf.write(UsersController.docRequest_login)
        generateSchema(outf,
                       schema=UsersController.schemaRequest_loginOrAdd)

        outf.write(UsersController.docResponse_login)
        generateSchema(outf,
                       schema=UsersController.schemaResp_loginOrAdd)


        generateSection(outf, header="h2", title='/TESTAPI/resetFixture request',
                        anchor='resetFixture')

        outf.write(TESTAPI_Controller.docReq_resetFixture)
        outf.write(TESTAPI_Controller.docResp_resetFixture)
        generateSchema(outf,
                       schema=TESTAPI_Controller.schemaResp_resetFixture)

        generateSection(outf, header="h2", title='/TESTAPI/unitTests request',
                        anchor='unitTests')

        outf.write(TESTAPI_Controller.docReq_unitTests)
        outf.write(TESTAPI_Controller.docResp_unitTests)
        generateSchema(outf,
                       schema=TESTAPI_Controller.schemaResp_unitTests)


Schema.registerErrorReporter(Utils.schemaErrorReporter)

###
### Main entry point
###
def run():
    """
    Main entry point
    """
    port = int(os.environ.get("PORT", 5000))
    # We use port 5000 to please Heroku 
    sys.stderr.write('http server is starting on 0.0.0.0:'+str(port)+'...\n')

    #ip and port of servr
    #by default http server port is 80
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, UserCounter_HTTPRequestHandler)
    sys.stderr.write('http server is running...\n')
    httpd.serve_forever()
    assert False #unreachable
    
if __name__ == '__main__':
    if '--doc' in sys.argv:
        Utils.schemaDoc()
        sys.exit(0)

    run()
