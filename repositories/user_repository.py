class UserRepository:

    def __init__(

        self,

        database

    ):

        self.database = database

    def create_user(

        self,

        username,

        password_hash,

        role

    ):

        self.database.cursor.execute(

            """

            INSERT INTO users

            (

                username,

                password_hash,

                role

            )

            VALUES(?,?,?)

            """,

            (

                username,

                password_hash,

                role

            )

        )

        self.database.connection.commit()

    def find_user(

        self,

        username

    ):

        cursor = self.database.cursor.execute(

            """

            SELECT *

            FROM users

            WHERE username=?

            """,

            (

                username,

            )

        )

        return cursor.fetchone()

    def delete_user(

        self,

        username

    ):

        self.database.cursor.execute(

            """

            DELETE FROM users

            WHERE username=?

            """,

            (

                username,

            )

        )

        self.database.connection.commit()
