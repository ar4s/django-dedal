"""
WSGI config for example project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

RUN_ON_HEROKU = os.getenv('RUN_ON_HEROKU')

settings_module = 'example.settings'

if RUN_ON_HEROKU:
    settings_module += '.heroku'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
