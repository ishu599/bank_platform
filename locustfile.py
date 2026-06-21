from locust import HttpUser
from locust import task
from locust import between


class BankUser(HttpUser):

    wait_time = between(1, 3)

    @task(5)
    def health(self):

        self.client.get("/health")

    @task(3)
    def login(self):

        self.client.post(
            "/auth/login",
            json={
                "username": "admin",
                "password": "password"
            }
        )

    @task(2)
    def payment(self):

        self.client.post(
            "/payments",
            json={
                "amount": 100
            }
        )