# coding: utf-8

from django.contrib.auth.models import (
    AbstractUser
)
from django.db import (
    models
)
from django.utils.translation import \
    ugettext_lazy as \
    _


class CustomUser(
    AbstractUser
):
    """
    Generic user model.

    This model aim to be used for user authentication.
    User can either be standard, staff or superuser.
    """

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    )
    is_verified = models.BooleanField(
        _('email verified'),
        default=False
    )
    verified_at = models.DateTimeField(
        _('verified at'),
        null=True
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'id'

    def __str__(self):
        """Override CustomUser model string representation."""
        return (
            str(self.id) +
            ' - ' +
            str(self.email)
        )
