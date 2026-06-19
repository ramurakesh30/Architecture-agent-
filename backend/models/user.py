import uuid

from sqlalchemy import Column, Index, String
from sqlalchemy.dialects.postgresql import UUID

from backend.db.database import Base


class User(Base):
    __tablename__ = "users"

    __table_args__ = (Index("idx_users_email", "email"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)
