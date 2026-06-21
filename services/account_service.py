class AccountService:

    def __init__(

        self,

        repository,

        redis

    ):

        self.repository = repository

        self.redis = redis

    def create_account(

    self,

    username,

    balance

        ):
        account = self.repository.find(

        username

    )

        if account:

            raise Exception(

            "Account already exists"

        )

        self.repository.create(

        username,

        balance

    )

        return True

    def get_balance(

    self,

    username

):

        cache_key = f"account:{username}"

        cached = self.redis.get(

        cache_key

    )

        if cached:

            return float(

            cached

        )

        account = self.repository.find(

        username

    )

        if not account:

            raise Exception(

            "Account not found"

        )

        balance = account["balance"]

        self.redis.set(

        cache_key,

        balance,

        ttl=300

    )

        return balance

    def withdraw(

    self,

    username,

    amount

):

        if amount <= 0:

            raise Exception(

            "Invalid amount"

        )

        balance = self.get_balance(

            username

    )

        if balance < amount:

            raise Exception(

            "Insufficient funds"

        )

        new_balance = (

        balance - amount

    )

        self.repository.update_balance(

        username,

        new_balance

    )

        self.redis.delete(

        f"account:{username}"

    )

        return True

    def deposit(

    self,

    username,

    amount

):

        if amount <= 0:

            raise Exception(

            "Invalid amount"

        )

        balance = self.get_balance(

        username

    )

        new_balance = (

        balance + amount

    )

        self.repository.update_balance(

        username,

        new_balance

    )

        self.redis.delete(

        f"account:{username}"

    )

        return True