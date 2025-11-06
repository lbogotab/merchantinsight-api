from app.db import SessionLocal
from app.models.commerce import Commerce
from app.models.terminal import Terminal

def seed_terminals():
    db = SessionLocal()
    try:
        if db.query(Terminal).count() > 0:
            print("ℹ️ Terminales ya existentes, sin cambios.")
            return

        terminals_data = [
            # --- C-0001 Panadería La 85 S.A.S. ---
            ("T-10001", "C-0001", "Bogotá", "SmartPOS Clover Flex", "En mantenimiento", "POS Físico", "Mastercard,American Express"),
            ("T-10002", "C-0001", "Bogotá", "Verifone VX520", "Activo", "POS Físico", "Mastercard,American Express"),
            ("T-10003", "C-0001", "Bogotá", "Ingenico iCT250", "Activo", "POS Físico", "Mastercard"),

            # --- C-0002 Ferretería El Tornillo Ltda. ---
            ("T-10004", "C-0002", "Medellín", "Verifone VX520", "En mantenimiento", "SmartPOS", "American Express,Visa"),
            ("T-10005", "C-0002", "Medellín", "PAX A920", "Inactivo", "SmartPOS", "Visa,American Express"),
            ("T-10006", "C-0002", "Medellín", "Ingenico iCT250", "Activo", "SmartPOS", "Visa"),

            # --- C-0003 Restaurante Sabor y Sazón S.A.S. ---
            ("T-10007", "C-0003", "Cali", "Ingenico iCT250", "En mantenimiento", "Link de Pago", "Visa,Mastercard"),

            # --- C-0004 Farmacia Vida Plena S.A. ---
            ("T-10008", "C-0004", "Barranquilla", "Ingenico iCT250", "Inactivo", "QR", "Visa,Mastercard,American Express"),
            ("T-10009", "C-0004", "Barranquilla", "PAX A920", "Inactivo", "QR", "American Express,Visa"),

            # --- C-0005 Tienda Mi Barrio E.U. ---
            ("T-10010", "C-0005", "Bucaramanga", "PAX A920", "Inactivo", "POS Físico", "Visa,American Express"),
            ("T-10011", "C-0005", "Bucaramanga", "PAX A920", "En mantenimiento", "POS Físico", "Visa"),
            ("T-10012", "C-0005", "Bucaramanga", "Verifone VX520", "Inactivo", "POS Físico", "Visa,Mastercard,American Express"),

            # --- C-0006 Papelería El Estudiante ---
            ("T-10013", "C-0006", "Pereira", "Verifone VX520", "Activo", "POS Físico", "Mastercard,American Express,Visa"),

            # --- C-0007 Licores del Norte ---
            ("T-10014", "C-0007", "Santa Marta", "SmartPOS Clover Flex", "Inactivo", "SmartPOS", "Mastercard,Visa,American Express"),

            # --- C-0008 Moda Urbana S.A.S. ---
            ("T-10015", "C-0008", "Cartagena", "Ingenico iCT250", "Activo", "Link de Pago", "Visa"),
            ("T-10016", "C-0008", "Cartagena", "SmartPOS Clover Flex", "En mantenimiento", "Link de Pago", "Visa,American Express"),
            ("T-10017", "C-0008", "Cartagena", "Verifone VX520", "Inactivo", "Link de Pago", "Mastercard,American Express"),

            # --- C-0009 Restaurante El Carbón ---
            ("T-10018", "C-0009", "Manizales", "SmartPOS Clover Flex", "Inactivo", "QR", "American Express"),
            ("T-10019", "C-0009", "Manizales", "PAX A920", "En mantenimiento", "QR", "Mastercard"),
            ("T-10020", "C-0009", "Manizales", "Verifone VX520", "Activo", "QR", "Mastercard,Visa,American Express"),

            # --- C-0010 Zapatería El Paso ---
            ("T-10021", "C-0010", "Cúcuta", "Ingenico iCT250", "Activo", "POS Físico", "American Express"),

            # --- C-0011 Heladería Polar ---
            ("T-10022", "C-0011", "Ibagué", "Verifone VX520", "En mantenimiento", "SmartPOS", "Visa,Mastercard,American Express"),

            # --- C-0012 Panadería Dulce Hogar ---
            ("T-10023", "C-0012", "Tunja", "SmartPOS Clover Flex", "Activo", "QR", "American Express,Visa"),
            ("T-10024", "C-0012", "Tunja", "Ingenico iCT250", "Activo", "QR", "American Express"),

            # --- C-0013 Autoservicio El Ahorro ---
            ("T-10025", "C-0013", "Villavicencio", "Verifone VX520", "Activo", "Link de Pago", "American Express,Visa"),

            # --- C-0014 Café Central ---
            ("T-10026", "C-0014", "Neiva", "Verifone VX520", "Activo", "SmartPOS", "Mastercard,American Express,Visa"),
            ("T-10027", "C-0014", "Neiva", "SmartPOS Clover Flex", "Activo", "SmartPOS", "American Express"),

            # --- C-0015 Minimercado Don Pepe ---
            ("T-10028", "C-0015", "Floridablanca", "Verifone VX520", "Inactivo", "POS Físico", "American Express,Visa,Mastercard"),

            # --- C-0016 Peluquería Glamour ---
            ("T-10029", "C-0016", "Popayán", "PAX A920", "Activo", "Link de Pago", "Mastercard,American Express,Visa"),

            # --- C-0017 Restaurante Mi Tierra ---
            ("T-10030", "C-0017", "Armenia", "Ingenico iCT250", "En mantenimiento", "SmartPOS", "American Express"),
            ("T-10031", "C-0017", "Armenia", "PAX A920", "En mantenimiento", "SmartPOS", "Visa,American Express"),
            ("T-10032", "C-0017", "Armenia", "Verifone VX520", "Inactivo", "SmartPOS", "Visa,American Express,Mastercard"),

            # --- C-0018 Ferretería El Martillo ---
            ("T-10033", "C-0018", "Yopal", "Ingenico iCT250", "Inactivo", "QR", "Visa"),

            # --- C-0019 Droguería El Sol ---
            ("T-10034", "C-0019", "Sincelejo", "SmartPOS Clover Flex", "Activo", "POS Físico", "Visa"),
            ("T-10035", "C-0019", "Sincelejo", "Verifone VX520", "Inactivo", "POS Físico", "American Express,Visa,Mastercard"),

            # --- C-0020 Panadería Santa Clara ---
            ("T-10036", "C-0020", "Montería", "SmartPOS Clover Flex", "En mantenimiento", "POS Físico", "Mastercard"),
            ("T-10037", "C-0020", "Montería", "Ingenico iCT250", "En mantenimiento", "POS Físico", "Visa"),
            ("T-10038", "C-0020", "Montería", "PAX A920", "Inactivo", "POS Físico", "Visa"),

            # --- C-0021 Supermercado El Campo ---
            ("T-10039", "C-0021", "Pasto", "Verifone VX520", "En mantenimiento", "SmartPOS", "American Express,Mastercard"),

            # --- C-0022 Restaurante El Sabor Llanero ---
            ("T-10040", "C-0022", "Arauca", "PAX A920", "Inactivo", "Link de Pago", "Mastercard,Visa"),
            ("T-10041", "C-0022", "Arauca", "SmartPOS Clover Flex", "Inactivo", "Link de Pago", "American Express"),

            # --- C-0023 Cafetería Aromas ---
            ("T-10042", "C-0023", "Riohacha", "PAX A920", "En mantenimiento", "QR", "Visa,American Express,Mastercard"),
            ("T-10043", "C-0023", "Riohacha", "SmartPOS Clover Flex", "Inactivo", "QR", "Visa,Mastercard,American Express"),

            # --- C-0024 Papelería Escolar ---
            ("T-10044", "C-0024", "Sincelejo", "PAX A920", "En mantenimiento", "POS Físico", "Visa,American Express,Mastercard"),

            # --- C-0025 Ferretería La Llave ---
            ("T-10045", "C-0025", "Medellín", "PAX A920", "En mantenimiento", "SmartPOS", "Visa,Mastercard"),
            ("T-10046", "C-0025", "Medellín", "Verifone VX520", "Activo", "SmartPOS", "Visa,Mastercard"),
        ]

        terminals_to_add = []
        for terminal_code, commerce_code, city, model, status, channel, franchises in terminals_data:
            commerce = db.query(Commerce).filter(Commerce.code == commerce_code).first()
            if not commerce:
                print(f"⚠️ Comercio con código {commerce_code} no encontrado, omitiendo {terminal_code}.")
                continue
            terminals_to_add.append(
                Terminal(
                    terminal_code=terminal_code,
                    commerce_id=commerce.id,
                    city=city,
                    model=model,
                    status=status,
                    channel=channel,
                    franchises=franchises,
                    assigned_by="Credibanco",
                )
            )

        db.add_all(terminals_to_add)
        db.commit()
        print("✅ Terminales iniciales creadas correctamente.")

    finally:
        db.close()