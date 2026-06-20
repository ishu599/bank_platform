from fastapi import APIRouter

from fastapi import HTTPException

from schemas.auth_schema import RegisterRequest

from system.container import container

from schemas.auth_schema import LoginRequest
router = APIRouter()


@router.post("/register")

def register(

    request: RegisterRequest

):

    try:

        container.auth_service.register(

            "api-request",

            request.username,

            request.password,

            request.role

        )

        return {

            "message": "user created"

        }

    except Exception as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )
    
@router.post(

    "/login"

)
def login(

    request: LoginRequest

):

    try:

        tokens = container.auth_service.login(

            "api-request",

            request.username,

            request.password

        )

        return tokens

    except Exception as e:

        raise HTTPException(

            status_code=401,

            detail=str(e)

        )