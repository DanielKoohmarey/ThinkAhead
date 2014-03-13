#
# A number of make targets to simpligy testing and setup tasks
#

# Default target: run all the tests
.PHONY: all_tests
all_tests ::

# Run the unit tests
.PHONY: unit_tests
unit_tests: 
	@echo "\n=======  Running unit tests =========\n"
	python serverTest.py
all_tests :: unit_tests

# Run the functional tests
# The functional tests are discovered by scanning files that start with test... for unittest.TestCase subclasses
.PHONY: func_tests
func_tests:
	@echo "\n======= Running functional tests ======\n"
	python -m unittest discover -v $(TESTARGS)

all_tests :: func_tests


# Make the student package
.PHONY: package
PACKAGE=loginCounterWarmup.tar.gz
package:
	cd .. && rm -f $(PACKAGE) && \
        tar cvfz $(PACKAGE) \
            --exclude .git --exclude .gitignore \
            --exclude .idea --exclude testPrivate.py --exclude gradingScript.py \
            --exclude TODO --exclude '*.pyc' \
            --exclude venv \
            warmup

COURSE_SSH=cs169@cory.eecs.berkeley.edu
COURSE_DIR=public_html/sp14



###
### DOCUMENTATION
###
.PHONY: docs
docs:
	rm -rf docs/html/*
	python server.py --doc  >docs/html/schemas.html
	TOPDIR=`pwd` doxygen docs/Doxyfile
	find docs/html -type d -exec chmod a+x \{\} \;
	rsync -prv docs/html/* $(COURSE_SSH):$(COURSE_DIR)/loginCounterWarmup


.PHONY: post_package
post_package: 
	$(MAKE) package docs
	rsync -prv ../$(PACKAGE) $(COURSE_SSH):$(COURSE_DIR)/loginCounterWarmup


###
### HEROKU DEPLOYMENT
###
### Read README for some deployment details
###
start_local: 
	foreman start

HEROKU_APP=serene-meadow-7552

# Since this file lives in a directory of a bigger git repository, we cannot 
# just push the whole repo (Heroku will not find the necessary files at top-level)
# Instead we use "git subtree"
deploy_heroku:
	pushd ../.. && git push git@heroku.com:$(HEROKU_APP).git `git subtree split --prefix project/warmup`:master --force && popd


logs_heroku:
	heroku logs -t --app $(HEROKU_APP)