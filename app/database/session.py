from sqlalchemy.orm import sessionmaker

from app.database.db import engine

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)
