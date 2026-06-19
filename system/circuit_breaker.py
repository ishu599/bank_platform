import time


class CircuitBreaker:

    def __init__(self):

        self.state = "CLOSED"

        self.failure_count = 0

        self.last_failure_time = None

        self.threshold = 3

        self.recovery_time = 30

    def can_execute(

        self

    ):

        current_time = time.time()

        if self.state == "CLOSED":

            return True

        elif self.state == "OPEN":

            if (

                current_time

                -

                self.last_failure_time

                <

                self.recovery_time

            ):

                return False

            self.state = "HALF_OPEN"

            return True

        elif self.state == "HALF_OPEN":

            return True

    def on_failure(

        self

    ):

        self.failure_count += 1

        self.last_failure_time = time.time()

        if (

            self.failure_count

            >=

            self.threshold

        ):

            self.state = "OPEN"

    def on_success(

        self

    ):

        self.last_failure_time = None

        self.failure_count = 0

        self.state = "CLOSED"

    def call(

        self,

        func,

        *args,

        **kwargs

    ):

        if not self.can_execute():

            raise Exception(

                "Circuit breaker open"

            )

        try:

            response = func(

                *args,

                **kwargs

            )

            self.on_success()

            return response

        except Exception:

            self.on_failure()

            raise
