from scrapy.item import Item, Field


class BookItem(Item):
    """Fields that relevant to scraped book"""

    title = Field()
    authors = Field()
    category = Field()
    description = Field()
    publication_date = Field()
    publishing_house = Field()
    series = Field()
    isbn = Field()
    sku = Field()
    number_of_pages = Field()
    image_link = Field()
    image_name = Field()
    image_urls = Field()
    images = Field()
    condition = Field()
    book_format = Field()
    currency = Field()
    initial_price = Field()
    price = Field()
    delivery_time = Field()
    created_at = Field()
    updated_at = Field()
