from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

class CommerceObservation(Base):
    __tablename__ = "commerce_observations"

    id = Column(Integer, primary_key=True, index=True)
    commerce_id = Column(Integer, ForeignKey("commerces.id", ondelete="CASCADE"), nullable=False)
    comment = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    commerce = relationship("Commerce", back_populates="observations")