"""Module to define schemas and models for the application."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator


class CategoryEnum(str, Enum):
    """Enum for the product category.

    Attributes:
        category1 (str): categoria1
        category2 (str): categoria2
        category3 (str): categoria3
    """

    category1 = "categoria1"
    category2 = "categoria2"
    category3 = "categoria3"


class Sales(BaseModel):
    """Schema for the sales date.

    Attributes:
        email (EmailStr): buyer's email
        date (datetime): date of the purchase
        value (PositiveFloat): purchase value
        quantity (PositiveInt): quantity of products
        product (str): product name
        category (str): product category(enum)
    """

    email: EmailStr
    date: datetime
    value: PositiveFloat
    quantity: PositiveInt
    product: str
    category: CategoryEnum

    @field_validator("category")
    def Category_must_have_in_enum(cls: type, error: str) -> str:
        """Validate if the category is in the enum.

        Args:
            error (str): Error message.

        Returns:
            str: Error message.
        """
        return error
