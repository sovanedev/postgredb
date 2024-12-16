import psycopg2
from _exceptions import *

class Base:
    def __init__(self, db_config: dict):
        """
        Инициализация класса Base.

        :param db_config: Словарь с параметрами подключения к базе данных.
        """
        self.db_config = db_config

    def connect(self):
        """
        Устанавливает соединение с базой данных.

        :return: Объект соединения с базой данных.
        :raises ConnectionError: Если не удается подключиться к базе данных.
        """
        try:
            return psycopg2.connect(**self.db_config)
        except psycopg2.Error as e:
            raise ConnectionError(f"Ошибка подключения: {e}")

    def add_table(self, table_sql: str):
        """
        Добавляет SQL-запрос для создания таблицы и выполняет его.

        :param table_sql: SQL-запрос на создание таблицы.
        :raises ExecutionError: Если ошибка возникает при выполнении запроса.
        :raises TableExistsError: Если таблица уже существует.
        """
        if not isinstance(table_sql, str):
            raise TypeError("Ожидалась строка для SQL-запроса, но получен {}".format(type(table_sql)))

        with self.connect() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(table_sql)
                    conn.commit()
                except psycopg2.errors.DuplicateTable as e:
                    raise TableExistsError("unknown", f"Ошибка: {e}")
                except psycopg2.Error as e:
                    raise ExecutionError(table_sql, f"Ошибка выполнения запроса: {e}")

    def execute(self, query: str, parameters: tuple = None):
        """
        Выполняет произвольный SQL-запрос.

        :param query: SQL-запрос для выполнения.
        :param parameters: Параметры для SQL-запроса (если есть).
        :return: ID последней вставленной строки, если запрос содержит 'RETURNING'.
        :raises ExecutionError: Если ошибка возникает при выполнении запроса.
        :raises InvalidQueryError: Если запрос недопустимый.
        """
        if not isinstance(query, str):
            raise InvalidQueryError(query, "Запрос должен быть строкой.")

        with self.connect() as conn:
            with conn.cursor() as cursor:
                try:
                    if parameters:
                        cursor.execute(query, parameters)
                    else:
                        cursor.execute(query)
                    if "RETURNING" in query:
                        last_row_id = cursor.fetchone()[0]
                    else:
                        last_row_id = None
                    conn.commit()
                except psycopg2.Error as e:
                    raise ExecutionError(query, f"Ошибка выполнения запроса: {e}")
        return last_row_id

    def fetchone(self, query: str, parameters: tuple = None):
        """
        Извлекает одну запись из базы данных.

        :param query: SQL-запрос для извлечения данных.
        :param parameters: Параметры для SQL-запроса (если есть).
        :return: Первая запись результата запроса.
        :raises ExecutionError: Если ошибка возникает при выполнении запроса.
        :raises InvalidQueryError: Если запрос недопустимый.
        """
        if not isinstance(query, str):
            raise InvalidQueryError(query, "Запрос должен быть строкой.")

        with self.connect() as conn:
            with conn.cursor() as cursor:
                try:
                    if parameters:
                        cursor.execute(query, parameters)
                    else:
                        cursor.execute(query)
                    return cursor.fetchone()
                except psycopg2.Error as e:
                    raise ExecutionError(query, f"Ошибка выполнения запроса: {e}")

    def fetchall(self, query: str, parameters: tuple = None):
        """
        Извлекает все записи из базы данных.

        :param query: SQL-запрос для извлечения данных.
        :param parameters: Параметры для SQL-запроса (если есть).
        :return: Все записи результата запроса.
        :raises ExecutionError: Если ошибка возникает при выполнении запроса.
        :raises InvalidQueryError: Если запрос недопустимый.
        """
        if not isinstance(query, str):
            raise InvalidQueryError(query, "Запрос должен быть строкой.")

        with self.connect() as conn:
            with conn.cursor() as cursor:
                try:
                    if parameters:
                        cursor.execute(query, parameters)
                    else:
                        cursor.execute(query)
                    return cursor.fetchall()
                except psycopg2.Error as e:
                    raise ExecutionError(query, f"Ошибка выполнения запроса: {e}")