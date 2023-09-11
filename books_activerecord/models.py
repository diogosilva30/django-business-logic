from django.db import models


class Book(models.Model):
    """Represents a book in the library."""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)

    owner_uuid = models.UUIDField(null=True)
