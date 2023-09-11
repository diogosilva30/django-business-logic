# apis/__init__.py
from ..apis import *  # noqa


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Book
from .serializers import BookSerializer


class BooksAPI(viewsets.GenericViewSet):
    """Books API."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=["PUT"])
    def borrow(self, request, pk=None):
        """Borrow a book for a given user."""
        return Response({"message": "Hello, world!"})
