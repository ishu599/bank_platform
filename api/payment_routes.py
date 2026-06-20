from fastapi import APIRouter

from fastapi import HTTPException

from system.container import container

from schemas.payment_schema import PaymentRequest

from models.transaction import Transaction


router = APIRouter()


transaction_counter = 1


@router.post(

    "/pay"

)

def pay(

    request: PaymentRequest

):

    global transaction_counter

    try:

        transaction = Transaction(

            transaction_id=transaction_counter,

            username=request.username,

            amount=request.amount

        )

        transaction_counter += 1

        response = container.payment_service.pay(

            transaction

        )

        return response

    except Exception as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )