from . import *  # noqa
import dj_database_url

ALLOWED_HOSTS = ['django-dedal.herokuapp.com']
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
