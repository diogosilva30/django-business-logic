"""Module containing services for the books app. Services are the
entrypoint into the domain layer. They are responsible for handling
business logic and data transformations.
"""
import logging

from .models import Book

logger = logging.getLogger(__name__)


class BookService:
    """Service for handling book domain logic."""

    @staticmethod
    def borrow_book(*, book: Book, user_uuid: str) -> bool:
        """Borrow a book for a given user.
        Parameters
        ----------
        book_id : int
            The id of the book to borrow.
        user_uuid : str
            The uuid of the user borrowing the book.

        Returns
        -------
        bool
            True if the book was successfully borrowed, False otherwise.
        """
        if book and book.quantity > 0:
            book.quantity -= 1
            logger.info("Borrowing book %s for user %s", book.pk, user_uuid)
            book.owner_uuid = user_uuid
            book.save(update_fields=["quantity", "owner_uuid"])
            return True

        logger.info("Book %s could not be borrowed for user %s", book.pk, user_uuid)

        return False
