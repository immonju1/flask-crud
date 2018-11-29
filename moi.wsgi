import sys

#require python
if sys.version_info[0]<3:
	raise Exception("Python3 required! Current (wrong) version: '%s'" % sys.version_info)

sys.path.insert(0, '/home/juhawsgi/public_wsgi/')
from moi import app as application
