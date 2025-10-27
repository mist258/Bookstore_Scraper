from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Book(Base):
    """Book database model."""
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(String(200))
    author: Mapped[str] = mapped_column(String(100))
    category: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(Text)
    publication_date: Mapped[Optional[str]] = mapped_column(String(50))
    publishing_house: Mapped[Optional[str]] = mapped_column(String(100))
    series: Mapped[Optional[str]] = mapped_column(String(50))
    isbn: Mapped[Optional[str]] = mapped_column(String(50), primary_key=True,  nullable=False, index=True)
    sku: Mapped[Optional[str]] = mapped_column(String(50), index=True)
    number_of_pages: Mapped[Optional[str]] = mapped_column(String(20))
    image_link: Mapped[Optional[str]] = mapped_column(String(255))
    image_name: Mapped[Optional[str]] = mapped_column(String(50))
    condition: Mapped[Optional[str]] = mapped_column(String(50))
    book_format: Mapped[Optional[str]] = mapped_column(String(50))
    currency: Mapped[Optional[str]] = mapped_column(String(5))
    initial_price: Mapped[Optional[float]] = mapped_column(Numeric(10, 2))
    price: Mapped[Optional[float]] = mapped_column(Numeric(10, 2))
    delivery_time: Mapped[Optional[str]] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)




