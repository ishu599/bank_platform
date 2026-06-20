from storage.database import Database

from repositories.user_repository import UserRepository
from repositories.refresh_token_repository import RefreshTokenRepository
from repositories.transaction_repository import TransactionRepository
from observability.audit_logger import AuditLogger
from observability.metrics import Metrics

from security.jwt_manager import JWTManager
from security.token_manager import TokenManager

from system.circuit_breaker import CircuitBreaker

from bank.bank_simulator import BankSimulator

from services.auth_service import AuthService
from services.account_service import AccountService
from services.payment_service import PaymentService
from services.fraud_detection import FraudDetector
from services.daily_limit_service import DailyLimitService

from events.event_bus import EventBus
from middleware.rate_limiter import RateLimiter

from services.cache_service import CacheService




class Container:

    def __init__(self):

        self.database = Database()

        self.database.initialize()

        self.metrics = Metrics()

        self.event_bus = EventBus()

        self.breaker = CircuitBreaker()

        self.bank = BankSimulator()

        self.account_service = AccountService()
        self.rate_limiter = RateLimiter()

        self.cache_service = CacheService()
        self.account_service.create_account(

    "raghu",

    100000

)
        self.fraud_detector = FraudDetector()

        self.daily_limit_service = DailyLimitService()
        self.transaction_repository = TransactionRepository(self.database)
        self.user_repository = UserRepository(

            self.database

        )

        self.refresh_repository = RefreshTokenRepository(

            self.database

        )

        self.audit_logger = AuditLogger(

            self.database

        )

        self.jwt_manager = JWTManager()

        self.token_manager = TokenManager()

        self.auth_service = AuthService(

            self.user_repository,

            self.jwt_manager,

            self.audit_logger,

            self.refresh_repository,

            self.token_manager

        )

        self.payment_service = PaymentService(

            self.bank,

            self.breaker,

            self.event_bus,

            self.metrics,

            self.fraud_detector,

            self.daily_limit_service,

            self.account_service

        )


container = Container()