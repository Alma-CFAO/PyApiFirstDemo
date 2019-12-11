# coding: utf-8

from guardian.shortcuts import (
    get_objects_for_user
)


def filter_queryset_on_user_perms(queryset, user):
    """Return queryset filtered by user object permissions."""
    perm_format = '%(app_label)s.view_%(model_name)s'
    shortcut_kwargs = {
        'accept_global_perms': False,
    }

    permission = perm_format % {
        'app_label': queryset.model._meta.app_label,
        'model_name': queryset.model._meta.model_name,
    }

    return get_objects_for_user(
        user,
        permission,
        queryset,
        **shortcut_kwargs
    )
