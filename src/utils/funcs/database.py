"""Helper functions for working with the database (MySQL)."""

from scrapy.utils.project import get_project_settings
from sqlalchemy import Executable
from sqlalchemy.dialects import mysql
from twisted.enterprise.adbapi import Transaction


def mysql_connection_string() -> str:
    """Returns string for connect to mysql."""
    settings = get_project_settings()
    return "mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4".format(  # pylint: disable=C0209
        settings.get("DB_USERNAME"),
        settings.get("DB_PASSWORD"),
        settings.get("DB_HOST"),
        settings.get("DB_PORT"),
        settings.get("DB_DATABASE"),
    )


# mypy: disable-error-code="attr-defined"
def execute_stmt(transaction: Transaction, stmt: Executable | str, is_many: bool = False) -> dict | tuple | None:
    """Executes the given SQL statement within the provided `Twisted.adbapi` transaction.

    Parameters:
    - transaction (Transaction): The `Twisted.adbapi` transaction object in which the statement will be executed.
    - stmt (SQLAlchemyExecutable | str): The SQL statement to be executed.
    - is_many (bool): Indicates whether the statement represents multiple rows. Defaults to False.

    Returns:
    - Optional[Union[dict, tuple]]: If is_many is True, returns a list of dictionaries representing rows.
      If is_many is False, returns a single dictionary or tuple representing the first result, or None if no result.

    Note:
    - When stmt is an SQLAlchemyExecutable, it is compiled with optional literal binds based on the
      literal_binds_enabled parameter and executed using the provided transaction.
    - When stmt is a raw SQL string, it is executed directly using the provided transaction.
    - If is_many is True, fetches all rows; if False, fetches the first row.

    """
    if isinstance(stmt, Executable):
        stmt_compiled = stmt.compile(dialect=mysql.dialect(), compile_kwargs={"render_postcompile": True})
        transaction.execute(str(stmt_compiled), tuple(stmt_compiled.params.values()))
    else:
        transaction.execute(stmt)

    if is_many:
        return transaction.fetchall()
    return transaction.fetchone()
