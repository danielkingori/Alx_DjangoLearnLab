"""
WSGI config for blogApplication project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from http.server import HTTPServer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogApplication.settings')

application = get_wsgi_application()
# httpd = HTTPServer(('localhost', 8000), application)
# httpd.serve_forever()