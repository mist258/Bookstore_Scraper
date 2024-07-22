"""Basic interface implementation for response parsers."""

import logging
from abc import ABC, abstractmethod

from scrapy.http import Response


class ResponseParser(ABC):
    """General interface for response parsers.

    Args:
        response (Response): Response object of a specific page.

    Attributes:
        logger (Logger): Logger instance.

    """

    _response: Response

    def __init__(self, response: Response) -> None:
        self._response = response
        self.logger = logging.getLogger(type(self).__name__)

    @classmethod
    @abstractmethod
    def is_supported(cls, response: Response) -> bool:
        """Checks if the Response object supported by the parser.

        Args:
            response (Response): Response object of a specific page.

        Returns:
            bool: True if the Response object supported by the parser, False otherwise.

        """

    def __repr__(self) -> str:
        """Returns a string representation of the object."""
        return f"<{self.__class__.__name__}(response={self._response})>"
