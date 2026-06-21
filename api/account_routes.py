from fastapi import APIRouter

from system.container import container

router = APIRouter()


@router.post(

    "/account/create"

)

def create_account(

    username: str,

    balance: float

):

    container.account_service.create_account(

        username,

        balance

    )

    return {

        "message": "Account created"

    }


@router.get(

    "/account/balance/{username}"

)

def get_balance(

    username: str

):

    balance = container.account_service.get_balance(

        username

    )

    return {

        "username": username,

        "balance": balance

    }