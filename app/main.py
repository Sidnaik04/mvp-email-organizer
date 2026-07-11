from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware

from app.config.logging import logger
from app.api.routes.auth import router as auth_router
from app.api.routes.gmail import router as gmail_router
from app.api.routes.test import router as test_router
from app.api.routes.evaluation import router as eval_router
from app.api.routes.database import router as db_router
from app.database.db import Base, engine
from sqlalchemy import text
import app.database.models


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Database Initialized...")
    logger.info("Starting Email Organizer API...")

    yield


app = FastAPI(title="Email Organizer MVP", version="1.0.0", lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key="change-this-later")


@app.get("/")
async def root():
    return {"message": "Email Organizer API"}


app.include_router(auth_router)
app.include_router(gmail_router)
app.include_router(test_router)
app.include_router(eval_router)
app.include_router(db_router)
