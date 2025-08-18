from fastapi import FastAPI
from app.routes.entries import router

from app.routes import entries

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix="/entries", tags=["entries"])