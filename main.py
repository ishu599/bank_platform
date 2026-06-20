from fastapi import FastAPI

from api.auth_routes import router as auth_router

from api.payment_routes import router as payment_router

from api.metrics_routes import router as metrics_router

from api.transaction_routes import router as transaction_router

from api.health_routes import router as health_router
app = FastAPI()


app.include_router(

    auth_router

)

app.include_router(

    payment_router

)

app.include_router(

    metrics_router

)

app.include_router(

    transaction_router

)
app.include_router(

    health_router

)