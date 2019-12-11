# coding: utf-8

from attr import (
    attrib,
    attrs
)
from stories import (
    Result,
    Success,
    arguments,
    story
)


@attrs
class RetrieveLastPet:
    """Retrieve last pet."""

    @story
    @arguments("user", "expand")
    def retrieve_last_story(I):
        """Execute retrieve last story."""
        I.find_pets_for_user
        I.find_related_photo_urls
        I.find_related_tags
        I.find_related_category
        I.limit_to_last_one
        I.return_result

    # Steps.

    def find_pets_for_user(self, ctx):
        """Find user's last pet."""
        pets = self.load_pets_for_user(ctx.user)
        return Success(pets=pets)

    def find_related_photo_urls(self, ctx):
        """Find related photo urls."""
        pets = self.prefetch_photo_urls(ctx.pets)
        return Success(with_photos=pets)

    def find_related_tags(self, ctx):
        """Find related tags."""
        pets = self.prefetch_tags(ctx.with_photos)
        return Success(with_tags=pets)

    def find_related_category(self, ctx):
        """Find related photo category."""
        pets = self.prefetch_category(ctx.with_tags)
        return Success(with_category=pets)

    def limit_to_last_one(self, ctx):
        """Limit to last one."""
        pet = self.limit_to_last(ctx.with_category)
        return Success(pet=pet)

    def return_result(self, ctx):
        """Return result in api format."""
        return Result(
            self.format_result(
                ctx.pet,
                ctx.expand
            )
        )

    # Dependencies.

    load_pets_for_user = attrib()
    prefetch_photo_urls = attrib()
    prefetch_tags = attrib()
    prefetch_category = attrib()
    limit_to_last = attrib()
    format_result = attrib()
