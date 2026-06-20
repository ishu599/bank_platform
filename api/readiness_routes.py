from fastapi import APIRouter

from system.container import container

router = APIRouter()


@router.get(

    "/ready"

)

def ready():

    try:

        container.database.get_connection()

        return {

            "status":"READY"

        }

    except:

        return {

            "status":"NOT_READY"

        }