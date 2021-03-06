from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings


def get_url():
    """
    List of url database
    """
    database = settings.DATABASE
    user = settings.DATABASE_USER
    password = settings.DATABASE_PASS
    name = settings.DATABASE_NAME
    host = settings.DATABASE_HOST
    port = settings.DATABASE_PORT
    if settings.DATABASE_URL:  # handle heroku postgres
        return settings.DATABASE_URL
    else:
        return f"{database}://{user}:{password}@{host}:{port}/{name}"

SQLALCHEMY_DATABASE_URL = get_url()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=2,
    pool_recycle=300,
    pool_use_lifo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
