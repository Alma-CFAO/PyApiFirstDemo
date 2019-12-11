# coding: utf-8

import pytest

from swagger_server.functions.utils import (
    model_to_dict
)

pytestmark = pytest.mark.django_db


def test_model_to_dict(
    category_factory,
    pet_factory,
    tag_factory
):
    """Test usage of model_to_dict function on Pet model with many to many and foreign key fields."""
    category = category_factory()
    tag1 = tag_factory()
    tag2 = tag_factory()
    pet = pet_factory()

    pet.tags.add(tag1)
    pet.tags.add(tag2)
    pet.category = category

    assert model_to_dict(pet, expand="category") == {
        'id': pet.id,
        'category': {
            'id': category.id,
            'name':
            'category_0'
        },
        'name': '',
        'status': '',
        'tags': [tag1.id, tag2.id],
        'photo_urls': []
    }
