"""
WSGI config for myvalentine project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import sys
import os

path = '/home/raechel/myvalentine'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myvalentine.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()