import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import logging


load_dotenv('.env')
DB_URL = os.getenv("DB_URL")



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if not DB_URL:
    raise ValueError("DB_URL environment variable is not set")


engine = create_engine(
    DB_URL,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True, 
    echo=False  # Set to True for SQL query logging
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
  
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
        db.rollback()
        raise
    finally:
        db.close()


def create_tables():

    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating tables: {e}")
        raise


def test_connection():
  
    try:
        with engine.connect() as connection:
            logger.info("Database connection successful")
            return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False