from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey, DateTime, Text, JSON
)
from sqlalchemy.orm import relationship
from app.db import Base

class TransactionSummary(Base):
    __tablename__ = "transaction_summaries"

    id = Column(Integer, primary_key=True, index=True)
    terminal_id = Column(Integer, ForeignKey("terminals.id", ondelete="CASCADE"), nullable=False, index=True)

    ciudad = Column(String(100), nullable=False)
    canal = Column(String(100), nullable=False)
    franquicias = Column(Text, nullable=False)
    total_transacciones = Column(Integer, nullable=False)
    volumen_total = Column(Float, nullable=False)

    moneda = Column(String(10), default="COP")
    observaciones = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    terminal = relationship("Terminal", back_populates="transaction_summary")

    def __repr__(self):
        return f"<TransactionSummary {self.terminal_id} {self.total_transacciones} txs>"