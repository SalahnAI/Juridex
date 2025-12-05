from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="LexiScan AI PRO",
    version="1.0.0"
)

app.include_router(router, prefix="/api")
