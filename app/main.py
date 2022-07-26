import uvicorn

from fastapi import FastAPI

from app.api.v1 import api_router
from app.core import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", reload=True, workers=1, port=8000)
