# coding: utf-8

from dependencies import (
    Injector,
    Package
)

stories = Package("swagger_server.stories")
repositories = Package("swagger_server.repositories")
functions = Package("swagger_server.functions")
serializers = Package("swagger_server.serializers")


class ListPets(Injector):
    """Implement ListPets with injected dependencies."""

    list_story = stories.ListPets.list_story
    load_pets_for_user = repositories.pet.load_pets_for_user
    count = repositories.pet.count
    prefetch_photo_urls = repositories.pet.prefetch_photo_urls
    prefetch_tags = repositories.pet.prefetch_tags
    prefetch_category = repositories.pet.prefetch_category
    limit_offset = repositories.pet.limit_offset
    format_result = serializers.pet.format_collection


class RetrieveLastPet(Injector):
    """Implement RetrieveLastPet with injected dependencies."""

    retrieve_last_story = stories.RetrieveLastPet.retrieve_last_story
    load_pets_for_user = repositories.pet.load_pets_for_user
    prefetch_photo_urls = repositories.pet.prefetch_photo_urls
    prefetch_tags = repositories.pet.prefetch_tags
    prefetch_category = repositories.pet.prefetch_category
    limit_to_last = repositories.pet.limit_to_last
    format_result = serializers.pet.format_instance
