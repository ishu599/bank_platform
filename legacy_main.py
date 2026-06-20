from storage.database import Database

from repositories.user_repository import UserRepository

from repositories.refresh_token_repository import RefreshTokenRepository

from security.jwt_manager import JWTManager

from security.token_manager import TokenManager

from observability.audit_logger import AuditLogger

from observability.metrics import Metrics

from events.event_bus import EventBus

from system.circuit_breaker import CircuitBreaker

from bank.bank_simulator import BankSimulator

from services.auth_service import AuthService

from services.payment_service import PaymentService

from models.transaction import Transaction

from services.fraud_detection import FraudDetector

from services.daily_limit_service import DailyLimitService

from services.account_service import AccountService


fraud_detector = FraudDetector()

daily_limit_service = DailyLimitService()

account_service = AccountService()

bank = BankSimulator()

breaker = CircuitBreaker()

metrics = Metrics()

event_bus = EventBus()



def on_payment_success(data):

    print(

        "PAYMENT SUCCESS:",

        data

    )


def on_payment_failure(data):

    print(

        "PAYMENT FAILURE:",

        data

    )


def main():

    database = Database()

    database.initialize()

    event_bus = EventBus()

    metrics = Metrics()

    breaker = CircuitBreaker()

    bank = BankSimulator()

    user_repository = UserRepository(

        database

    )

    refresh_repository = RefreshTokenRepository(

        database

    )

    audit_logger = AuditLogger(

        database

    )

    jwt_manager = JWTManager()

    token_manager = TokenManager()

    auth_service = AuthService(

        user_repository,

        jwt_manager,

        audit_logger,

        refresh_repository,

        token_manager

    )

    payment_service = PaymentService(

        bank,

        breaker,

        event_bus,

        metrics,

        fraud_detector,

        daily_limit_service,

        account_service

    )

    event_bus.subscribe(

        "payment_success",

        on_payment_success

    )

    event_bus.subscribe(

        "payment_failure",

        on_payment_failure

    )
    
    request_id = "req-001"

    username = "raghu"

    password = "password123"

    role = "admin"

    try:

        auth_service.register(

            request_id,

            username,

            password,

            role

        )

    except Exception:

        pass

    tokens = auth_service.login(

        request_id,

        username,

        password

    )

    print(

        "LOGIN SUCCESS"

    )

    print(

        tokens

    )
    account_service.create_account(

    username,

    100000

    )
    transaction = Transaction(

        transaction_id=1,

        username=username,

        amount=1000

    )

    try:

        response = payment_service.pay(

            transaction

        )

        print(

            response

        )

    except Exception as e:

        print(

            e

        )

    print(

        metrics.get_metrics()

    )

    print(

        audit_logger.get_logs()

    )


if __name__ == "__main__":
    main()