from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware

from app.config.logging import logger
from app.api.routes.auth import router as auth_router
from app.api.routes.gmail import router as gmail_router
from app.api.routes.test import router as test_router
from app.database.db import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    logger.info("Database Initialized...")

    logger.info("Starting Email organizer API...")

    yield


app = FastAPI(title="Email Organizer MVP", version="1.0.0", lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key="change-this-later")


@app.get("/")
async def root():
    return {"message": "Email Organizer API"}


app.include_router(auth_router)
app.include_router(gmail_router)
app.include_router(test_router)