
import time


class AuditLogger:

    def __init__(

        self,

        database

    ):

        self.database = database

    def log(

        self,

        request_id,

        username,

        action,

        status

    ):

        self.database.cursor.execute(

            """

            INSERT INTO audit_logs

            (

                request_id,

                username,

                action,

                status,

                timestamp

            )

            VALUES(?,?,?,?,?)

            """,

            (

                request_id,

                username,

                action,

                status,

                int(

                    time.time()

                )

            )

        )

        self.database.connection.commit()

    def get_logs(

        self

    ):

        cursor = self.database.cursor.execute(

            """

            SELECT *

            FROM audit_logs

            ORDER BY timestamp DESC

            """

        )

        return cursor.fetchall()
