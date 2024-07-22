"""Factory implementation for response parsers.

Attributes:
    AnyResponseParser: Parser type that inherits from ResponseParser.

"""

from typing import Any, Generic, TypeVar

from scrapy.http import Response

from parsers.exceptions import MultipleParsersFoundError, ParserNotFoundError
from parsers.response_parser import ResponseParser

AnyResponseParser = TypeVar("AnyResponseParser", bound=ResponseParser)


class ParserFactory(Generic[AnyResponseParser]):
    """Factory for response parsers.

    This class creates different response parsers based on the given list of parser types.

    References:
        More detailed description here:
            - \
https://groupbwt.atlassian.net/wiki/spaces/CA/pages/3244753015/Response+Parsers+and+Factory+guidelines#ParserFactory

    Args:
        parsers: list[type[AnyResponseParser]]: List of parsers that the factory class will work with.

    """

    _parsers: list[type[AnyResponseParser]]

    def __init__(self, parsers: list[type[AnyResponseParser]]) -> None:
        self._parsers = parsers

    def create_parser(self, response: Response, *args: Any, **kwargs: Any) -> AnyResponseParser:
        """Creates an instance of the parser that supports the passed Response object.

        Args:
            response (Response): Response object of a specific page.
            *args (Any): Positional arguments to be passed to the parser constructor.
            **kwargs (Any): Keyword arguments to be passed to the parser constructor.

        Returns:
            AnyResponseParser: Parser instance.

        Raises:
            ParserNotFoundError: Parser not found for this Response object.
            MultipleParsersFoundError: Response object supported by multiple parsers.

        """
        supported_parsers = [p for p in self._parsers if p.is_supported(response)]
        if len(supported_parsers) == 1:
            return supported_parsers[0](response, *args, **kwargs)
        if len(supported_parsers) > 1:
            raise MultipleParsersFoundError("Response object supported by multiple parsers")
        raise ParserNotFoundError("Parser not found for this Response object")

    def __repr__(self) -> str:
        """Returns a string representation of the object."""
        return f"<{self.__class__.__name__}(number_of_parsers={len(self._parsers)})>"
