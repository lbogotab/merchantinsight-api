from app.db import SessionLocal
from app.models.commerce import Commerce
from app.models.invoice import Invoice
from datetime import datetime, timedelta
import random

def seed_invoices():
    db = SessionLocal()
    try:
        if db.query(Invoice).count() > 0:
            print("ℹ️ Facturas ya existentes, sin cambios.")
            return

        invoices_data = [
            ("FCT-2025-1001", "C-0001", "2025-05-03", "mayo 2025", 18664766, 671805, 17992961, "Pagada", "LIQ-2025-1068, LIQ-2025-1071"),
            ("FCT-2025-1002", "C-0001", "2025-06-11", "junio 2025", 6741530, 199412, 6542118, "Pendiente", "LIQ-2025-1042, LIQ-2025-1089, LIQ-2025-1031"),
            ("FCT-2025-1003", "C-0002", "2025-01-14", "enero 2025", 7939821, 577366, 7362455, "Pendiente", "LIQ-2025-1000"),
            ("FCT-2025-1004", "C-0002", "2025-06-24", "junio 2025", 20043180, 523572, 19519608, "Pagada", "LIQ-2025-1085"),
            ("FCT-2025-1005", "C-0003", "2025-03-26", "marzo 2025", 5712561, 214267, 5498294, "Pendiente", "LIQ-2025-1061, LIQ-2025-1033, LIQ-2025-1060"),
            ("FCT-2025-1006", "C-0003", "2025-01-25", "enero 2025", 15237360, 618754, 14618606, "Pendiente", "LIQ-2025-1077"),
            ("FCT-2025-1007", "C-0004", "2025-09-19", "septiembre 2025", 15578476, 323298, 15255178, "En revisión", "LIQ-2025-1055, LIQ-2025-1087, LIQ-2025-1068"),
            ("FCT-2025-1008", "C-0004", "2025-08-17", "agosto 2025", 19075958, 810180, 18265778, "Pagada", "LIQ-2025-1023, LIQ-2025-1092, LIQ-2025-1010"),
            ("FCT-2025-1009", "C-0004", "2025-08-22", "agosto 2025", 13787478, 416486, 13370992, "Pendiente", "LIQ-2025-1050, LIQ-2025-1009, LIQ-2025-1092"),
            ("FCT-2025-1010", "C-0004", "2025-08-13", "agosto 2025", 24232343, 1616886, 22615457, "Pagada", "LIQ-2025-1075"),
            ("FCT-2025-1011", "C-0005", "2025-06-01", "junio 2025", 16808263, 1342192, 15466071, "Pendiente", "LIQ-2025-1064, LIQ-2025-1092, LIQ-2025-1007"),
            ("FCT-2025-1012", "C-0005", "2025-05-16", "mayo 2025", 12830704, 675539, 12155165, "Pagada", "LIQ-2025-1068"),
            ("FCT-2025-1013", "C-0006", "2025-07-25", "julio 2025", 20478527, 463793, 20014734, "Pagada", "LIQ-2025-1024, LIQ-2025-1002"),
            ("FCT-2025-1014", "C-0006", "2025-05-26", "mayo 2025", 16812754, 1027225, 15785529, "Pendiente", "LIQ-2025-1053, LIQ-2025-1000, LIQ-2025-1013"),
            ("FCT-2025-1015", "C-0006", "2025-02-17", "febrero 2025", 16913885, 1055818, 15858067, "Pagada", "LIQ-2025-1001, LIQ-2025-1068"),
            ("FCT-2025-1016", "C-0007", "2025-02-18", "febrero 2025", 18562945, 403710, 18159235, "Pendiente", "LIQ-2025-1060, LIQ-2025-1004"),
            ("FCT-2025-1017", "C-0007", "2025-09-11", "septiembre 2025", 18893936, 772800, 18121136, "En revisión", "LIQ-2025-1020, LIQ-2025-1053, LIQ-2025-1008"),
            ("FCT-2025-1018", "C-0007", "2025-03-12", "marzo 2025", 12884064, 832914, 12051150, "En revisión", "LIQ-2025-1097"),
            ("FCT-2025-1019", "C-0008", "2025-07-18", "julio 2025", 15273151, 439383, 14833768, "En revisión", "LIQ-2025-1099, LIQ-2025-1049"),
            ("FCT-2025-1020", "C-0008", "2025-06-05", "junio 2025", 22948955, 1801395, 21147560, "En revisión", "LIQ-2025-1080"),
            ("FCT-2025-1021", "C-0008", "2025-03-26", "marzo 2025", 24773461, 1069588, 23703873, "Pagada", "LIQ-2025-1017, LIQ-2025-1058, LIQ-2025-1085"),
            ("FCT-2025-1022", "C-0008", "2025-01-12", "enero 2025", 20090229, 1451813, 18638416, "En revisión", "LIQ-2025-1091, LIQ-2025-1085, LIQ-2025-1057"),
            ("FCT-2025-1023", "C-0009", "2025-07-26", "julio 2025", 5948182, 175558, 5772624, "Pendiente", "LIQ-2025-1065, LIQ-2025-1071, LIQ-2025-1017"),
            ("FCT-2025-1024", "C-0009", "2025-06-17", "junio 2025", 8515750, 449013, 8066737, "Pendiente", "LIQ-2025-1072"),
            ("FCT-2025-1025", "C-0009", "2025-06-03", "junio 2025", 14118463, 1070023, 13048440, "Pagada", "LIQ-2025-1041"),
            ("FCT-2025-1026", "C-0010", "2025-07-02", "julio 2025", 21795582, 541003, 21254579, "Pagada", "LIQ-2025-1025, LIQ-2025-1097, LIQ-2025-1002"),
            ("FCT-2025-1027", "C-0010", "2025-04-09", "abril 2025", 23945654, 810696, 23134958, "En revisión", "LIQ-2025-1010, LIQ-2025-1043"),
            ("FCT-2025-1028", "C-0010", "2025-09-18", "septiembre 2025", 9478430, 718109, 8760321, "En revisión", "LIQ-2025-1061"),
            ("FCT-2025-1029", "C-0011", "2025-07-25", "julio 2025", 5947060, 210591, 5736469, "En revisión", "LIQ-2025-1043, LIQ-2025-1050"),
            ("FCT-2025-1030", "C-0011", "2025-04-27", "abril 2025", 21819412, 1647311, 20172101, "En revisión", "LIQ-2025-1000, LIQ-2025-1076, LIQ-2025-1077"),
            #Added more invoices for diversity
            ("FCT-2025-1031", "C-0012", "2025-04-15", "abril 2025", 12000000, 500000, 11500000, "Pagada", "LIQ-2025-1101, LIQ-2025-1102"),
            ("FCT-2025-1032", "C-0013", "2025-05-20", "mayo 2025", 8500000, 300000, 8200000, "Pendiente", "LIQ-2025-1103, LIQ-2025-1104"),
            ("FCT-2025-1033", "C-0014", "2025-06-10", "junio 2025", 15000000, 1000000, 14000000, "En revisión", "LIQ-2025-1105, LIQ-2025-1106"),
            ("FCT-2025-1034", "C-0015", "2025-07-05", "julio 2025", 23000000, 1500000, 21500000, "Pagada", "LIQ-2025-1107, LIQ-2025-1108"),
            ("FCT-2025-1035", "C-0016", "2025-08-12", "agosto 2025", 7000000, 200000, 6800000, "Pendiente", "LIQ-2025-1109, LIQ-2025-1110"),
            ("FCT-2025-1036", "C-0017", "2025-09-01", "septiembre 2025", 13000000, 700000, 12300000, "En revisión", "LIQ-2025-1111, LIQ-2025-1112"),
            ("FCT-2025-1037", "C-0018", "2025-04-22", "abril 2025", 9000000, 400000, 8600000, "Pagada", "LIQ-2025-1113, LIQ-2025-1114"),
            ("FCT-2025-1038", "C-0019", "2025-05-30", "mayo 2025", 11000000, 600000, 10400000, "Pendiente", "LIQ-2025-1115, LIQ-2025-1116"),
            ("FCT-2025-1039", "C-0020", "2025-06-18", "junio 2025", 16000000, 800000, 15200000, "En revisión", "LIQ-2025-1117, LIQ-2025-1118"),
            ("FCT-2025-1040", "C-0021", "2025-07-23", "julio 2025", 21000000, 1200000, 19800000, "Pagada", "LIQ-2025-1119, LIQ-2025-1120"),
            ("FCT-2025-1041", "C-0022", "2025-08-14", "agosto 2025", 6000000, 150000, 5850000, "Pendiente", "LIQ-2025-1121, LIQ-2025-1122"),
            ("FCT-2025-1042", "C-0023", "2025-09-07", "septiembre 2025", 14000000, 900000, 13100000, "En revisión", "LIQ-2025-1123, LIQ-2025-1124"),
            ("FCT-2025-1043", "C-0024", "2025-04-28", "abril 2025", 10000000, 500000, 9500000, "Pagada", "LIQ-2025-1125, LIQ-2025-1126"),
            ("FCT-2025-1044", "C-0025", "2025-05-19", "mayo 2025", 18000000, 1100000, 16900000, "Pendiente", "LIQ-2025-1127, LIQ-2025-1128"),
        ]

        payment_methods = ["Transferencia", "Débito automático", "Compensación interna"]

        invoices_to_add = []
        for (
            invoice_code, commerce_code, issued_date, billing_period,
            gross_amount, discounts, net_amount, status, settlements
        ) in invoices_data:
            commerce = db.query(Commerce).filter(Commerce.code == commerce_code).first()
            if not commerce:
                print(f"⚠️ Comercio {commerce_code} no encontrado, omitiendo {invoice_code}.")
                continue

            issued_dt = datetime.strptime(issued_date, "%Y-%m-%d").date()
            due_date = issued_dt + timedelta(days=30)

            if status == "Pagada":
                payment_date = issued_dt + timedelta(days=random.randint(1,10))
            else:
                payment_date = None

            payment_method = random.choice(payment_methods)
            currency = "COP"
            tax_value = round(gross_amount * 0.19, 2)
            invoice_type = "Mensual"
            observations = "Factura generada automáticamente"
            is_recurrent = True

            invoices_to_add.append(
                Invoice(
                    invoice_code=invoice_code,
                    commerce_id=commerce.id,
                    issued_date=issued_dt,
                    billing_period=billing_period,
                    gross_amount=gross_amount,
                    discounts_and_retentions=discounts,
                    net_amount=net_amount,
                    status=status,
                    settlements_refs=settlements,
                    due_date=due_date,
                    payment_date=payment_date,
                    payment_method=payment_method,
                    currency=currency,
                    tax_value=tax_value,
                    invoice_type=invoice_type,
                    observations=observations,
                    is_recurrent=is_recurrent,
                )
            )

        db.add_all(invoices_to_add)
        db.commit()
        print("✅ Facturas iniciales creadas correctamente.")

    finally:
        db.close()