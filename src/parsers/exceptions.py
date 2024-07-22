"""Parsers exceptions."""


class ParserError(ValueError):
    """Base class for related parsers errors."""


class ParserNotFoundError(ParserError):
    """Supported parser not found for received response."""


class MultipleParsersFoundError(ParserError):
    """Multiple parsers support the received answer."""
