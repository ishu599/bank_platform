class AccountService:

    def __init__(

        self

    ):

        self.accounts = {}

    def create_account(

        self,

        username,

        balance

    ):

        if username in self.accounts:

            raise Exception(

                "Account already exists"

            )

        self.accounts[username] = balance

        return True

    def get_balance(

        self,

        username

    ):

        if username not in self.accounts:

            raise Exception(

                "Account not found"

            )

        return self.accounts[username]

    def withdraw(

        self,

        username,

        amount

    ):

        if username not in self.accounts:

            raise Exception(

                "Account not found"

            )

        if amount <= 0:

            raise Exception(

                "Invalid amount"

            )

        balance = self.accounts[username]

        if balance < amount:

            raise Exception(

                "Insufficient funds"

            )

        self.accounts[username] = (

            balance - amount

        )

        return True

    def deposit(

        self,

        username,

        amount

    ):

        if username not in self.accounts:

            raise Exception(

                "Account not found"

            )

        if amount <= 0:

            raise Exception(

                "Invalid amount"

            )

        self.accounts[username] += amount

        return True
