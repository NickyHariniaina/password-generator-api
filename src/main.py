from fastapi import FastAPI
from .password_generator.router import router

app = FastAPI()

app.include_router(router, prefix="/api", tags=["Password generator"])
app.include_router(router, prefix="/api", tags=["Password checker"])
