import time


class PaymentService:

    def __init__(

        self,

        bank,

        circuit_breaker,

        event_bus,

        metrics

    ):

        self.bank = bank

        self.breaker = circuit_breaker

        self.event_bus = event_bus

        self.metrics = metrics

    def pay(

        self,

        transaction

    ):

        start = time.time()

        try:

            response = self.breaker.call(

                self.bank.process_payment,

                transaction

            )

            latency = (

                time.time()

                -

                start

            )

            self.metrics.record_success(

                latency

            )

            self.event_bus.publish(

                "payment_success",

                {

                    "transaction_id": transaction.transaction_id,

                    "username": transaction.username

                }

            )

            return response

        except Exception:

            latency = (

                time.time()

                -

                start

            )

            self.metrics.record_failure(

                latency

            )

            self.event_bus.publish(

                "payment_failure",

                {

                    "transaction_id": transaction.transaction_id,

                    "username": transaction.username

                }

            )

            raise
