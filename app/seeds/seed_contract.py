from app.db import SessionLocal
from app.models.commerce import Commerce
from app.models.contract import Contract
from datetime import datetime

def seed_contracts():
    db = SessionLocal()
    try:
        if db.query(Contract).count() > 0:
            print("ℹ️ Contratos ya existentes, sin cambios.")
            return

        contracts_data = [
            ("CTR-2025-1001", "C-0001", "2025-07-31", "SmartPOS", 24, 21573195, "En renovación", "Julián Pérez", "Contrato con liquidación mensual."),
            ("CTR-2025-1002", "C-0002", "2025-06-07", "SmartPOS", 36, 11496546, "Rescindido", "Andrea Ruiz", "Renovación automática anual."),
            ("CTR-2025-1003", "C-0003", "2025-02-16", "Link de pagos", 24, 17869297, "Finalizado", "Julián Pérez", "Renovación automática anual."),
            ("CTR-2025-1004", "C-0004", "2025-07-26", "Pasarela eCommerce", 24, 6111369, "Finalizado", "Luis Vargas", "Contrato con descuento por volumen transaccional."),
            ("CTR-2025-1005", "C-0005", "2025-06-24", "SmartPOS", 36, 20154456, "Rescindido", "María Rincón", "Contrato con descuento por volumen transaccional."),
            ("CTR-2025-1006", "C-0006", "2025-04-19", "QR", 12, 14836082, "Activo", "Laura Jiménez", "Contrato con liquidación mensual."),
            ("CTR-2025-1007", "C-0007", "2025-08-17", "SmartPOS", 24, 12982010, "Activo", "Luis Vargas", "Contrato bajo modalidad de arrendamiento."),
            ("CTR-2025-1008", "C-0008", "2025-04-18", "QR", 36, 15095689, "Rescindido", "Julián Pérez", "Contrato con descuento por volumen transaccional."),
            ("CTR-2025-1009", "C-0009", "2025-05-06", "QR", 12, 10226303, "Activo", "Carlos Gómez", "Contrato con liquidación mensual."),
            ("CTR-2025-1010", "C-0010", "2025-09-05", "Link de pagos", 36, 24594668, "Activo", "Laura Jiménez", "Sujeto a revisión de comisiones preferenciales."),
            ("CTR-2025-1011", "C-0011", "2025-02-22", "Link de pagos", 36, 9938283, "En renovación", "Andrea Ruiz", "Contrato con descuento por volumen transaccional."),
            ("CTR-2025-1012", "C-0012", "2025-05-17", "Link de pagos", 36, 23961558, "Rescindido", "María Rincón", "Contrato con descuento por volumen transaccional."),
            ("CTR-2025-1013", "C-0013", "2025-05-28", "QR", 36, 12198184, "En renovación", "Carlos Gómez", "Incluye soporte técnico 24/7."),
            ("CTR-2025-1014", "C-0014", "2025-05-28", "Pasarela eCommerce", 24, 6588879, "Rescindido", "María Rincón", "Contrato con descuento por volumen transaccional."),
            ("CTR-2025-1015", "C-0015", "2025-04-03", "Datáfono", 36, 8996850, "Rescindido", "Laura Jiménez", "Renovación automática anual."),
            ("CTR-2025-1016", "C-0016", "2025-07-03", "SmartPOS", 36, 24989434, "Rescindido", "María Rincón", "Incluye soporte técnico 24/7."),
            ("CTR-2025-1017", "C-0017", "2025-04-13", "Link de pagos", 12, 9076779, "Finalizado", "Laura Jiménez", "Contrato bajo modalidad de arrendamiento."),
            ("CTR-2025-1018", "C-0018", "2025-04-20", "SmartPOS", 12, 7990796, "Rescindido", "Julián Pérez", "Pendiente actualización de tarifas."),
            ("CTR-2025-1019", "C-0019", "2025-01-14", "Datáfono", 12, 12759863, "Rescindido", "Luis Vargas", "Contrato con descuento por volumen transaccional."),
            ("CTR-2025-1020", "C-0020", "2025-06-05", "Datáfono", 12, 6584281, "Finalizado", "Laura Jiménez", "Pendiente actualización de tarifas."),
            ("CTR-2025-1021", "C-0021", "2025-08-26", "SmartPOS", 36, 24371088, "Finalizado", "Laura Jiménez", "Renovación automática anual."),
            ("CTR-2025-1022", "C-0022", "2025-04-16", "Pasarela eCommerce", 24, 23541476, "En renovación", "Julián Pérez", "Incluye soporte técnico 24/7."),
            ("CTR-2025-1023", "C-0023", "2025-06-16", "QR", 36, 15848552, "Rescindido", "María Rincón", "Contrato con liquidación mensual."),
            ("CTR-2025-1024", "C-0024", "2025-08-01", "QR", 12, 24907443, "Finalizado", "María Rincón", "Sujeto a revisión de comisiones preferenciales."),
            ("CTR-2025-1025", "C-0025", "2025-08-13", "Datáfono", 36, 11478133, "Rescindido", "Luis Vargas", "Contrato bajo modalidad de arrendamiento."),
        ]

        contracts_to_add = []
        for (
            contract_code, commerce_code, signing_date, main_product, duration_months,
            total_value, status, sales_representative, notes
        ) in contracts_data:
            commerce = db.query(Commerce).filter(Commerce.code == commerce_code).first()
            if not commerce:
                print(f"⚠️ Comercio {commerce_code} no encontrado, omitiendo {contract_code}.")
                continue

            contracts_to_add.append(
                Contract(
                    contract_code=contract_code,
                    commerce_id=commerce.id,
                    signing_date=datetime.strptime(signing_date, "%Y-%m-%d").date(),
                    main_product=main_product,
                    duration_months=duration_months,
                    total_value=total_value,
                    status=status,
                    sales_representative=sales_representative,
                    notes=notes,
                )
            )

        db.add_all(contracts_to_add)
        db.commit()
        print("✅ Contratos iniciales creados correctamente.")

    finally:
        db.close()