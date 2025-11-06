from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Date, Text, Boolean, Float, DateTime, func
from datetime import datetime, date
from app.db import Base

class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    lead_code: Mapped[str] = mapped_column(String(50), unique=True, index=True)

    commerce_id: Mapped[int | None] = mapped_column(ForeignKey("commerces.id"), nullable=True)
    created_date: Mapped[date] = mapped_column(Date)
    contact_name: Mapped[str] = mapped_column(String(100))  # contacto o nombre de comercio
    origin: Mapped[str] = mapped_column(String(100))
    product_interest: Mapped[str] = mapped_column(String(100))
    current_status: Mapped[str] = mapped_column(String(50))
    assigned_advisor: Mapped[str] = mapped_column(String(100))
    comments: Mapped[str] = mapped_column(Text)

    probability: Mapped[float] = mapped_column(Float, default=0.0)  # probabilidad de conversión (%)
    stage: Mapped[str] = mapped_column(String(50), default="Inicial")  # etapa del embudo comercial
    expected_value: Mapped[float] = mapped_column(Float, default=0.0)  # valor estimado del negocio
    conversion_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    converted_to_contract: Mapped[bool] = mapped_column(Boolean, default=False)
    lost_reason: Mapped[str] = mapped_column(Text, nullable=True)  # motivo de no conversión
    next_action: Mapped[str] = mapped_column(Text, nullable=True)  # siguiente acción planificada

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    commerce = relationship("Commerce", back_populates="leads")