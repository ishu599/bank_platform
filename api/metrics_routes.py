from fastapi import APIRouter

from system.container import container


router = APIRouter()


@router.get(

    "/metrics"

)

def metrics():

    return (

        container.metrics.get_metrics()

    )