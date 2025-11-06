from datetime import datetime
from app.db import SessionLocal
from app.models.support_ticket import SupportTicket
from app.models.commerce import Commerce

def seed_support_tickets():
    db = SessionLocal()

    data = [
        # SUP-2025-5001
        ("SUP-2025-5001", "C-0009", "2025-07-05", "Actualización de software", "En sitio",
         "Luis Salazar", "Cancelado", 2.4, "Instalación completada parcialmente por restricción de acceso remoto.",
         "Se actualizó firmware de terminal principal y verificó conectividad con switch de red. Se recomienda revisión del enlace WAN en próxima visita.", "Alta"),

        # SUP-2025-5002
        ("SUP-2025-5002", "C-0013", "2025-05-22", "Mantenimiento preventivo", "En sitio",
         "Luis Salazar", "Cancelado", 1.6, "Se ejecutó limpieza de terminales e inspección de lector EMV.",
         "Capacitación al personal sobre uso de SmartPOS Clover Flex. Cliente manifestó mejoras en estabilidad de red WiFi.", "Media"),

        # SUP-2025-5003
        ("SUP-2025-5003", "C-0013", "2025-03-29", "Reinstalación", "En sitio",
         "Andrés Pardo", "Cancelado", 4.0, "Se reemplazó equipo POS modelo VX520 por terminal Clover Flex.",
         "Configuración inicial completada, faltante validación de clave comercio-terminal.", "Alta"),

        # SUP-2025-5004
        ("SUP-2025-5004", "C-0005", "2025-04-06", "Actualización de software", "Remoto",
         "Diego Arango", "Programado", 3.8, "Actualización antifraude v3.2 aplicada en entorno de prueba.",
         "Instalación de nuevo software antifraude. Pendiente validación de logs de detección por cliente.", "Alta"),

        # SUP-2025-5005
        ("SUP-2025-5005", "C-0012", "2025-04-03", "Revisión en sitio", "En sitio",
         "Javier Méndez", "Programado", 3.3, "Se realizó diagnóstico físico del lector de tarjetas NFC.",
         "Instalación de software antifraude v3.2. Terminal actualizada sin incidencias críticas.", "Media"),

        # SUP-2025-5006
        ("SUP-2025-5006", "C-0012", "2025-05-31", "Capacitación", "Remoto",
         "Natalia Becerra", "Completado", 2.0, "Capacitación sobre conciliación y reportes diarios.",
         "Sesión de capacitación virtual completada. Satisfacción alta reportada por el comercio.", "Baja"),

        # SUP-2025-5007
        ("SUP-2025-5007", "C-0018", "2025-04-16", "Mantenimiento preventivo", "Remoto",
         "Camila Torres", "Completado", 1.5, "Verificación del log de transacciones y estado del lector NFC.",
         "Soporte en línea para conciliación de transacciones y testeo de reversos automáticos.", "Media"),

        # SUP-2025-5008
        ("SUP-2025-5008", "C-0018", "2025-07-18", "Mantenimiento preventivo", "En sitio",
         "Andrés Pardo", "Programado", 1.5, "Inspección física de conectores y firmware en terminal modelo D210.",
         "Se actualizó firmware de terminal y verificó conectividad con switch. Terminal quedó operativa.", "Alta"),

        # SUP-2025-5009
        ("SUP-2025-5009", "C-0015", "2025-08-03", "Revisión en sitio", "En sitio",
         "Andrés Pardo", "Cancelado", 3.9, "Se realizaron pruebas de conectividad y reemplazo de fuente de poder.",
         "Revisión en sitio completada sin hallazgos críticos. Cliente solicita monitoreo 24h.", "Baja"),

        # SUP-2025-5010
        ("SUP-2025-5010", "C-0011", "2025-04-26", "Capacitación", "Remoto",
         "Diego Arango", "Programado", 2.2, "Asistencia remota para restablecer conexión con pasarela.",
         "Sesión remota de 2h con ejercicios prácticos sobre reversos automáticos y conciliación.", "Media"),

        # SUP-2025-5011
        ("SUP-2025-5011", "C-0011", "2025-06-18", "Actualización de software", "Remoto",
         "Javier Méndez", "En curso", 1.9, "Actualización parcial de módulos de seguridad y cifrado TLS 1.3.",
         "Asistencia remota en progreso. Pendiente validación de logs de aplicación.", "Alta"),
    ]

    for (
        support_code,
        commerce_code,
        fecha_atencion,
        tipo_servicio,
        modo_atencion,
        tecnico_asignado,
        estado,
        duracion_horas,
        resultado,
        observaciones,
        prioridad,
    ) in data:
        commerce = db.query(Commerce).filter(Commerce.code == commerce_code).first()
        if not commerce:
            continue

        ticket = SupportTicket(
            support_code=support_code,
            commerce_id=commerce.id,
            fecha_atencion=datetime.strptime(fecha_atencion, "%Y-%m-%d"),
            tipo_servicio=tipo_servicio,
            modo_atencion=modo_atencion,
            tecnico_asignado=tecnico_asignado,
            estado=estado,
            duracion_horas=duracion_horas,
            resultado=resultado,
            observaciones=observaciones,
            prioridad=prioridad,
        )
        db.add(ticket)

    db.commit()
    db.close()
    print("✅ Soportes detallados creados correctamente.")