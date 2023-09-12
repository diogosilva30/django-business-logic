from django.db import models

from django.db import models
from pydantic import BaseModel


class MagicMeta(type(models.Model)):
    """Metaclass that automatically defines django fields based on a provided pydantic model."""

    def __new__(cls, name, bases, attrs):
        pydantic_model = attrs.get("pydantic_model")

        if not pydantic_model:
            raise ValueError(
                "pydantic_model attribute is required for models that use MagicMeta"
            )

        for field_name, field_type in pydantic_model.__annotations__.items():
            # Translate Pydantic field types to Django field types
            if field_type == int:
                django_field = models.IntegerField()
            elif field_type == str:
                django_field = models.CharField(max_length=255)
            else:
                raise ValueError(f"Unsupported field type: {field_type}")

            attrs[field_name] = django_field

        return super().__new__(cls, name, bases, attrs)


class BookDTO(BaseModel):
    # id: int
    title: str
    author: str
    quantity: int
    owner_uuid: str
    some_other_field: int


class BookORM(models.Model, metaclass=MagicMeta):
    pydantic_model = BookDTO
