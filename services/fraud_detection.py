from collections import deque

import time


class FraudDetector:

    def __init__(self):

        self.history = {}

        self.max_amount = 50000

        self.blacklist = {

            "friend",

            "user"

        }

    def check(

        self,

        transaction

    ):

        username = transaction.username

        current_time = time.time()

        if username in self.blacklist:

            raise Exception(

                "user is blacklisted"

            )

        if transaction.amount > self.max_amount:

            raise Exception(

                "amount exceeded maximum amount"

            )

        if username not in self.history:

            self.history[username] = deque()

        history = self.history[username]

        while history and current_time - history[0] > 30:

            history.popleft()

        if len(history) >= 3:

            raise Exception(

                "too many attempts in 30 sec"

            )

        history.append(

            current_time

        )

        return True