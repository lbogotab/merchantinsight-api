from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.commerce import Commerce
from app.models.terminal import Terminal
from app.models.invoice import Invoice
from app.models.incident import Incident
from app.models.novelty import Novedad
from app.models.transaction import TransactionSummary
from app.models.commerce_observation import CommerceObservation

router = APIRouter(prefix="/commerces", tags=["Commerces Lite"])


@router.get("/detail/{commerce_code}")
def get_commerce_detail_lite(commerce_code: str, db: Session = Depends(get_db)):
    """
    Devuelve una vista simplificada del comercio:
    comercio + terminales + facturas + incidentes + observaciones.
    Ideal para pruebas o consultas rápidas.
    """

    commerce = db.query(Commerce).filter(Commerce.code == commerce_code).first()
    if not commerce:
        raise HTTPException(status_code=404, detail=f"Comercio {commerce_code} no encontrado")

    # -------- TERMINALES --------
    terminals = []
    for t in commerce.terminals:
        resumen_tx = db.query(TransactionSummary).filter(TransactionSummary.terminal_id == t.id).first()
        novedades = db.query(Novedad).filter(Novedad.terminal_id == t.id).all()

        terminals.append({
            "codigo_terminal": t.terminal_code,
            "ciudad": t.city,
            "modelo": t.model,
            "estado": t.status,
            "canal": t.channel,
            "franquicias": t.franchises,
            "asignado_por": t.assigned_by,
            "ultima_actualizacion": t.last_update,
            "resumen_transacciones": {
                "total_transacciones": resumen_tx.total_transacciones if resumen_tx else 0,
                "volumen_total": resumen_tx.volumen_total if resumen_tx else 0.0
            } if resumen_tx else None,
            "novedades": [
                {
                    "codigo": n.novedad_code,
                    "fecha": n.fecha,
                    "tipo": n.tipo,
                    "responsable": n.responsable,
                    "observacion": n.observacion
                }
                for n in novedades
            ]
        })

    # -------- FACTURAS --------
    invoices = [
        {
            "codigo": f.invoice_code,
            "fecha_emision": f.issued_date,
            "periodo": f.billing_period,
            "importe_neto": f.net_amount,
            "estado": f.status,
        }
        for f in commerce.invoices
    ]

    # -------- INCIDENTES --------
    incidents = [
        {
            "codigo": i.incident_code,
            "fecha_reporte": i.reported_date,
            "categoria": i.category,
            "estado": i.status,
            "impacto": i.impact_level,
        }
        for i in commerce.incidents
    ]

    # -------- OBSERVACIONES --------
    observations = db.query(CommerceObservation).filter(CommerceObservation.commerce_id == commerce.id).all()
    observations_list = [
        {
            "id": o.id,
            "comentario": o.comment,
            "fecha": o.created_at
        }
        for o in observations
    ]

    # -------- RESPUESTA --------
    return {
        "comercio": {
            "codigo": commerce.code,
            "nombre": commerce.name,
            "segmento": commerce.segment,
            "estado": commerce.status,
            "canal_principal": commerce.channel,
            "direccion": commerce.address,
            "ciudad": commerce.city,
            "departamento": commerce.department,
            "correo_contacto": commerce.contact_email,
            "telefono_contacto": commerce.contact_phone,
            "nivel_riesgo": commerce.risk_level,
            "facturacion_promedio": commerce.avg_monthly_billing,
            "productos_principales": commerce.main_products,
        },
        "terminales": terminals,
        "facturas": invoices,
        "incidentes": incidents,
        "observaciones": observations_list
    }