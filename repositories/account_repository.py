class AccountRepository:

    def __init__(

        self,

        database

    ):

        self.database = database

    def create(

        self,

        username,

        balance

    ):

        connection = self.database.get_connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            INSERT INTO accounts(

                username,

                balance

            )

            VALUES(

                %s,

                %s

            )

            """,

            (

                username,

                balance

            )

        )

        connection.commit()

        cursor.close()

    def find(

        self,

        username

    ):

        connection = self.database.get_connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            SELECT *

            FROM accounts

            WHERE username=%s

            """,

            (

                username,

            )

        )

        row = cursor.fetchone()

        if row:

            columns = [

                desc[0]

                for desc in cursor.description

            ]

            cursor.close()

            return dict(

                zip(

                    columns,

                    row

                )

            )

        cursor.close()

        return None

    def update_balance(

        self,

        username,

        balance

    ):

        connection = self.database.get_connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            UPDATE accounts

            SET balance=%s

            WHERE username=%s

            """,

            (

                balance,

                username

            )

        )

        connection.commit()

        cursor.close()