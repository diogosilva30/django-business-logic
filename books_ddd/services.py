"""Module containing services for the books app. Services are the
entrypoint into the domain layer. They are responsible for handling
business logic and data transformations.
"""
import logging

from .repositories import BookRepository

logger = logging.getLogger(__name__)


class BookService:
    """Service for handling book domain logic."""

    @staticmethod
    def borrow_book(*, book_id: int, user_uuid: str) -> bool:
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

        book = BookRepository.get_by_id(book_id)
        if book and book.quantity > 0:
            book.quantity -= 1
            logger.info("Borrowing book %s for user %s", book_id, user_uuid)
            BookRepository.update_owner(book=book, owner_uuid=user_uuid)
            return True

        logger.info("Book %s could not be borrowed for user %s", book_id, user_uuid)

        return False
