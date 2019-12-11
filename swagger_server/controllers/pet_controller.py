# coding: utf-8

from swagger_server.functions.auth import (
    login_required
)
from swagger_server.implemented import (
    ListPets,
    RetrieveLastPet
)


@login_required
def pet_get(user, limit=None, offset=None, expand=None):  # noqa: E501
    """List pets from the store.

     # noqa: E501

    :param user: authenticated user
    :type user: Object
    :param limit: items per page limit
    :type limit: int
    :param offset: number of items to skip
    :type offset: int
    :param expand: what related data to expand
    :type expand: str

    :rtype: Object
    """
    return ListPets.list_story(
        user,
        limit,
        offset,
        expand
    )


@login_required
def pet_last_get(user, expand=None):  # noqa: E501
    """List last pet from the store.

     # noqa: E501

    :param user: authenticated user
    :type user: Object
    :param limit: items per page limit
    :type limit: int
    :param offset: number of items to skip
    :type offset: int
    :param expand: what related data to expand
    :type expand: str

    :rtype: Pet
    """
    return RetrieveLastPet.retrieve_last_story(
        user,
        expand
    )
