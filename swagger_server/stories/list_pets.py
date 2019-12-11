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
class ListPets:
    """List pets available."""

    @story
    @arguments("user", "limit", "offset", "expand")
    def list_story(I):
        """Execute list story."""
        I.find_pets_for_user
        I.find_results_count
        I.find_related_photo_urls
        I.find_related_tags
        I.find_related_category
        I.apply_limit_and_offset
        I.return_results

    # Steps.

    def find_pets_for_user(self, ctx):
        """Find user's pets."""
        pets = self.load_pets_for_user(ctx.user)
        return Success(pets=pets)

    def find_results_count(self, ctx):
        """Find number of results count."""
        count = self.count(ctx.pets)
        return Success(count=count)

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

    def apply_limit_and_offset(self, ctx):
        """Filter results with limit and offset."""
        pets = self.limit_offset(ctx.with_category, ctx.limit, ctx.offset)
        return Success(limitted=pets)

    def return_results(self, ctx):
        """Return results in api format."""
        return Result(
            self.format_result(
                ctx.limitted,
                ctx.expand,
                ctx.count
            )
        )

    # Dependencies.

    limit_offset = attrib()
    count = attrib()
    load_pets_for_user = attrib()
    prefetch_photo_urls = attrib()
    prefetch_tags = attrib()
    prefetch_category = attrib()
    format_result = attrib()
