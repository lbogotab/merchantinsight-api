from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Date, Text, Float, Boolean, DateTime, func
from datetime import datetime, date
from app.db import Base

class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    incident_code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    commerce_id: Mapped[int] = mapped_column(ForeignKey("commerces.id"), nullable=False)

    reported_date: Mapped[date] = mapped_column(Date)
    resolved_date: Mapped[date] = mapped_column(Date, nullable=True)
    resolution_time_days: Mapped[float] = mapped_column(Float, nullable=True)

    category: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(50))
    severity: Mapped[str] = mapped_column(String(50), default="Media") 
    impact_level: Mapped[str] = mapped_column(String(50), default="Moderado")  
    root_cause: Mapped[str] = mapped_column(Text, nullable=True) 
    corrective_action: Mapped[str] = mapped_column(Text, nullable=True) 

    description: Mapped[str] = mapped_column(Text)
    responsible_area: Mapped[str] = mapped_column(String(100))
    customer_impact: Mapped[bool] = mapped_column(Boolean, default=False) 
    financial_impact: Mapped[float] = mapped_column(Float, default=0.0) 

    observations: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    commerce = relationship("Commerce", back_populates="incidents")