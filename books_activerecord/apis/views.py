from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Book
from .serializers import BorrowBookSerializer, BookSerializer
from rest_framework import mixins


class BooksAPI(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    """Books API."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=["PUT"], serializer_class=BorrowBookSerializer)
    def borrow(self, request, pk=None):
        """Borrow a book for a given user."""

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
