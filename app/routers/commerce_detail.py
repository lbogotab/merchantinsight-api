from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.commerce import Commerce
from app.models.terminal import Terminal
from app.models.contract import Contract
from app.models.invoice import Invoice
from app.models.incident import Incident
from app.models.settlement import Settlement
from app.models.support_ticket import SupportTicket
from app.models.lead import Lead
from app.models.novelty import Novedad
from app.models.transaction import TransactionSummary
from app.models.commerce_observation import CommerceObservation

router = APIRouter(prefix="/commerces", tags=["Commerces"])


@router.get("/detail-full/{commerce_code}")
def get_commerce_detail(commerce_code: str, db: Session = Depends(get_db)):
    """
    Devuelve una vista consolidada del comercio incluyendo:
    datos generales, terminales, contratos, facturas, incidentes,
    leads, conciliaciones, tickets de soporte, y novedades.
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
                "volumen_total": resumen_tx.volumen_total if resumen_tx else 0.0,
                "ciudad": resumen_tx.ciudad if resumen_tx else None,
                "canal": resumen_tx.canal if resumen_tx else None
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

    # -------- CONTRATOS --------
    contracts = [
        {
            "codigo": c.contract_code,
            "fecha_firma": c.signing_date,
            "producto_principal": c.main_product,
            "duracion_meses": c.duration_months,
            "valor_total": c.total_value,
            "estado": c.status,
            "representante": c.sales_representative,
            "notas": c.notes
        }
        for c in commerce.contracts
    ]

    # -------- FACTURAS --------
    invoices = [
        {
            "codigo": f.invoice_code,
            "fecha_emision": f.issued_date,
            "periodo": f.billing_period,
            "importe_bruto": f.gross_amount,
            "descuentos_retenciones": f.discounts_and_retentions,
            "impuestos": f.tax_value,
            "importe_neto": f.net_amount,
            "estado": f.status,
            "metodo_pago": f.payment_method,
            "recurrente": f.is_recurrent,
        }
        for f in commerce.invoices
    ]

    # -------- INCIDENTES --------
    incidents = [
        {
            "codigo": i.incident_code,
            "fecha_reporte": i.reported_date,
            "fecha_resolucion": i.resolved_date,
            "categoria": i.category,
            "estado": i.status,
            "severidad": i.severity,
            "impacto": i.impact_level,
            "causa_raiz": i.root_cause,
            "accion_correctiva": i.corrective_action,
            "area_responsable": i.responsible_area,
            "impacto_financiero": i.financial_impact,
            "observaciones": i.observations
        }
        for i in commerce.incidents
    ]

    # -------- CONCILIACIONES --------
    settlements = [
        {
            "codigo": s.settlement_code,
            "fecha": s.settlement_date,
            "transacciones": s.transaction_count,
            "monto_total": s.total_amount,
            "tasa_comision": s.commission_rate,
            "retenido": s.retained_amount,
            "neto": s.net_amount,
            "tipo_cuenta": s.account_type,
            "periodo": s.period
        }
        for s in commerce.settlements
    ]

    # -------- SOPORTES --------
    supports = db.query(SupportTicket).filter(SupportTicket.commerce_id == commerce.id).all()
    support_tickets = [
        {
            "codigo": s.support_code,
            "fecha": s.fecha_atencion,
            "tipo_servicio": s.tipo_servicio,
            "modo_atencion": s.modo_atencion,
            "tecnico": s.tecnico_asignado,
            "estado": s.estado,
            "duracion_horas": s.duracion_horas,
            "resultado": s.resultado,
            "observaciones": s.observaciones,
            "prioridad": s.prioridad
        }
        for s in supports
    ]

    # -------- LEADS --------
    leads = [
        {
            "codigo": l.lead_code,
            "fecha_creacion": l.created_date,
            "contacto": l.contact_name,
            "origen": l.origin,
            "interes": l.product_interest,
            "estado_actual": l.current_status,
            "asesor_asignado": l.assigned_advisor,
            "probabilidad": l.probability,
            "valor_estimado": l.expected_value,
            "convertido_a_contrato": l.converted_to_contract,
        }
        for l in commerce.leads
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

    # -------- RESPUESTA FINAL --------
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
        "contratos": contracts,
        "facturas": invoices,
        "incidentes": incidents,
        "conciliaciones": settlements,
        "tickets_soporte": support_tickets,
        "observaciones": observations_list
    }