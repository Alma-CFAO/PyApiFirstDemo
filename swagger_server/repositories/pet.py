# coding: utf-8

from apps.db.models import (
    Pet
)
from swagger_server.functions.db import (
    apply_limit_and_offset_on_queryset
)
from swagger_server.functions.filters import (
    filter_queryset_on_user_perms
)


def load_pets():
    """Prepare queryset with all pets in database."""
    return Pet.objects.all()


def count(pets):
    """Return count from queryset."""
    return pets.count()


def load_pets_for_user(user):
    """Prepare queryset with all pets in database user's has permission on."""
    queryset = Pet.objects.all()
    return filter_queryset_on_user_perms(queryset, user)


def prefetch_photo_urls(pets):
    """Prefetch photo_urls related to pets in queryset."""
    return pets.prefetch_related('photo_urls')


def prefetch_tags(pets):
    """Prefetch tags related to pets in queryset."""
    return pets.prefetch_related('tags')


def prefetch_category(pets):
    """Prefetch category related to pets in queryset."""
    return pets.prefetch_related('category')


def limit_offset(pets, limit, offset):
    """Apply limit and offset on queryset."""
    return apply_limit_and_offset_on_queryset(
        pets,
        limit,
        offset
    )


def limit_to_last(pets):
    """Limit queryset to the last pet found."""
    return pets.last()
