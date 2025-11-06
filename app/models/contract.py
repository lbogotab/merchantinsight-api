from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Date, Float, Text, func, DateTime
from datetime import datetime, date
from app.db import Base

class Contract(Base):
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    contract_code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    commerce_id: Mapped[int] = mapped_column(ForeignKey("commerces.id"), nullable=False)

    signing_date: Mapped[date] = mapped_column(Date)
    main_product: Mapped[str] = mapped_column(String(100))
    duration_months: Mapped[int] = mapped_column(Integer)
    total_value: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(50))
    sales_representative: Mapped[str] = mapped_column(String(100))
    notes: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    commerce = relationship("Commerce", back_populates="contracts")