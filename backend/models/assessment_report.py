from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
