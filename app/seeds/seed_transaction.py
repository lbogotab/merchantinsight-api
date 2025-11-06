from app.db import SessionLocal
from app.models.transaction import TransactionSummary
from app.models.terminal import Terminal

def seed_transaction_summaries():
    db = SessionLocal()

    transaction_data = [
        ("T-10001", "Bogotá", "POS Físico", "Mastercard, American Express", 774, 34885207),
        ("T-10002", "Bogotá", "POS Físico", "Mastercard, American Express", 145, 204058447),
        ("T-10003", "Bogotá", "POS Físico", "Mastercard", 401, 70737657),
        ("T-10004", "Medellín", "SmartPOS", "American Express, Visa", 348, 42456926),
        ("T-10005", "Medellín", "SmartPOS", "Visa, American Express", 224, 186650134),
        ("T-10006", "Medellín", "SmartPOS", "Visa", 678, 28337464),
        ("T-10007", "Cali", "Link de Pago", "Visa, Mastercard", 724, 118258777),
        ("T-10008", "Barranquilla", "QR", "Visa, Mastercard, American Express", 152, 12998630),
        ("T-10009", "Barranquilla", "QR", "American Express, Visa", 215, 63690184),
        ("T-10010", "Bucaramanga", "POS Físico", "Visa, American Express", 358, 140655277),
        ("T-10011", "Bucaramanga", "POS Físico", "Visa", 736, 12123195),
        ("T-10012", "Bucaramanga", "POS Físico", "Visa, Mastercard, American Express", 694, 58375074),
        ("T-10013", "Pereira", "POS Físico", "Mastercard, American Express, Visa", 785, 193260488),
        ("T-10014", "Santa Marta", "SmartPOS", "Mastercard, Visa, American Express", 678, 117613994),
        ("T-10015", "Cartagena", "Link de Pago", "Visa", 345, 125583634),
        ("T-10016", "Cartagena", "Link de Pago", "Visa, American Express", 723, 79676249),
        ("T-10017", "Cartagena", "Link de Pago", "Mastercard, American Express", 126, 208690800),
        ("T-10018", "Manizales", "QR", "American Express", 283, 192405367),
        ("T-10019", "Manizales", "QR", "Mastercard", 552, 96335303),
        ("T-10020", "Manizales", "QR", "Mastercard, Visa, American Express", 404, 46736211),
        ("T-10021", "Cúcuta", "POS Físico", "American Express", 340, 209948894),
        ("T-10022", "Ibagué", "SmartPOS", "Visa, Mastercard, American Express", 464, 32436862),
        ("T-10023", "Tunja", "QR", "American Express, Visa", 214, 106985959),
        ("T-10024", "Tunja", "QR", "American Express", 219, 101362792),
        ("T-10025", "Villavicencio", "Link de Pago", "American Express, Visa", 472, 167061472),
        ("T-10026", "Neiva", "SmartPOS", "Mastercard, American Express, Visa", 390, 221661847),
        ("T-10027", "Neiva", "SmartPOS", "American Express", 164, 200885885),
        ("T-10028", "Floridablanca", "POS Físico", "American Express, Visa, Mastercard", 590, 148942632),
        ("T-10029", "Popayán", "Link de Pago", "Mastercard, American Express, Visa", 247, 106612049),
        ("T-10030", "Armenia", "SmartPOS", "American Express", 200, 153187279),
        ("T-10031", "Armenia", "SmartPOS", "Visa, American Express", 420, 227641619),
        ("T-10032", "Armenia", "SmartPOS", "Visa, American Express, Mastercard", 763, 171032631),
        ("T-10033", "Yopal", "QR", "Visa", 490, 159981787),
        ("T-10034", "Sincelejo", "POS Físico", "Visa", 316, 194132063),
        ("T-10035", "Sincelejo", "POS Físico", "American Express, Visa, Mastercard", 191, 17300889),
        ("T-10036", "Montería", "POS Físico", "Mastercard", 797, 66175976),
        ("T-10037", "Montería", "POS Físico", "Visa", 416, 26418995),
        ("T-10038", "Montería", "POS Físico", "Visa", 358, 237594939),
        ("T-10039", "Pasto", "SmartPOS", "American Express, Mastercard", 223, 107039357),
        ("T-10040", "Arauca", "Link de Pago", "Mastercard, Visa", 404, 126711401),
        ("T-10041", "Arauca", "Link de Pago", "American Express", 770, 228904813),
        ("T-10042", "Riohacha", "QR", "Visa, American Express, Mastercard", 493, 48662126),
        ("T-10043", "Riohacha", "QR", "Visa, Mastercard, American Express", 499, 100367253),
        ("T-10044", "Sincelejo", "POS Físico", "Visa, American Express, Mastercard", 334, 184898778),
        ("T-10045", "Medellín", "SmartPOS", "Visa, Mastercard", 393, 193393455),
        ("T-10046", "Medellín", "SmartPOS", "Visa, Mastercard", 819, 178955674),
    ]

    for t_code, ciudad, canal, franquicias, total_tx, volumen in transaction_data:
            terminal = db.query(Terminal).filter(Terminal.terminal_code == t_code).first()
            if terminal:
                franquicia_list = [f.strip() for f in franquicias.split(",")]
                distribucion = {f: round(100 / len(franquicia_list), 2) for f in franquicia_list}
                promedio = round(volumen / total_tx, 2) if total_tx > 0 else 0.0

                entry = TransactionSummary(
                    terminal_id=terminal.id,
                    ciudad=ciudad,
                    canal=canal,
                    franquicias=franquicias,
                    total_transacciones=total_tx,
                    volumen_total=volumen,
                    moneda="COP",
                    observaciones="Transacciones registradas automáticamente para análisis inicial",
                )
                db.add(entry)

    db.commit()
    db.close()
    print("✅ Transacciones iniciales creadas correctamente.")