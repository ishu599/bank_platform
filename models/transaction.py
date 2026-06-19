from time import time


class Transaction:

    def __init__(

        self,

        transaction_id,

        username,

        amount

    ):

        self.transaction_id = transaction_id

        self.username = username

        self.amount = amount

        self.status = "PENDING"

        self.created_at = int(

            time()

        )
