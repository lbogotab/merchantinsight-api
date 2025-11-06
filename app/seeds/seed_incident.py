from datetime import date, timedelta
from app.db import SessionLocal
from app.models.incident import Incident
from app.models.commerce import Commerce

def seed_incidents():
    db = SessionLocal()
    if db.query(Incident).count() > 0:
        print("⚠️  Incidents already seeded.")
        db.close()
        return

    incidents_data = [
        {
            "incident_code": "INC-2025-4001",
            "commerce_code": "C-0002",
            "reported_date": date(2025, 3, 23),
            "resolved_date": date(2025, 3, 25),
            "resolution_time_days": 2,
            "category": "Error de liquidación",
            "status": "Resuelta",
            "severity": "Alta",
            "impact_level": "Moderado",
            "root_cause": "Duplicación de transacción por error en sincronización de lotes.",
            "corrective_action": "Actualización del middleware de conciliación.",
            "description": "Transacción duplicada reportada por cliente final.",
            "responsible_area": "Soporte de Red",
            "customer_impact": True,
            "financial_impact": 150000.0,
            "observations": "Se implementó alerta preventiva en sistema de liquidación."
        },
        {
            "incident_code": "INC-2025-4002",
            "commerce_code": "C-0009",
            "reported_date": date(2025, 1, 1),
            "resolved_date": None,
            "resolution_time_days": None,
            "category": "Fallo de conexión",
            "status": "Abierta",
            "severity": "Media",
            "impact_level": "Moderado",
            "root_cause": "Intermitencia en red 4G de proveedor local.",
            "corrective_action": "Programar mantenimiento en enlace secundario.",
            "description": "Solicitud de mantenimiento preventivo en punto de venta.",
            "responsible_area": "Soporte de Red",
            "customer_impact": False,
            "financial_impact": 0.0,
            "observations": "Se detectaron 3 reconexiones fallidas previas."
        },
        {
            "incident_code": "INC-2025-4003",
            "commerce_code": "C-0003",
            "reported_date": date(2025, 1, 4),
            "resolved_date": date(2025, 1, 5),
            "resolution_time_days": 1,
            "category": "Transacción duplicada",
            "status": "Cerrada sin acción",
            "severity": "Baja",
            "impact_level": "Bajo",
            "root_cause": "Error de comunicación entre API de pagos y terminal.",
            "corrective_action": "Reinicio remoto del dispositivo afectado.",
            "description": "Terminal presentó error intermitente en conexión 4G.",
            "responsible_area": "Área Técnica",
            "customer_impact": False,
            "financial_impact": 0.0,
            "observations": "Revisión completada sin anomalías en logs."
        },
        {
            "incident_code": "INC-2025-4004",
            "commerce_code": "C-0014",
            "reported_date": date(2025, 3, 6),
            "resolved_date": date(2025, 3, 10),
            "resolution_time_days": 4,
            "category": "Falla en terminal",
            "status": "Resuelta",
            "severity": "Alta",
            "impact_level": "Alto",
            "root_cause": "Desincronización de certificados TLS en pasarela.",
            "corrective_action": "Renovación y despliegue de certificados.",
            "description": "Fallo temporal de comunicación con pasarela de pagos.",
            "responsible_area": "Atención Comercios",
            "customer_impact": True,
            "financial_impact": 350000.0,
            "observations": "Requiere verificación adicional del proveedor de hosting."
        },
        {
            "incident_code": "INC-2025-4005",
            "commerce_code": "C-0024",
            "reported_date": date(2025, 8, 29),
            "resolved_date": date(2025, 9, 2),
            "resolution_time_days": 4,
            "category": "Falla en terminal",
            "status": "Resuelta",
            "severity": "Media",
            "impact_level": "Moderado",
            "root_cause": "Pérdida temporal de conexión con API de pagos.",
            "corrective_action": "Reinicio del balanceador y actualización de firmware.",
            "description": "Fallo temporal de comunicación con pasarela de pagos.",
            "responsible_area": "Atención Comercios",
            "customer_impact": True,
            "financial_impact": 120000.0,
            "observations": "Se programó mantenimiento de seguimiento semanal."
        },
        {
            "incident_code": "INC-2025-4006",
            "commerce_code": "C-0024",
            "reported_date": date(2025, 4, 16),
            "resolved_date": date(2025, 4, 21),
            "resolution_time_days": 5,
            "category": "Reclamación de cobro",
            "status": "Resuelta",
            "severity": "Alta",
            "impact_level": "Moderado",
            "root_cause": "Doble liquidación causada por actualización concurrente.",
            "corrective_action": "Bloqueo temporal de operaciones durante sincronización.",
            "description": "Solicitud de mantenimiento preventivo en punto de venta.",
            "responsible_area": "Área Técnica",
            "customer_impact": True,
            "financial_impact": 180000.0,
            "observations": "Caso cerrado tras validación del área de conciliación."
        },
        {
            "incident_code": "INC-2025-4007",
            "commerce_code": "C-0004",
            "reported_date": date(2025, 9, 6),
            "resolved_date": date(2025, 9, 7),
            "resolution_time_days": 1,
            "category": "Reclamación de cobro",
            "status": "Cerrada sin acción",
            "severity": "Baja",
            "impact_level": "Bajo",
            "root_cause": "Error de interpretación de liquidación por el usuario.",
            "corrective_action": "Educación al comercio y envío de instructivo.",
            "description": "Fallo temporal de comunicación con pasarela de pagos.",
            "responsible_area": "Atención Comercios",
            "customer_impact": False,
            "financial_impact": 0.0,
            "observations": "Cierre validado con soporte comercial."
        },
        {
            "incident_code": "INC-2025-4008",
            "commerce_code": "C-0004",
            "reported_date": date(2025, 4, 3),
            "resolved_date": None,
            "resolution_time_days": None,
            "category": "Solicitud de mantenimiento",
            "status": "Abierta",
            "severity": "Media",
            "impact_level": "Moderado",
            "root_cause": "Desgaste físico del dispositivo principal.",
            "corrective_action": "Pendiente envío de nuevo terminal.",
            "description": "Reclamo por cobro no autorizado en terminal.",
            "responsible_area": "Atención Comercios",
            "customer_impact": True,
            "financial_impact": 250000.0,
            "observations": "Incidente pendiente de validación logística."
        },
        {
            "incident_code": "INC-2025-4009",
            "commerce_code": "C-0025",
            "reported_date": date(2025, 3, 29),
            "resolved_date": date(2025, 3, 30),
            "resolution_time_days": 1,
            "category": "Transacción duplicada",
            "status": "Resuelta",
            "severity": "Alta",
            "impact_level": "Alto",
            "root_cause": "Procesamiento duplicado por error de timeout.",
            "corrective_action": "Implementación de reintentos idempotentes.",
            "description": "Solicitud de mantenimiento preventivo en punto de venta.",
            "responsible_area": "Soporte de Red",
            "customer_impact": True,
            "financial_impact": 230000.0,
            "observations": "Revisar casos similares en marzo."
        },
        {
            "incident_code": "INC-2025-4010",
            "commerce_code": "C-0025",
            "reported_date": date(2025, 8, 22),
            "resolved_date": date(2025, 8, 27),
            "resolution_time_days": 5,
            "category": "Fallo de conexión",
            "status": "Resuelta",
            "severity": "Media",
            "impact_level": "Moderado",
            "root_cause": "Pérdida de sincronización con SAP.",
            "corrective_action": "Reindexación manual de registros y control de heartbeat.",
            "description": "Liquidación del día no reflejada en sistema SAP.",
            "responsible_area": "Área Técnica",
            "customer_impact": True,
            "financial_impact": 95000.0,
            "observations": "Requiere monitoreo de 72 horas posteriores."
        },
        {
            "incident_code": "INC-2025-4011",
            "commerce_code": "C-0013",
            "reported_date": date(2025, 7, 6),
            "resolved_date": date(2025, 7, 11),
            "resolution_time_days": 5,
            "category": "Falla en terminal",
            "status": "Resuelta",
            "severity": "Alta",
            "impact_level": "Alto",
            "root_cause": "Error en configuración del driver POS.",
            "corrective_action": "Reinstalación del firmware de controladores.",
            "description": "Solicitud de mantenimiento preventivo en punto de venta.",
            "responsible_area": "Área Técnica",
            "customer_impact": True,
            "financial_impact": 200000.0,
            "observations": "Caso revisado con fabricante del hardware."
        },
        {
            "incident_code": "INC-2025-4012",
            "commerce_code": "C-0011",
            "reported_date": date(2025, 5, 28),
            "resolved_date": None,
            "resolution_time_days": None,
            "category": "Fallo de conexión",
            "status": "En análisis",
            "severity": "Media",
            "impact_level": "Moderado",
            "root_cause": "Pendiente de diagnóstico de logs del switch local.",
            "corrective_action": "Se solicitó revisión a proveedor externo.",
            "description": "Solicitud de mantenimiento preventivo en punto de venta.",
            "responsible_area": "Soporte de Red",
            "customer_impact": False,
            "financial_impact": 0.0,
            "observations": "Escalada a nivel 2 de soporte."
        },
        {
            "incident_code": "INC-2025-4013",
            "commerce_code": "C-0017",
            "reported_date": date(2025, 3, 20),
            "resolved_date": date(2025, 3, 21),
            "resolution_time_days": 1,
            "category": "Reclamación de cobro",
            "status": "Cerrada sin acción",
            "severity": "Baja",
            "impact_level": "Bajo",
            "root_cause": "Cobro legítimo validado en logs de liquidación.",
            "corrective_action": "Comunicación al comercio con evidencia del proceso.",
            "description": "Solicitud de mantenimiento preventivo en punto de venta.",
            "responsible_area": "Atención Comercios",
            "customer_impact": False,
            "financial_impact": 0.0,
            "observations": "Caso cerrado tras validación conjunta con área comercial."
        }
    ]

    for data in incidents_data:
        commerce = db.query(Commerce).filter(Commerce.code == data["commerce_code"]).first()
        if commerce:
            incident = Incident(**{k: v for k, v in data.items() if k != "commerce_code"})
            incident.commerce_id = commerce.id
            db.add(incident)

    db.commit()
    db.close()
    print("✅ Incidentes iniciales creados correctamente.")