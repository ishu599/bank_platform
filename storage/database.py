import sqlite3


class Database:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if hasattr(self, "initialized"):

            return

        self.connection = sqlite3.connect(

            "bank_platform.db",

            check_same_thread=False

        )

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.initialized = True

    def initialize(self):

        self.create_users_table()

        self.create_refresh_tokens_table()

        self.create_audit_logs_table()

        self.create_transactions_table()

    def create_transactions_table(self):

        self.cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS transactions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        amount REAL,

        status TEXT,

        created_at TEXT

    )
    """
    )
        self.connection.commit()
    def create_users_table(self):

        self.cursor.execute(

            """
            CREATE TABLE IF NOT EXISTS users(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                username TEXT UNIQUE NOT NULL,

                password_hash TEXT NOT NULL,

                role TEXT NOT NULL

            )
            """
        )

        self.connection.commit()

    def create_refresh_tokens_table(self):

        self.cursor.execute(

            """
            CREATE TABLE IF NOT EXISTS refresh_tokens(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                username TEXT NOT NULL,

                token_hash TEXT UNIQUE NOT NULL,

                expires_at INTEGER NOT NULL,

                created_at INTEGER NOT NULL

            )
            """
        )

        self.connection.commit()

    def create_audit_logs_table(self):

        self.cursor.execute(

            """
            CREATE TABLE IF NOT EXISTS audit_logs(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                request_id TEXT NOT NULL,

                username TEXT NOT NULL,

                action TEXT NOT NULL,

                status TEXT NOT NULL,

                timestamp INTEGER NOT NULL

            )
            """
        )

        self.connection.commit()
    
    def close(self):

        self.connection.close()
