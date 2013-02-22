"""
WSGI config for zangetsu project.

"""
import os
import sys

sys.path.append('/home/caglar/zangetsu')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zangetsu.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
