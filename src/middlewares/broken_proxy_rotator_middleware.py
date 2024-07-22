"""RotatingProxiesDownloadHandler implementation."""

import logging

from scrapy import Request, Spider
from scrapy.core.downloader.handlers.http11 import TunnelError
from twisted.internet.error import ConnectionRefusedError as ConnectionRefusedError_
from twisted.internet.error import TimeoutError as TimeoutError_
from twisted.web._newclient import ResponseNeverReceived


class BrokenProxyRotatorMiddleware:
    """Middleware for intercepting proxy connection errors and changing proxy IPs."""

    def __init__(self):
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)

    def process_exception(self, request: Request, exception: Exception, spider: Spider) -> None:
        """Calls when a download handler or a `process_request` (from a downloader middleware) raises an exception.
        It adds the `Connection=close` header when encountering exceptions of a specific type,
        allowing you to obtain a new IP address when using a rotating proxy.

        Args:
            request (Request): Scrapy request object.
            exception (Exception): Raised exception.
            spider (Spider): Spider which send the request.

        Returns:
            None: If it returns None, Scrapy will continue processing this exception, executing any
            other `process_exception()`.

        """
        if isinstance(exception, (TunnelError, ConnectionRefusedError_, ResponseNeverReceived, TimeoutError_)):
            exception_name = exception.__class__.__name__
            BrokenProxyRotatorMiddleware.set_close_connection_header(request, exception_name, self.logger)

    @staticmethod
    def set_close_connection_header(request: Request, reason: str, logger: logging.Logger) -> None:
        """Sets the 'Connection=close' header for a Scrapy request object.

        Args:
            request (Request): A Scrapy request object for which the 'Connection=close' header will be set.
            reason (str): The reason for setting the header triggering reconnection to the site (and changing proxies).
            logger (Logger): An instance of the logging.Logger class to log the action.

        """
        logger.info(f"Set `Connection=close` header for request to {request.url}, reason={reason}.")
        request.headers["Connection"] = "close"
