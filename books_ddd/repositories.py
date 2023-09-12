"""Module containing repositories for the books app. Repositories are
encapsulations of data access logic. They are responsible for
interacting with the database and returning domain objects.
"""
from typing import Type, TypeVar

from django.shortcuts import get_object_or_404
from .models import BookDTO, BookORM

T = TypeVar("T", bound=BookORM)
D = TypeVar("D", bound=BookDTO)


class BaseRepository:
    dto_class: Type[D]

    def to_dto(self, instance: T) -> D:
        return self.dto_class.from_orm(instance)


class BookRepository(BaseRepository):
    dto_class = BookDTO

    def get_by_id(self, *, book_id: int) -> BookDTO:
        """Get a book by its id."""

        django_book = get_object_or_404(BookORM, id=book_id)
        return self.to_dto(django_book)

    def update_owner(self, *, book_id: int, owner_uuid: str) -> BookDTO:
        """Update the owner of a book.
        Parameters
        ----------
        book : Book
            The book to update.
        owner_uuid : str
            The uuid of the new owner.

        Returns
        -------
        Book
            The updated book.
        """
        django_book = get_object_or_404(BookORM, id=book_id)
        django_book.owner_uuid = owner_uuid
        django_book.save(update_fields=["owner_uuid"])
        return self.to_dto(django_book)
