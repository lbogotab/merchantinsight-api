from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Text, Float, DateTime, func
from datetime import datetime
from app.db import Base

class Commerce(Base):
    __tablename__ = "commerces"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(String(255))
    segment: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(50))
    channel: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=True)
    department: Mapped[str] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    contact_email: Mapped[str] = mapped_column(String(255), nullable=True)
    contact_phone: Mapped[str] = mapped_column(String(50), nullable=True)
    risk_level: Mapped[str] = mapped_column(String(50), nullable=True)
    avg_monthly_billing: Mapped[float] = mapped_column(Float, nullable=True)
    main_products: Mapped[str] = mapped_column(Text, nullable=True)

    terminals: Mapped[list["Terminal"]] = relationship(back_populates="commerce", cascade="all, delete-orphan")
    contracts = relationship("Contract", back_populates="commerce", cascade="all, delete-orphan")
    invoices = relationship("Invoice", back_populates="commerce", cascade="all, delete-orphan")
    incidents = relationship("Incident", back_populates="commerce", cascade="all, delete-orphan")
    leads = relationship("Lead", back_populates="commerce", cascade="all, delete-orphan")
    settlements = relationship("Settlement", back_populates="commerce", cascade="all, delete-orphan")

    observations = relationship("CommerceObservation", back_populates="commerce", cascade="all, delete-orphan")