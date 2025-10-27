"""Initialization of 'database/models/' package."""

from .base import Base
from .book_models import Book

__all__ = ["Base", "Book"]
