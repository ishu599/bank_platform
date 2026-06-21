import time
from observability.prometheus_metrics import REQUEST_COUNT
from observability.prometheus_metrics import PAYMENT_SUCCESS
from observability.prometheus_metrics import PAYMENT_FAILURE
from observability.prometheus_metrics import PAYMENT_LATENCY

class PaymentService:

    def __init__(

        self,

        bank,

        circuit_breaker,

        event_bus,

        metrics,

        fraud_detector,

        daily_limit_service,

        account_service,

        transaction_repository

    ):

        self.bank = bank

        self.breaker = circuit_breaker

        self.event_bus = event_bus

        self.metrics = metrics
    
        self.fraud = fraud_detector

        self.daily_limit = daily_limit_service

        self.account_service = account_service

        self.transaction_repository = transaction_repository

    def pay(

        self,

        transaction

    ):
        REQUEST_COUNT.inc()
        start = time.time()
        money_withdrawn = False
        try:
            self.fraud.check(

                    transaction

                    )

            self.daily_limit.check(

                 transaction

                    )

            self.account_service.withdraw(

                    transaction.username,

                    transaction.amount

                    )
            money_withdrawn = True
            response = self.breaker.call(

            self.bank.process_payment,

            transaction

                )
            
                      
            self.transaction_repository.save(

    transaction.username,

    transaction.amount,

    "SUCCESS"

)


            latency = (

                time.time()

                -

                start

            )

            self.metrics.record_success(

                latency

            )
            PAYMENT_SUCCESS.inc()

            PAYMENT_LATENCY.observe(latency)
            self.event_bus.publish(

                "payment_success",

                {

                    "transaction_id": transaction.transaction_id,

                    "username": transaction.username

                }

            )

            return response

        except Exception:

            if money_withdrawn:
                self.account_service.deposit(
                        transaction.username,
                        transaction.amount
                        )

            latency = (

                time.time()

                -

                start

            )
            self.transaction_repository.save(

    transaction.username,

    transaction.amount,

    "FAILED"

)
            self.metrics.record_failure(

                latency

            )
            PAYMENT_FAILURE.inc()

            PAYMENT_LATENCY.observe(latency)
            self.event_bus.publish(

                "payment_failure",

                {

                    "transaction_id": transaction.transaction_id,

                    "username": transaction.username

                }

            )

            raise
