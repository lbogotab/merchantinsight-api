from sqlalchemy import Column, Integer, String, Date, Float, Text, ForeignKey, DateTime
from datetime import datetime
from app.db import Base

class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id = Column(Integer, primary_key=True, index=True)
    support_code = Column(String(50), unique=True, nullable=False)
    commerce_id = Column(Integer, ForeignKey("commerces.id", ondelete="CASCADE"), nullable=False)
    fecha_atencion = Column(Date, nullable=False)

    tipo_servicio = Column(String(100), nullable=False)
    modo_atencion = Column(String(50), nullable=False, default="En sitio")  # remoto / en sitio
    tecnico_asignado = Column(String(100), nullable=False)
    estado = Column(String(50), nullable=False)
    duracion_horas = Column(Float, nullable=False)

    resultado = Column(Text, nullable=True)
    observaciones = Column(Text, nullable=True)
    prioridad = Column(String(20), default="Media")  # Alta / Media / Baja

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)