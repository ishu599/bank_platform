from fastapi import APIRouter

from fastapi import Depends

from middleware.auth_middleware import verify_token

from system.container import container

router = APIRouter()


@router.get(

    "/transactions/{username}"

)

def get_transactions(

    username:str,

    user=Depends(

        verify_token

    )

):

    cache_key = f"transactions:{username}"

    cached = container.cache_service.get(

        cache_key

    )

    if cached:

        return {

            "source":"cache",

            "data":cached

        }

    data = container.transaction_repository.get_by_user(

        username

    )

    container.cache_service.set(

        cache_key,

        str(data),

        60

    )

    return {

        "source":"database",

        "data":data

    }