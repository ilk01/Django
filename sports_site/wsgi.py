"""
WSGI config for sports_site project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_site.settings')

application = get_wsgi_application()
