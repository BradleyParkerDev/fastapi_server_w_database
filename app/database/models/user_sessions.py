import uuid
from .model_base_class import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from datetime import datetime, timezone, timedelta 

class UserSession(Base):
    __tablename__ = "user_sessions"

    session_id = Column(pgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(pgUUID(as_uuid=True), ForeignKey('users.user_id',ondelete="CASCADE"), nullable=True)
    start_time = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    # expiration_time = Column(DateTime, default=lambda: datetime.now(timezone.utc) + timedelta(days=7))
    # expiration_time = Column(DateTime, default=lambda: datetime.now(timezone.utc) + timedelta(minutes=20))
    expiration_time = Column(DateTime, default=lambda: datetime.now(timezone.utc) + timedelta(minutes=2))




    @staticmethod
    def get_expiration_time():
        return datetime.now(timezone.utc) + timedelta(days=7)