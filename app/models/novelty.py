# app/models/novedad.py
from datetime import datetime, date
from sqlalchemy import (
    Column, Integer, String, Enum, Date, Text, ForeignKey,
    UniqueConstraint, Index, DateTime
)
from sqlalchemy.orm import relationship
from app.db import Base

# Catálogos controlados
TIPOS_NOVEDAD = (
    "Alta de terminal",
    "Baja de terminal",
    "Cambio de estado",
    "Cambio de canal o modelo",
    "Reasignación comercial",
)

RESPONSABLES = ("Credibanco", "Comercio")

class Novedad(Base):
    __tablename__ = "novedades"

    id = Column(Integer, primary_key=True, index=True)
    # Código legible + único para trazabilidad (útil en auditoría)
    novedad_code = Column(String(64), unique=True, nullable=False, index=True)

    terminal_id = Column(Integer, ForeignKey("terminals.id", ondelete="CASCADE"), nullable=False, index=True)
    fecha = Column(Date, nullable=False, index=True)

    # Enums tipados para consistencia
    tipo = Column(Enum(*TIPOS_NOVEDAD, name="tipo_novedad"), nullable=False, index=True)
    responsable = Column(Enum(*RESPONSABLES, name="responsable_novedad"), nullable=False)

    observacion = Column(Text, nullable=True)

    # Metadatos
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Evita duplicados lógicos (la misma acción en la misma fecha sobre la misma terminal)
    __table_args__ = (
        UniqueConstraint("terminal_id", "fecha", "tipo", name="uq_novedades_terminal_fecha_tipo"),
        Index("ix_novedades_terminal_fecha", "terminal_id", "fecha"),
    )

    # Relación inversa
    terminal = relationship("Terminal", back_populates="novedades")

    def __repr__(self) -> str:
        return f"<Novedad {self.novedad_code} {self.tipo} {self.fecha}>"