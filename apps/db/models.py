# coding: utf-8

from django.db import (
    models
)


class BaseModel(models.Model):
    """Define an abstract Base model for other models to inherit from."""

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        """Make is abstract."""

        abstract = True


class Category(BaseModel):
    """Define Category model fields."""

    name = models.TextField()


class Tag(BaseModel):
    """Define Tag model fields."""

    name = models.TextField()


class PhotoUrl(BaseModel):
    """Define PhotoUrl model fields."""

    url = models.TextField()


class Pet(BaseModel):
    """Define Pet model fields."""

    tags = models.ManyToManyField(Tag)
    photo_urls = models.ManyToManyField(PhotoUrl)
    category = models.ForeignKey(
        Category,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.TextField()
    status = models.TextField()
