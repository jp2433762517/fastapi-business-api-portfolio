from fastapi import FastAPI
from .router import api_router

app = FastAPI(title="fastapi-business-api-portfolio")

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def health():
    return {"status": "ok"}
