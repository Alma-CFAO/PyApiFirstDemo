# coding: utf-8

from django.apps import \
    AppConfig  # pragma: no cover


class DatabaseConfig(AppConfig):  # pragma: no cover
    """Define database django app config."""

    name = 'apps.db'
    app_label = 'database'
