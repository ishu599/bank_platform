from prometheus_client import Counter
from prometheus_client import Histogram

REQUEST_COUNT = Counter(
    "payment_requests_total",
    "Total payment requests"
)

PAYMENT_SUCCESS = Counter(
    "payment_success_total",
    "Successful payments"
)

PAYMENT_FAILURE = Counter(
    "payment_failure_total",
    "Failed payments"
)

PAYMENT_LATENCY = Histogram(
    "payment_latency_seconds",
    "Payment latency"
)