"""Implementation declarative base class."""

from typing import Any

from sqlalchemy import MetaData
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base model."""

    type_annotation_map = {list[dict[str, Any]]: JSON, list[dict[str, str]]: JSON, dict[str, str]: JSON}

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )
