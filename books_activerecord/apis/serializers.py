from rest_framework import serializers

from ..models import Book
from ..services import BookService


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BorrowBookSerializer(serializers.ModelSerializer):
    """Serializer for the borrow book endpoint."""

    def update(self, instance: Book, validated_data: dict):
        """Calls the borrow_book service method to borrow a book for a given user."""

        borrowed: bool = BookService.borrow_book(
            book=instance,
            user_uuid=validated_data["owner_uuid"],
        )

        if not borrowed:
            raise serializers.ValidationError(
                {"detail": "Book could not be borrowed. It may be out of stock."}
            )

        return instance

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["quantity", "name", "author", "title"]
