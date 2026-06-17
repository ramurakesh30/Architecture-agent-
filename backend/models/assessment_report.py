from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, ForeignKey

user_id = Column(

    UUID(as_uuid=True),

    ForeignKey("users.id"),

    nullable=False
)