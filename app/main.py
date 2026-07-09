from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware

from app.config.logging import logger
from app.api.routes.auth import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Email organizer API...")
    yield


app = FastAPI(title="Email Organizer MVP", version="1.0.0", lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key="change-this-later")


@app.get("/")
async def root():
    return {"message": "Email Organizer API"}


app.include_router(auth_router)
