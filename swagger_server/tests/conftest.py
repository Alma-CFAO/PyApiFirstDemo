# coding: utf-8

import factory
import pytest
from django.utils import (
    timezone
)
from factory.django import (
    DjangoModelFactory
)
from pytest_factoryboy import (
    register
)

from apps.boilerplace.models import (
    CustomUser
)
from apps.db.models import (
    Category,
    Pet,
    PhotoUrl,
    Tag
)

DEFAULT_EMAIL = 'dummy@email.value'
DEFAULT_PASSWORD = 'hackme38'

pytestmark = pytest.mark.django_db


@register
class CustomUserFactory(DjangoModelFactory):
    """Create a custom user instance."""

    class Meta:
        """Class meta properties."""

        model = CustomUser

    email = factory.Sequence(lambda n: 'test-user{0}@exemple.com'.format(n))
    username = factory.Sequence(lambda n: 'test-user{0}@exemple.com'.format(n))
    password = factory.PostGenerationMethodCall(
        'set_password', DEFAULT_PASSWORD
    )
    date_joined = timezone.now()
    last_login = timezone.now()


@register
class CategoryFactory(DjangoModelFactory):
    """Create a category instance."""

    class Meta:
        """Class meta properties."""

        model = Category

    name = factory.Sequence(lambda n: 'category_{0}'.format(n))


@register
class TagFactory(DjangoModelFactory):
    """Create a tag instance."""

    class Meta:
        """Class meta properties."""

        model = Tag

    name = factory.Sequence(lambda n: 'tag_{0}'.format(n))


@register
class PhotoUrlFactory(DjangoModelFactory):
    """Create a photo url instance."""

    class Meta:
        """Class meta properties."""

        model = PhotoUrl

    url = factory.Sequence(lambda n: 'http://mo.n/image_{0}'.format(n))


@register
class PetFactory(DjangoModelFactory):
    """Create a pet instance."""

    class Meta:
        """Class meta properties."""

        model = Pet

    category = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        """Affect tags at instance creation."""
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for tag in extracted:
                self.tags.add(tag)

    @factory.post_generation
    def photo_urls(self, create, extracted, **kwargs):
        """Affect photo_urls at instance creation."""
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for photo_url in extracted:
                self.photo_urls.add(photo_url)
