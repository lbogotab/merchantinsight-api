from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime, Text, func
from datetime import datetime
from app.db import Base

class Terminal(Base):
    __tablename__ = "terminals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    terminal_code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    commerce_id: Mapped[int] = mapped_column(ForeignKey("commerces.id"), nullable=False)
    city: Mapped[str] = mapped_column(String(100))
    model: Mapped[str] = mapped_column(String(150))
    status: Mapped[str] = mapped_column(String(100))
    channel: Mapped[str] = mapped_column(String(100))
    franchises: Mapped[str] = mapped_column(Text)
    assigned_by: Mapped[str] = mapped_column(String(100), default="Credibanco")
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    commerce: Mapped["Commerce"] = relationship(back_populates="terminals")
    novedades = relationship("Novedad", back_populates="terminal", cascade="all, delete-orphan")
    transaction_summary = relationship(
    "TransactionSummary", back_populates="terminal", uselist=False, cascade="all, delete-orphan"
)