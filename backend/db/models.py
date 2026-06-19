import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from backend.db.database import Base


class AssessmentReport(Base):
    __tablename__ = "assessment_reports"

    __table_args__ = (
        Index("idx_reports_user_id", "user_id"),
        Index("idx_reports_created_at", "created_at"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    repository_name = Column(String, nullable=False)

    overall_score = Column(Integer, nullable=False)

    report_json = Column(JSONB, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
