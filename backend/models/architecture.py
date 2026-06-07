from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID

from backend.db.database import Base

class ArchitectureReview(Base):
    __tablename__ = "architecture_reviews"

    id = Column(UUID(as_uuid=True), primary_key=True)
    input_text = Column(Text)
    status = Column(String)
    result = Column(Text)