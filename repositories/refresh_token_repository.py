import time


class RefreshTokenRepository:

    def __init__(

        self,

        database

    ):

        self.database = database

    def create_token(

        self,

        username,

        token_hash,

        expires_at

    ):

        self.database.cursor.execute(

            """

            INSERT INTO refresh_tokens

            (

                username,

                token_hash,

                expires_at,

                created_at

            )

            VALUES(?,?,?,?)

            """,

            (

                username,

                token_hash,

                expires_at,

                int(

                    time.time()

                )

            )

        )

        self.database.connection.commit()

    def get_token(

        self,

        token_hash

    ):

        cursor = self.database.cursor.execute(

            """

            SELECT *

            FROM refresh_tokens

            WHERE token_hash=?

            """,

            (

                token_hash,

            )

        )

        return cursor.fetchone()

    def delete_token(

        self,

        token_hash

    ):

        self.database.cursor.execute(

            """

            DELETE FROM refresh_tokens

            WHERE token_hash=?

            """,

            (

                token_hash,

            )

        )

        self.database.connection.commit()

    def delete_user_tokens(

        self,

        username

    ):

        self.database.cursor.execute(

            """

            DELETE FROM refresh_tokens

            WHERE username=?

            """,

            (

                username,

            )

        )

        self.database.connection.commit()

    def token_exists(

        self,

        token_hash

    ):

        cursor = self.database.cursor.execute(

            """

            SELECT 1

            FROM refresh_tokens

            WHERE token_hash=?

            """,

            (

                token_hash,

            )

        )

        return cursor.fetchone() is not None
