from datetime import datetime


class TransactionRepository:

    def __init__(

        self,

        database

    ):

        self.database = database

    def save(

        self,

        username,

        amount,

        status

    ):

        connection = self.database.get_connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            INSERT INTO transactions(

                username,

                amount,

                status,

                created_at

            )

            VALUES(

                %s,

                %s,

                %s,

                %s

            )

            """,

            (

                username,

                amount,

                status,

                datetime.utcnow().isoformat()

            )

        )

        connection.commit()

    def get_by_user(

        self,

        username

    ):

        connection = self.database.get_connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            SELECT *

            FROM transactions

            WHERE username=%s

            ORDER BY id DESC

            """,

            (

                username,

            )

        )

        rows = cursor.fetchall()

        columns = [

            desc[0]

            for desc in cursor.description

        ]

        return [

            dict(

                zip(

                    columns,

                    row

                )

            )

            for row in rows

        ]