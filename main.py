from fastapi import FastAPI

from api.auth_routes import router as auth_router

from api.payment_routes import router as payment_router

from api.metrics_routes import router as metrics_router


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