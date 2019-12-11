# coding: utf-8

from swagger_server.functions.utils import (
    model_to_dict
)
from swagger_server.models import (
    Pet
)


def format_instance(pet, expand):
    """Format response properly form instance."""
    return Pet.from_dict(
        model_to_dict(pet, expand)
    )


def format_collection(pets, expand, count):
    """Format response properly from queryset, expand and result count."""
    api_pets = []
    for pet in pets:
        api_pets.append(
            Pet.from_dict(
                model_to_dict(pet, expand)
            )
        )

    return {
        "count": count,
        "results": api_pets
    }
