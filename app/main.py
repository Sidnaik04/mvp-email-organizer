from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware

from app.config.logging import logger
from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router
from app.api.routes.gmail import router as gmail_router
from app.api.routes.classify import router as classify_router
from app.api.routes.history import router as history_router
from app.api.routes.stats import router as stats_router
from app.database.db import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    logger.info("Database Initialized...")

    logger.info("Starting Email organizer API...")

    yield


app = FastAPI(title="Email Organizer MVP", version="1.0.0", lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key="change-this-later")


app.include_router(health_router)
app.include_router(auth_router)
app.include_router(gmail_router)
app.include_router(classify_router)
app.include_router(history_router)
app.include_router(stats_router)
