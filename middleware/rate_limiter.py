import time

from collections import deque

from fastapi import HTTPException


class RateLimiter:

    def __init__(

        self

    ):

        self.history = {}

        self.limit = 10

        self.window = 60

    def check(

        self,

        username

    ):

        current = time.time()

        if username not in self.history:

            self.history[username] = deque()

        queue = self.history[username]

        while (

            queue

            and

            current - queue[0] > self.window

        ):

            queue.popleft()

        if len(

            queue

        ) >= self.limit:

            raise HTTPException(

                status_code=429,

                detail="Too many requests"

            )

        queue.append(

            current

        )