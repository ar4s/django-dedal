from . import *  # noqa
import dj_database_url

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
