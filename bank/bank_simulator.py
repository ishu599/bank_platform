import random


class BankSimulator:

    def process_payment(

        self,

        transaction

    ):

        chance = random.random()

        if chance < 0.2:

            raise Exception(

                "Bank unavailable"

            )

        return {

            "transaction_id": transaction.transaction_id,

            "status": "SUCCESS"

        }
