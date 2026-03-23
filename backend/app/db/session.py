from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.app.core.config import settings

# Create a new SQLAlchemy engine instance
engine = create_engine(settings.DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a scoped session
db_session = scoped_session(SessionLocal)

def get_db():
    """
    Dependency that provides a database session.
    Yields a database session and closes it after use.
    """
    try:
        yield db_session
    finally:
        db_session.remove()