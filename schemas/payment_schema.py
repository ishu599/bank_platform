from pydantic import BaseModel


class PaymentRequest(

    BaseModel

):

    username: str

    amount: float


class AccountCreateRequest(

    BaseModel

):

    username: str

    initial_balance: float


class DepositRequest(

    BaseModel

):

    username: str

    amount: float