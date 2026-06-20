from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from system.container import container

security = HTTPBearer()


def verify_token(

    credentials: HTTPAuthorizationCredentials = Depends(

        security

    )

):

    token = credentials.credentials

    try:

        payload = container.jwt_manager.verify(

            token

        )

        return payload

    except Exception as e:

        raise HTTPException(

            status_code=401,

            detail=str(e)

        )