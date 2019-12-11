# coding: utf-8

"""
Flask app with connexion and Django ORM.

See: https://docs.djangoproject.com/en/dev/topics/settings/#either-configure-or-django-settings-module-is-required

isort:skip_file
"""

import os

import connexion
from django.apps import (
    apps
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")

from django.conf import (  # NOQA
    settings
)
from flask import (  # NOQA
    Flask
)

from swagger_server import (  # NOQA
    encoder
)

apps.populate(settings.INSTALLED_APPS)

app = connexion.App(__name__, specification_dir='./swagger_server/openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml', arguments={'title': 'Swagger Petstore'})

if __name__ == '__main__':
    app.run(debug=True)
