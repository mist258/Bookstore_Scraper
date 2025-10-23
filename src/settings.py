"""Scrapy settings for data_collection project.

For simplicity, this file contains only settings considered important or
commonly used. You can find more settings consulting the documentation:

    https://docs.scrapy.org/en/latest/topics/settings.html
    https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
    https://docs.scrapy.org/en/latest/topics/spider-middleware.html

"""

import os

from dotenv import load_dotenv
from scrapy.utils.reactor import install_reactor

from middlewares import BrokenProxyRotatorMiddleware, HttpProxyMiddleware
from rmq.utils import get_import_full_name
from utils.funcs.util import strtobool

load_dotenv(verbose=False, override=True)
FEED_EXPORT_ENCODING="utf-8"

BOT_NAME = "scrapy_boilerplate_v2"

SPIDER_MODULES = ["spiders"]
NEWSPIDER_MODULE = "spiders"
COMMANDS_MODULE = "commands"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "data_collection (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "middlewares.DataCollectionSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # "middlewares.DataCollectionDownloaderMiddleware": 543,
    get_import_full_name(HttpProxyMiddleware): 749,
    # "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 750,
    get_import_full_name(BrokenProxyRotatorMiddleware): 910,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "pipelines.DataCollectionPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# database (MySQL) settings
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

# RabbitMQ settings
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
RABBITMQ_VIRTUAL_HOST = os.getenv("RABBITMQ_VIRTUAL_HOST")

# proxy settings
PROXY_ENABLED = strtobool(os.getenv("PROXY_ENABLED", "False"))
PROXY_ADDRESS = os.getenv("PROXY_ADDRESS")
PROXY_USERNAME = os.getenv("PROXY_USERNAME")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")
PROXY_PORT = os.getenv("PROXY_PORT")

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
install_reactor(TWISTED_REACTOR)
FEED_EXPORT_ENCODING = "utf-8"
