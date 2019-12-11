# coding: utf-8

from settings.base import *  # NOQA

# For db:erdiagram and dev:shell command
INSTALLED_APPS += (  # NOQA
    'django_extensions',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
