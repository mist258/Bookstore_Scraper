from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from items_book.books_items import BookItem


class BooksSpider(CrawlSpider):
    name = "books_spider"
    allowed_domains = ["www.kennys.ie"]
    start_urls = ["https://www.kennys.ie/fiction",
                  "https://www.kennys.ie/poetry",
                  "https://www.kennys.ie/science-technology"]

    rules = (
        # rule for parse items
        Rule(
            LinkExtractor(restrict_xpaths="//div[@class='vm-product-descr-container-1']/h1/a"),
            callback="parse_item",
            follow=False
        ),
        # rule to follow links
        Rule(
            LinkExtractor(
                allow=(r'/fiction/', r'/poetry/', r'/science-technology/'),
                restrict_xpaths='//li[contains(@class, "item-")]//a'
            ),
            follow=True
        ),
        # rule for pagination
        Rule(
            LinkExtractor(restrict_xpaths="//li[@class='pagination-next']")
        )
    )

    def parse_item(self, response):
        item = BookItem()

        item["title"] = response.xpath('//div[@class="spacer-buy-area"]/h1/text()').get()
        item["authors"] = response.xpath(
            '//div[@class="spacer-buy-area"]/h2[@class="sc-author"]/text()'
        ).get()
        categories = response.xpath(
            '//div[@class="breadcrumbs"]/a[@class="pathway"][position()>1]/text()'
        ).getall()
        item["category"] = ", ".join([c.strip() for c in categories]) if categories else None
        item["description"] = response.xpath(
            '//div[@class="product-description"]/span[@itemprop="description"]/text()'
        ).get()
        item["publication_date"] = response.xpath(
            '//span[@class="product-fields-title" and contains(text(), "Publication date")]/ancestor::div[@class="span6"]/following-sibling::div/span[@class="product-field-display"]/text()'
        ).get()
        item["publishing_house"] =response.xpath(
            '//span[@class="product-fields-title" and contains(text(), "Publisher")]/ancestor::div[@class="span6"]/following-sibling::div/span[@class="product-field-display"]/text()'
        ).get()
        item["series"] = response.xpath(
            '//span[@class="product-fields-title" and contains(text(), "Series")]/ancestor::div[@class="span6"]/following-sibling::div/span[@class="product-field-display"]/text()'
        ).get()
        item["isbn"] = response.xpath(
            '//span[@class="product-fields-title" and contains(text(), "ISBN")]/ancestor::div[@class="span6"]/following-sibling::div/span[@class="product-field-display"]/text()'
        ).get()
        item["sku"] = response.xpath(
            '//span[@class="product-fields-title" and contains(text(), "SKU")]/ancestor::div[@class="span6"]/following-sibling::div/span[@class="product-field-display"]/text()'
        ).get()
        item["number_of_pages"] =  response.xpath(
            '//span[@class="product-fields-title" and contains(text(), "Number of Pages")]/ancestor::div[@class="span6"]/following-sibling::div/span[@class="product-field-display"]/text()'
        ).get()
        # item["image_link"] = response.xpath(
        #     '//div[@class="imagebox"]/img[@itemprop="image"]/@src'
        # ).get()
        #
        # if item["image_link"]:
        #     item["image_urls"] = [response.urljoin(item["image_link"])]
        # else:
        #     item["image_urls"] = []
        #
        # item["image_name"] = item["image_link"].split("/")[-1] if item["image_link"] else None
        # image_relative = response.xpath('//div[@class="imagebox"]/img[@itemprop="image"]/@src').get()
        # item["image_link"] = urljoin(response.url, image_relative) if image_relative else None
        item["image_link"] = response.xpath(
            '//div[@class="imagebox"]/img[@itemprop="image"]/@src'
        ).get()
        item["image_urls"] = [item["image_link"]] if item["image_link"] else []
        item["image_name"] = item["image_link"].split("/")[-1]
        item["condition"] = response.xpath(
            '//span[@class="product-fields-title" and contains(text(), "Condition")]/ancestor::div[@class="span6"]/following-sibling::div/span[@class="product-field-display"]/text()'
        ).get()
        item["book_format"] = response.xpath(
            '//span[@class="product-fields-title" and contains(text(), "Format")]/ancestor::div[@class="span6"]/following-sibling::div/span[@class="product-field-display"]/text()'
        ).get()
        item["currency"] = response.xpath(
            '//div[@class="PricesalesPrice vm-display vm-price-value"]/span[@class="PricesalesPrice"]/text()'
        ).re_first(r'[^\d.,\s]+')
        item["price"] = response.xpath(
            '//div[@class="PricesalesPrice vm-display vm-price-value"]/span[@class="PricesalesPrice"]/text()'
        ).re_first(r'[\d,.]+')
        item["initial_price"] = response.xpath(
            '//div[@class="PricebasePrice vm-display vm-price-value"]/span[@class="PricebasePrice"]/text()'
        ).re_first(r'[\d,.]+')
        item["delivery_time"] = response.xpath(
            '//span[@class="product-fields-title" and contains(text(), "Shipping Time")]/ancestor::div[@class="span6"]/following-sibling::div/span[@class="product-field-display"]/text()'
        ).get()
        item["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yield item
