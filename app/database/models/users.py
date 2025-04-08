import uuid
from .model_base_class import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from datetime import datetime, timezone 

class User(Base):
    __tablename__ = "users"

    user_id = Column(pgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_image = Column(String, nullable=False)
    user_name = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    password = Column(String, unique=True, nullable=False)
    last_updated = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

