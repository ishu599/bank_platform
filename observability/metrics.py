class Metrics:

    def __init__(

        self

    ):

        self.total_requests = 0

        self.success_requests = 0

        self.failed_requests = 0

        self.total_latency = 0

    def record_success(

        self,

        latency

    ):

        self.total_requests += 1

        self.success_requests += 1

        self.total_latency += latency

    def record_failure(

        self,

        latency

    ):

        self.total_requests += 1

        self.failed_requests += 1

        self.total_latency += latency

    def get_metrics(

        self

    ):

        average_latency = 0

        if self.total_requests:

            average_latency = (

                self.total_latency

                /

                self.total_requests

            )

        return {

            "total_requests": self.total_requests,

            "success_requests": self.success_requests,

            "failed_requests": self.failed_requests,

            "average_latency": average_latency

        }
