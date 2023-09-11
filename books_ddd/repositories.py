"""Module containing repositories for the books app. Repositories are
encapsulations of data access logic. They are responsible for
interacting with the database and returning domain objects.
"""
from django.shortcuts import get_object_or_404
from .models import Book


class BookRepository:
    @staticmethod
    def get_by_id(book_id: int) -> Book:
        """Get a book by its id.

        Parameters
        ----------
        book_id : int
            The id of the book to get.

        Returns
        -------
        Book
            The book with the given id.

        Raises
        ------
        Http404
            If no book with the given id exists.
        """
        return get_object_or_404(Book, id=book_id)

    @staticmethod
    def update_owner(*, book: Book, owner_uuid: str) -> Book:
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
        book.owner_uuid = owner_uuid
        book.save()
        return book
