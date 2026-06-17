import uuid

from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Integer,
    DateTime
)

from sqlalchemy.dialects.postgresql import (
    UUID,
    JSONB
)

from backend.db.database import Base

from backend.models.user import User

from datetime import datetime




class AssessmentReport(
    Base
):

    __tablename__ = (
        "assessment_reports"
    )

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    repository_name = Column(
        String,
        nullable=False
    )

    overall_score = Column(
        Integer,
        nullable=False
    )

    report_json = Column(
        JSONB,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )