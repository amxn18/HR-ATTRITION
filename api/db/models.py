import uuid
from sqlalchemy import Column, Integer, Float, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID, JSONB

from api.db.base import Base

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(
        UUID(as_uuid=True),
        primary_key = True,
        default = uuid.uuid4,
    )

    input_data = Column(
        JSONB,
        nullable = False
    )

    prediction = Column(
        Integer, 
        nullable=False
    )
    probability = Column(
        Float,
        nullable=False
    )

    latency_ms = Column(
        Float,
        nullable=False
    )
    model_name = Column(
        String,
        nullable=False
    )
    model_alias = Column(
        String,
        nullable=False
    )
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
