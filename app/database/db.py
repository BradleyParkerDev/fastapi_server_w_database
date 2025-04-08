import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.models import Base, UserSession, User


# Disable SQLAlchemy INFO logs but keep warnings/errors
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)  # Suppresses SQL execution logs (e.g., SELECT, INSERT)
logging.getLogger("sqlalchemy.orm").setLevel(logging.WARNING)  # Hides ORM-related logs (e.g., session commits, queries)
logging.getLogger("sqlalchemy.pool").setLevel(logging.WARNING)  # Prevents logs about database connections (pooling)
logging.getLogger("sqlalchemy").setLevel(logging.WARNING)  # Disables all SQLAlchemy logs except warnings/errors

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# For CRUD operations
class DB:
    def __init__(self):
        self.database_url = DATABASE_URL
        self.session_local = None
        self.session = None

    def initialize(self):
        self.engine = create_engine(self.database_url,echo=False) # echo=False suppresses SQL logs
        self.session_local = sessionmaker(bind=self.engine)
        self.session = self.session_local()

    def close(self):
        if self.session:
            self.session.close()

# For db creation without alembic
engine = create_engine(DATABASE_URL, echo=False) # echo=False suppresses SQL logs
def init_db():
    print("Connecting to database...")
    Base.metadata.create_all(bind=engine)
    print("App successfully connected to database!!!")