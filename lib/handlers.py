"""Module that handles the wrappers and handlers for the DB connection
"""
import logging
from lib.helpers.enum_base import EnumBase
from lib.db import DB
from app.config import Config


class OperationType(EnumBase):
    """Enum class for query operation types
    """
    FETCH_ALL = "fetch_all"
    RUN_QUERY = "run_query"
    FETCH_ROW = "fetch_one"


class CRUDWrapper:
    """DB Wrapper for basic CRUD operations"""

    def __init__(self):
        self.db = DB(db=Config.SCHEMA).db_connect
        self.logger = logging.getLogger("crud_wrapper")

    def read(self, table: str, values: dict, fetch_all=False):
        """Simple GET operation to fetch from table in DB

        Args:
            table (str): Table name
            values (dict): A map of the columns->values to search for
            fetch_all (bool, optional): Whether to fetch all results. Defaults to False

        Returns:
            if fetch_all:
                list: List of rows, represented as dicts
            else:
                dict: Singular row result
        """
        with self.db("dict") as cursor:
            cursor.execute(
                f"""
                SELECT * FROM {table}
                WHERE {' AND '.join([f'{x} = %s' for x in values.keys()])}
            """,
                tuple(values.values()),
            )
            data = cursor.fetchall()

        if data and not fetch_all:
            return data[0]

        return data

    def insert(self, table: str, columns: list, values: list):
        """Method to perform simple INSERT operation

        Args:
            table (str): Table to insert into
            column (list): Columns to add data for
            value (list): Data values

        Returns:
            int: Last row id of an auto increment column
        """
        with self.db() as cursor:
            cursor.execute(
                f"""
                INSERT INTO {table} ({','.join(columns)})
                VALUES ({','.join(['%s' for x in values])})
            """,
                tuple(values),
            )

            return cursor.getlastrowid()

    def update(self, table: str, new_values: dict, condition: list):
        """Simple update method to aid in generic operations

        Args:
            table (str): Name of target table
            values (dict): A map of the columns->values to set to
            condition (list): The conditions to check for

        Returns:
            str: The executed statement
        """
        with self.db() as cursor:
            cursor.execute(
                f"""
                UPDATE {table}
                SET {','.join([f'{x} = %s' for x,y in new_values.items()])}
                WHERE {' AND '.join(condition)}
            """,
                tuple(new_values.values()),
            )
            # pylint: disable=protected-access
            return cursor._executed

    def drop(self, table: str, condition_values: dict, condition: list):
        """Simple delete method for basic operations

        Args:
            table (str): Target table name
            condition (list): List of conditions to fulfill
            values (dict): Map of values to apply to the conditions

        Returns:
            str: Executed query
        """
        with self.db() as cursor:
            cursor.execute(
                f"""
                DELETE {table}
                WHERE {' AND '.join(condition)}
            """,
                condition_values,
            )
            # pylint: disable=protected-access
            return cursor._executed


class DBWrapper:
    """DB Wrapper that allows more freedom for custom queries, etc."""

    def __init__(self):
        self.db = DB(db=Config.SCHEMA).db_connect
        self.logger = logging.getLogger("db_wrapper")

    def _execute(
        self,
        query: str,
        operation_type: OperationType,
        params: dict = None,
        cursor_type: str = "dict",
    ):
        result = None
        with self.db(cur_type=cursor_type) as cursor:
            # Execute query with params
            cursor.execute(query, params)
            # Determine return based on operation type
            if operation_type == OperationType.FETCH_ALL:
                result = cursor.fetchall()
            if operation_type == OperationType.FETCH_ROW:
                result = cursor.fetchone()
            if operation_type == OperationType.RUN_QUERY:
                result = cursor.rowcount
        return result


    def run_query(self, query: str, params: dict = None, cursor_type: str='dict') -> int:
        """Execute a SQL query that doesn't require fetching results

        Args:
            query (str): Query to run
            params (dict, optional): Query params. Defaults to None.
            cursor_type (str, optional): _description_. Defaults to 'dict'.

        Returns:
            int: Count of affected rows
        """
        return self._execute(
            query=query,
            operation_type=OperationType.RUN_QUERY,
            params=params,
            cursor_type=cursor_type
        )

    def fetch_all(self, query: str, params: dict = None, cursor_type: str='dict') -> list:
        """Fetch all results from a specified query

        Args:
            query (str): Query to run
            params (dict, optional): Query parameters. Defaults to None.
            cursor_type (str, optional): Cursor type for resultset. Defaults to 'dict'.

        Returns:
            list: List of results
        """
        return self._execute(
            query=query,
            operation_type=OperationType.FETCH_ALL,
            params=params,
            cursor_type=cursor_type
        )

    def fetch_row(self, query: str, params: dict = None, cursor_type: str='dict') -> list:
        """Fetch a single result from a specified query

        Args:
            query (str): Query to run
            params (dict, optional): Query parameters. Defaults to None.
            cursor_type (str, optional): Cursor type for resultset. Defaults to 'dict'.

        Returns:
            dict: Query result
        """
        return self._execute(
            query=query,
            operation_type=OperationType.FETCH_ROW,
            params=params,
            cursor_type=cursor_type
        )
