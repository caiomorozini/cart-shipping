from fastapi import FastAPI
from .routers import shipping

app = FastAPI()

app.include_router(shipping.router)
