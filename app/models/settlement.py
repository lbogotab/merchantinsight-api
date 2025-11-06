from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, ForeignKey, Date, Text
from app.db import Base

class Settlement(Base):
    __tablename__ = "settlements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    settlement_code: Mapped[str] = mapped_column(String(50), unique=True, index=True)

    commerce_id: Mapped[int] = mapped_column(ForeignKey("commerces.id"))
    settlement_date: Mapped[Date] = mapped_column(Date)
    transaction_count: Mapped[int] = mapped_column(Integer)
    total_amount: Mapped[float] = mapped_column(Float)
    commission_rate: Mapped[float] = mapped_column(Float)
    retained_amount: Mapped[float] = mapped_column(Float)
    net_amount: Mapped[float] = mapped_column(Float)
    account_type: Mapped[str] = mapped_column(String(50))  # Cuenta Corriente / Ahorros
    period: Mapped[str] = mapped_column(String(20))  # Por ejemplo, “enero 2025”
    notes: Mapped[str] = mapped_column(Text, nullable=True)

    commerce = relationship("Commerce", back_populates="settlements")