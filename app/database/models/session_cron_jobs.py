import uuid
from .model_base_class import Base
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from datetime import datetime, timezone

class SessionCronJob(Base):
    __tablename__ = "session_cron_jobs"

    cron_job_id = Column(pgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    last_checked = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    sessions_deleted = Column(Integer, nullable=False, default=0)
