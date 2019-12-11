# coding: utf-8

from functools import (
    wraps
)

import jwt
from connexion.apps import (
    flask_app
)
from django.conf import (
    settings
)
from django.contrib.auth.models import (
    AnonymousUser
)

from apps.boilerplace.models import (
    CustomUser
)

SECRET_KEY = settings.SECRET_KEY


def login_required(function):
    """Wrap controller function to test if user is logged in."""
    @wraps(function)
    def decorated(*args, **kwargs):
        """Return HTTP401 Response if user is not logged in else run controller code."""
        if isinstance(kwargs['user'], AnonymousUser):
            return {
                "detail": "Authorization token invalid or expired",
                "status": 401,
                "title": "Unauthorized",
                "type": "about:blank"
            }
        return function(*args, **kwargs)
    return decorated


def user_info_to_user_instance(user_info, update_or_create=True):
    """Add user_instance in kwargs, builded from user_info from token."""
    user_instance = AnonymousUser()

    # Create instance from user info
    if user_info is not None:

        # CustomUser
        if (
            'is_app' not in user_info.keys()
        ):
            values = {
                'email': user_info['email'],
                'username': user_info['email'],
                'is_verified': user_info['is_verified'],
                'is_active': user_info['is_active'],
                'is_staff': user_info['is_staff'],
                'is_superuser': user_info['is_superuser'],
                'date_joined': user_info['date_joined'],
                'last_login': user_info['last_login'],
            }
            if update_or_create:
                user, created = CustomUser.objects.update_or_create(
                    values,
                    id=user_info['id']
                )
                user.save()
            else:
                user = CustomUser(
                    id=user_info['id'],
                    **values
                )
            user_instance = user

    return user_instance


def fake_user_if_fake_jwt_token(token):
    """Fake user info is DEBUG is True and fake token was given."""
    user_info = None
    if token == 'super_user':
        user_info = {
            'id': 1,
            'email': "super@user.test",
            'is_active': True,
            'is_staff': True,
            'is_superuser': True,
            'is_verified': True,
            'date_joined': "2018-01-23T12:51:46+00:00",
            'last_login': "2018-02-06T11:07:02.193120+00:00"
        }
    elif token == 'staff_user':
        user_info = {
            'id': 1,
            'email': "staff@user.test",
            'is_active': True,
            'is_staff': True,
            'is_superuser': False,
            'is_verified': True,
            'date_joined': "2018-01-23T12:51:46+00:00",
            'last_login': "2018-02-06T11:07:02.193120+00:00"
        }
    elif token == 'standard_user':
        user_info = {
            'id': 1,
            'email': "standard@user.test",
            'is_active': True,
            'is_staff': False,
            'is_superuser': False,
            'is_verified': True,
            'date_joined': "2018-01-23T12:51:46+00:00",
            'last_login': "2018-02-06T11:07:02.193120+00:00"
        }
    elif token == 'unverified_standard_user':
        user_info = {
            'id': 1,
            'email': "standard@user.test",
            'is_active': True,
            'is_staff': False,
            'is_superuser': False,
            'is_verified': False,
            'date_joined': "2018-01-23T12:51:46+00:00",
            'last_login': "2018-02-06T11:07:02.193120+00:00",
        }
    elif token == 'blocked_standard_user':
        user_info = {
            'id': 1,
            'email': "standard@user.test",
            'is_active': False,
            'is_staff': False,
            'is_superuser': False,
            'is_verified': False,
            'date_joined': "2018-01-23T12:51:46+00:00",
            'last_login': "2018-02-06T11:07:02.193120+00:00"
        }
    return user_info


def decode_jwt_token(token):
    """Return user information decodded from token or None is token is None."""
    user_info = None

    try:
        user_info = jwt.decode(
            token,
            SECRET_KEY,
            verify=True,
            options={
                'verify_exp': True,
            },
            leeway=0,
            audience=None,
            issuer=None,
            algorithms=['HS256']
        )
    except jwt.exceptions.PyJWTError:
        pass

    is_debug = flask_app.flask.current_app.config['DEBUG'] is True

    if is_debug:
        user_info = fake_user_if_fake_jwt_token(token)

    user_instance = user_info_to_user_instance(
        user_info,
        update_or_create=(
            not is_debug
        )
    )

    return {
        'sub':
        user_instance
    }
