import psycopg2


class PostgresDatabase:

    def __init__(self):

        self.connection = psycopg2.connect(

            host="postgres",

            database="bankdb",

            user="bankuser",

            password="bankpassword"

        )

    def get_connection(self):

        return self.connection