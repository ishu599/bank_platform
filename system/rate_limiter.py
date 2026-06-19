from collections import deque
import time


class RateLimiter:

    def __init__(self):

        self.user_requests = {}

    def allow_request(

        self,

        username

    ):

        if username not in self.user_requests:

            self.user_requests[

                username

            ] = deque()

        history = self.user_requests[

            username

        ]

        current_time = time.time()

        while (

            history

            and

            current_time - history[0] > 60

        ):

            history.popleft()

        if len(history) < 5:

            history.append(

                current_time

            )

            return True

        return False
