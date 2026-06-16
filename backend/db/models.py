import uuid

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)

from sqlalchemy.dialects.postgresql import (
    UUID,
    JSONB
)

from sqlalchemy.orm import declarative_base

from datetime import datetime

Base = declarative_base()


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