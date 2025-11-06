from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Date, Float, Text, Boolean, func, DateTime
from datetime import datetime, date
from app.db import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    invoice_code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    commerce_id: Mapped[int] = mapped_column(ForeignKey("commerces.id"), nullable=False)

    issued_date: Mapped[date] = mapped_column(Date)
    due_date: Mapped[date] = mapped_column(Date, nullable=True)
    payment_date: Mapped[date] = mapped_column(Date, nullable=True)
    billing_period: Mapped[str] = mapped_column(String(50))
    invoice_type: Mapped[str] = mapped_column(String(50), default="Mensual")
    
    gross_amount: Mapped[float] = mapped_column(Float)
    discounts_and_retentions: Mapped[float] = mapped_column(Float)
    tax_value: Mapped[float] = mapped_column(Float, default=0.0)
    net_amount: Mapped[float] = mapped_column(Float)

    status: Mapped[str] = mapped_column(String(50))
    payment_method: Mapped[str] = mapped_column(String(50), nullable=True)
    currency: Mapped[str] = mapped_column(String(10), default="COP")
    settlements_refs: Mapped[str] = mapped_column(Text)
    observations: Mapped[str] = mapped_column(Text, nullable=True)
    is_recurrent: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    commerce = relationship("Commerce", back_populates="invoices")