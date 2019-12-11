# coding: utf-8

from django.utils.translation import \
    ugettext_lazy as \
    _

# SECURITY WARNING: keep the secret key used in production secret!
# AND CHANGE THIS PLEASE, THIS IS THE DEMO SECRET KEY!
SECRET_KEY = '123jiraidanslesbois'

ALLOWED_HOSTS = ['*']

# Database config

DB_PREFIX = "connexiontest_"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

# Django apps config

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'guardian',

    'apps.boilerplace',
    'apps.db'
)

# Auth database config for guardian

AUTH_USER_MODEL = 'boilerplace.CustomUser'
ANONYMOUS_USER_NAME = None 

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    ('pt', _('Portuguese')),
]

# Ignore guardian warning as standard django guardian backend is missing
# And we do not care!
SILENCED_SYSTEM_CHECKS = ["guardian.W001"]
