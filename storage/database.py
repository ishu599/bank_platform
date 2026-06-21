import os
import psycopg2


class Database:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if hasattr(

            self,

            "initialized"

        ):

            return

        self.connection = psycopg2.connect(

            host=os.getenv(

                "DB_HOST",

                "localhost"

            ),

            port=int(

                os.getenv(

                    "DB_PORT",

                    5432

                )

            ),

            database=os.getenv(

                "DB_NAME",

                "bankdb"

            ),

            user=os.getenv(

                "DB_USER",

                "postgres"

            ),

            password=os.getenv(

                "DB_PASSWORD",

                "password"

            )

        )

        self.initialized = True

    def get_connection(

        self

    ):

        return self.connection