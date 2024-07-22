"""Implementation http proxy middleware."""

from typing import Self

from scrapy import Request, Spider
from scrapy.crawler import Crawler
from scrapy.exceptions import NotConfigured
from w3lib.http import basic_auth_header


class HttpProxyMiddleware:
    """Middleware sets the HTTP proxy to use for requests, by setting the proxy meta value for Request objects."""

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Self:
        """Returns a new instance of the middleware.

        Args:
            crawler (Crawler): Crawler object.

        """
        if crawler.settings.getbool("PROXY_ENABLED"):
            return cls()

        crawler.spider.logger.info(f"{cls.__name__} disabled.")
        raise NotConfigured

    def _update_request(self, request: Request, spider: Spider) -> Request:
        """Sets proxy credentials to request meta.

        Args:
            request (Request): Scrapy request object.
            spider (Spider): Spider which send the request.

        """
        proxy: str | None = spider.settings.get("PROXY_ADDRESS")
        if not proxy:
            raise ValueError("Proxy enabled but not configured")

        if "http" not in proxy:
            proxy = f"http://{proxy}"

        username: str | None = spider.settings.get("PROXY_USERNAME")
        password: str | None = spider.settings.get("PROXY_PASSWORD")
        if username and password:
            request.headers["Proxy-Authorization"] = basic_auth_header(username, password, "utf-8")

        request.meta["proxy"] = proxy
        return request

    def process_request(self, request: Request, spider: Spider) -> None:
        """Called for each request that goes through the download middleware.

        Args:
            request (Request): Scrapy request object.
            spider (Spider): Spider which send the request.

        """
        if "proxy" not in request.meta:
            self._update_request(request, spider)
