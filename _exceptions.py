class DatabaseError(Exception):
    """Базовый класс для ошибок базы данных."""
    pass

class ConnectionError(DatabaseError):
    """Ошибка подключения к базе данных."""
    def __init__(self, message="Не удалось подключиться к базе данных."):
        self.message = message
        super().__init__(self.message)

class ExecutionError(DatabaseError):
    """Ошибка выполнения SQL-запроса."""
    def __init__(self, query, message="Ошибка выполнения запроса."):
        self.message = message
        self.query = query
        super().__init__(f"{self.message} Запрос: {self.query}")

class TableExistsError(DatabaseError):
    """Ошибка, когда таблица уже существует."""
    def __init__(self, table_name, message="Таблица уже существует."):
        self.message = message
        self.table_name = table_name
        super().__init__(f"{self.message} Имя таблицы: {self.table_name}")

class TableNotFoundError(DatabaseError):
    """Ошибка, когда таблица не найдена."""
    def __init__(self, table_name, message="Таблица не найдена."):
        self.message = message
        self.table_name = table_name
        super().__init__(f"{self.message} Имя таблицы: {self.table_name}")

class InvalidQueryError(DatabaseError):
    """Ошибка, связанная с недопустимым SQL-запросом."""
    def __init__(self, query, message="Недопустимый SQL-запрос."):
        self.message = message
        self.query = query
        super().__init__(f"{self.message} Запрос: {self.query}")