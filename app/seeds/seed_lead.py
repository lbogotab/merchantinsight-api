from datetime import date
from random import uniform, choice
from app.db import SessionLocal
from app.models.lead import Lead
from app.models.commerce import Commerce

def seed_leads():
    db = SessionLocal()
    if db.query(Lead).count() > 0:
        print("⚠️ Leads already seeded.")
        db.close()
        return

    leads_data = [
        # --- Panadería La 85 S.A.S. ---
        {
            "lead_code": "LEAD-2025-1001",
            "contact_name": "Panadería La 85 S.A.S.",
            "created_date": date(2025, 2, 27),
            "origin": "Campaña digital",
            "product_interest": "QR",
            "current_status": "En seguimiento",
            "assigned_advisor": "Carlos Gómez",
            "comments": "Pendiente de validación documental.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1002",
            "contact_name": "Panadería La 85 S.A.S.",
            "created_date": date(2025, 2, 22),
            "origin": "Portal web",
            "product_interest": "Datáfono",
            "current_status": "Cerrado no efectivo",
            "assigned_advisor": "María Rincón",
            "comments": "Solicita demo del producto.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1003",
            "contact_name": "Panadería La 85 S.A.S.",
            "created_date": date(2025, 2, 17),
            "origin": "Referido",
            "product_interest": "Link de pagos",
            "current_status": "Nuevo",
            "assigned_advisor": "Andrea Ruiz",
            "comments": "Pendiente de validación documental.",
            "commerce_code": None,
        },

        # --- Ferretería El Tornillo Ltda. ---
        {
            "lead_code": "LEAD-2025-1004",
            "contact_name": "Ferretería El Tornillo Ltda.",
            "created_date": date(2025, 8, 3),
            "origin": "Referido",
            "product_interest": "Pasarela eCommerce",
            "current_status": "Convertido",
            "assigned_advisor": "María Rincón",
            "comments": "Pendiente de validación documental.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1005",
            "contact_name": "Ferretería El Tornillo Ltda.",
            "created_date": date(2025, 8, 5),
            "origin": "Aliado comercial",
            "product_interest": "QR",
            "current_status": "En seguimiento",
            "assigned_advisor": "Carlos Gómez",
            "comments": "Contactado por correo electrónico.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1006",
            "contact_name": "Ferretería El Tornillo Ltda.",
            "created_date": date(2025, 2, 22),
            "origin": "Campaña digital",
            "product_interest": "Pasarela eCommerce",
            "current_status": "Nuevo",
            "assigned_advisor": "Laura Jiménez",
            "comments": "Contactado por correo electrónico.",
            "commerce_code": None,
        },

        # --- Algunos ejemplos más (resumen) ---
        {
            "lead_code": "LEAD-2025-1012",
            "contact_name": "Tienda Mi Barrio E.U.",
            "created_date": date(2025, 3, 25),
            "origin": "Asesor territorial",
            "product_interest": "Pasarela eCommerce",
            "current_status": "Convertido",
            "assigned_advisor": "Luis Vargas",
            "comments": "Interesado en tarifas reducidas por volumen de transacciones.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1016",
            "contact_name": "Licores del Norte",
            "created_date": date(2025, 5, 16),
            "origin": "Referido",
            "product_interest": "Link de pagos",
            "current_status": "Convertido",
            "assigned_advisor": "Luis Vargas",
            "comments": "Requiere capacitación sobre el uso del SmartPOS.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1021",
            "contact_name": "Restaurante El Carbón",
            "created_date": date(2025, 2, 28),
            "origin": "Portal web",
            "product_interest": "QR",
            "current_status": "Convertido",
            "assigned_advisor": "María Rincón",
            "comments": "Contactado por correo electrónico.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1022",
            "contact_name": "Zapatería El Paso",
            "created_date": date(2025, 3, 22),
            "origin": "Asesor territorial",
            "product_interest": "Datáfono",
            "current_status": "Convertido",
            "assigned_advisor": "Andrea Ruiz",
            "comments": "Pendiente de validación documental.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1042",
            "contact_name": "Droguería El Sol",
            "created_date": date(2025, 9, 7),
            "origin": "Referido",
            "product_interest": "Link de pagos",
            "current_status": "Convertido",
            "assigned_advisor": "Carlos Gómez",
            "comments": "Solicita demo del producto.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1047",
            "contact_name": "Supermercado El Campo",
            "created_date": date(2025, 8, 3),
            "origin": "Portal web",
            "product_interest": "SmartPOS",
            "current_status": "Convertido",
            "assigned_advisor": "Laura Jiménez",
            "comments": "Pendiente de validación documental.",
            "commerce_code": None,
        },
        {
            "lead_code": "LEAD-2025-1055",
            "contact_name": "Ferretería La Llave",
            "created_date": date(2025, 5, 16),
            "origin": "Portal web",
            "product_interest": "Pasarela eCommerce",
            "current_status": "Convertido",
            "assigned_advisor": "María Rincón",
            "comments": "Solicita demo del producto.",
            "commerce_code": None,
        },
    ]

    # --- Enriquecimiento automático ---
    for data in leads_data:
        status = data["current_status"]
        if status == "Convertido":
            stage = "Cerrado - Ganado"
            probability = round(uniform(0.85, 0.95), 2)
            expected_value = round(uniform(10000000, 25000000), 2)
            converted_to_contract = True
            conversion_date = date(2025, data["created_date"].month, min(data["created_date"].day + 5, 28))
            lost_reason = None
            next_action = "Seguimiento postventa"
        elif status == "Cerrado no efectivo":
            stage = "Cerrado - Perdido"
            probability = round(uniform(0.05, 0.25), 2)
            expected_value = round(uniform(3000000, 8000000), 2)
            converted_to_contract = False
            conversion_date = None
            lost_reason = choice(["Desinterés del comercio", "Competencia con mejores tarifas", "Falta de documentación"])
            next_action = "Recontactar en próxima campaña"
        elif status == "En seguimiento":
            stage = "Negociación"
            probability = round(uniform(0.5, 0.75), 2)
            expected_value = round(uniform(6000000, 18000000), 2)
            converted_to_contract = False
            conversion_date = None
            lost_reason = None
            next_action = "Llamada de seguimiento"
        else:  # "Nuevo"
            stage = "Inicial"
            probability = round(uniform(0.2, 0.4), 2)
            expected_value = round(uniform(5000000, 10000000), 2)
            converted_to_contract = False
            conversion_date = None
            lost_reason = None
            next_action = "Contactar para primera validación"

        commerce = db.query(Commerce).filter(Commerce.code == data["commerce_code"]).first() if data["commerce_code"] else None
        lead = Lead(
            lead_code=data["lead_code"],
            contact_name=data["contact_name"],
            created_date=data["created_date"],
            origin=data["origin"],
            product_interest=data["product_interest"],
            current_status=data["current_status"],
            assigned_advisor=data["assigned_advisor"],
            comments=data["comments"],
            probability=probability,
            stage=stage,
            expected_value=expected_value,
            conversion_date=conversion_date,
            converted_to_contract=converted_to_contract,
            lost_reason=lost_reason,
            next_action=next_action,
            commerce_id=commerce.id if commerce else None,
        )
        db.add(lead)

    db.commit()
    db.close()
    print("✅ Leads iniciales creados correctamente.")