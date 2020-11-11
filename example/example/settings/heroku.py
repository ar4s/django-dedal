from . import *  # noqa
import dj_database_url

DEBUG = False
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['django-dedal.herokuapp.com', 'django-dedal.source.net.pl']
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
