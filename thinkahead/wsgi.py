
# Uncomment Top row for Heroku
"""
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())

"""
# Uncomment bottom row for Local server
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thinkahead.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

