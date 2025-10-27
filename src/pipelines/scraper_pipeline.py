from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from database.models import Book
from utils.mysql_connection_string import mysql_connection_string


class BookPipeline:

    def open_spider(self, spider):
        """ Launch the spider"""

        connection_str = mysql_connection_string()
        engine = create_engine(connection_str)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        spider.logger.info('Establish connection to database')



    def process_item(self, item, spider):

        existing_book = self.session.query(Book).filter_by(isbn=item['isbn']).first()
        try:
            if existing_book:
                existing_book.title = item.get('title')
                existing_book.authors = item.get('authors')
                existing_book.category = item.get('category')
                existing_book.description = item.get('description')
                existing_book.publication_date = item.get('publication_date')
                existing_book.publishing_house = item.get('publishing_house')
                existing_book.series = item.get('series')
                existing_book.isbn = item.get('isbn')
                existing_book.sku = item.get('sku')
                existing_book.number_of_pages = item.get('number_of_pages')
                existing_book.image_link = item.get('image_link')
                existing_book.image_name = item.get('image_name')
                existing_book.condition = item.get('condition')
                existing_book.book_format = item.get('book_format')
                existing_book.currency = item.get('currency')
                existing_book.initial_price = item.get('initial_price')
                existing_book.price = item.get('price')
                existing_book.delivery_time = item.get('delivery_time')
                existing_book.created_at = item.get('created_at')
                existing_book.updated_at = item.get('updated_at')

            else:
                book = Book(
                    title=item.get('title'),
                    author=item.get('authors'),
                    category=item.get('category'),
                    description=item.get('description'),
                    publication_date=item.get('publication_date'),
                    publishing_house=item.get('publishing_house'),
                    series=item.get('series'),
                    isbn=item.get('isbn'),
                    sku=item.get('sku'),
                    number_of_pages=item.get('number_of_pages'),
                    image_link=item.get('image_link'),
                    image_name=item.get('image_name'),
                    condition=item.get('condition'),
                    book_format=item.get('book_format'),
                    currency=item.get('currency'),
                    initial_price=item.get('initial_price'),
                    price=item.get('price'),
                    delivery_time=item.get('delivery_time'),
                    created_at=item.get('created_at'),
                    updated_at=item.get('updated_at'),
                )
                self.session.add(book)
            self.session.commit()
            spider.logger.info(f"Inserted book: {item['title']} - {item['isbn']}")

        except SQLAlchemyError as e:
            self.session.rollback()
            spider.logger.error(f"Raised error: {e}")

        return item


    def close_spider(self, spider):
        """ Close the spider"""
        self.session.close()
        spider.logger.info('Closing connection to database')

