\mainpage

CS169 Warmup Project is a simple project designed as a quick tutorial for building and deploying a web app for students in the CS169 class.
The implementation documented here does not use any web framework, but is otherwise fully functional.
The tests included with this implementation can be used as functional and acceptance tests for other implementations as well.

The description for this project is at: https://sites.google.com/site/ucbcs169sp14/project/warmupproject

Project Specification
-------------------

  - The class server.UsersModel contains the specification for your model
     - This entire documentation is generated using doxygen from comments in the Python files
       and *.md files (markdown format). This allows those parts of the documentation that are tied to the code
       to stay close to the code itself.
  - The client-server protocol uses JSON with the following [schemas](schemas.html)
     - The schema documentation is also extracted from the code by \ref schema_by_example


Installation
-------------

  - Unpack the loginCounterWarmup.tar.gz.

Running the server
------------------
   - You need to have python 2.x (>= 2.6) installed

         python server.py

     - this will run a web server on port 5000 on localhost

   - To manually test the mock server using the HTML client:
     - open a browser and point it to http://localhost:5000/client.html

   - To run unit tests for the mock server backend:

         make unit_tests

      - This will run the unit tests specified in serverTest.TestUsers
      - These unit tests are specific to the way the mock server is implemented. You will have to
        write your own unit tests using the conventions of the framework you are using.

   - To run functional tests for the mock server backend:

         # start a server
         python server.py
         make func_tests

       - This will issue requests to localhost:5000 and will check the results
       - The actual test specification are collected from all the test*.py files in the
        current directory (using Python standard unittest framework)
       - By default we are giving you the test in testSimple.TestUnit (the same tests as the serverTest.TestUsers
         unit tests but executed through the HTTP api), and testSimple.TestAddUser

       - To run functional tests against some other running backend

             # start your backend, e.g., on Heroku at myapp.herokuapp.com
             make func_tests TEST_SERVER=myapp.herokuapp.com

       - the TEST_SERVER environment variable can be set to the hostname:port for
          the server to test (defaults to localhost:5000)
       - We will grade your project by running these tests, the tests you will provide in testAdditional,
         and other test too ...


Writing more tests
-------------------

  - You should write more functional tests, in Python, following the model of the
    tests in testSimple.py. Put your tests in a file "testAdditional.py"
    next to testSimple.py. The "test" prefix of the name is required by the unittest
    framework, the rest is a requirement of our grading script.

Heroku deployment details
---------------

  The course web page has more extensive documentation about deploying to Heroku. This section documents
  the specific difficulties that I ran into when deploying these project.

  Deploying this app to Heroku was not trivial. Here is what worked:

  - install virtualenv
      - On Mac OSX with my python setup the permissions were missing the
        execute bit:

              INSTALL_DIR=/opt/local/Library/Frameworks/Python.framework/Versions/2.7
              sudo chmod a+x $INSTALL_DIR/bin/virtualenv*
              sudo chmod a+x $INSTALL_DIR/lib/python2.7/site-packages/virtualenv-1.8.4-py2.7.egg-info
              sudo chmod a+x $INSTALL_DIR/lib/python2.7/site-packages/virtualenv_support
  - run virtualenv in the local project directory

            PATH=$INSTALL_DIR/bin:$PATH virtualenv --distribute venv
  - this will create a venv subdirectory. Add it to .gitignore
  - activate this virtual environment
       source venv/bin/activate
  - generate the requirements.txt (this must exist for Python projects in
     Heroku)

         pip freeze >requirements.txt
  - generate the Procfile

  - try to run the project locally:

        foreman start (also make start_local)

  - Create the Heroku app
       heroku create
       - Here you will normally see that the git remote is added (git remote
          v). In my case, it wasn't. This was because the project was in a
       subdirectory (project/warmup) and heroku did not find the .git
       directory. This created lots of problems, because everytime I pushed to
       Heroku I was getting "Heroku push rejected, no Cedar-supported app
       detected". It took me a while to figure this out.
       - Now I use "git subtree" (see Makefile)

   - I had trouble getting the app started because it was using the wrong
     port. The solution was to write the app to read the value of the PORT
     environment variable and use it as a port number.

  - A very useful command for debugging this was:

        heroku logs -t --app myapp
    
