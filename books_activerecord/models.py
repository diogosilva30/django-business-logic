from django.db import models


class Book(models.Model):
    """Represents a book in the library."""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)

    owner_uuid = models.UUIDField(null=True)

    def borrow(self, user_uuid: str) -> bool:
        """Active Record Approach for borrowing a book from the library."""
        if self.quantity > 0:
            self.quantity -= 1
            self.owner_uuid = user_uuid
            self.save(update_fields=["quantity", "owner_uuid"])
            return True
        return False
