# app/seeds/seed_novelty.py
from datetime import date
from app.db import SessionLocal
from app.models.terminal import Terminal
from app.models.novelty import Novedad

def _get_terminal_id_col():
    """
    Devuelve la columna identificadora disponible en Terminal:
    code | terminal_code | serial_number | identifier.
    Lanza ValueError si ninguna existe.
    """
    candidates = ("code", "terminal_code", "serial_number", "identifier")
    for c in candidates:
        if hasattr(Terminal, c):
            return getattr(Terminal, c)
    raise ValueError(
        "El modelo Terminal no tiene ninguna columna identificadora esperada "
        "(code, terminal_code, serial_number, identifier)."
    )

def seed_novedades():
    db = SessionLocal()

    # --- Define aquí TODAS las novedades que compartiste ---
    novedades_data = [
        # (terminal_code, fecha, tipo, responsable, observacion)
        ("T-10001", date(2025, 2, 1),  "Cambio de estado",        "Credibanco", "Actualización de estado operativo de la terminal T-10001 tras proceso de mantenimiento."),
        ("T-10001", date(2025, 4, 5),  "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10001 en un nuevo punto de venta."),
        ("T-10001", date(2025, 7, 2),  "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10001 en un nuevo punto de venta."),
        ("T-10002", date(2025, 4, 17), "Reasignación comercial",   "Credibanco", "Reasignación de la terminal T-10002 a un nuevo comercio o ubicación."),
        ("T-10003", date(2025, 4, 23), "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10003 a un nuevo comercio o ubicación."),
        ("T-10003", date(2025, 4, 15), "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10003 a un nuevo comercio o ubicación."),
        ("T-10003", date(2025, 1, 25), "Baja de terminal",         "Comercio",   "La terminal T-10003 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10004", date(2025, 5, 5),  "Baja de terminal",         "Comercio",   "La terminal T-10004 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10004", date(2025, 2, 3),  "Cambio de canal o modelo", "Credibanco", "La terminal T-10004 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10005", date(2025, 6, 20), "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10005 tras proceso de mantenimiento."),
        ("T-10005", date(2025, 8, 18), "Alta de terminal",         "Comercio",   "Se registró la instalación de la terminal T-10005 en un nuevo punto de venta."),
        ("T-10006", date(2025, 9, 10), "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10006 a un nuevo comercio o ubicación."),
        ("T-10007", date(2025, 4, 23), "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10007 en un nuevo punto de venta."),
        ("T-10007", date(2025, 4, 25), "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10007 tras proceso de mantenimiento."),
        ("T-10007", date(2025, 4, 28), "Alta de terminal",         "Comercio",   "Se registró la instalación de la terminal T-10007 en un nuevo punto de venta."),
        ("T-10008", date(2025, 8, 21), "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10008 tras proceso de mantenimiento."),
        ("T-10008", date(2025, 6, 12), "Baja de terminal",         "Comercio",   "La terminal T-10008 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10009", date(2025, 2, 20), "Baja de terminal",         "Credibanco", "La terminal T-10009 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10009", date(2025, 3, 15), "Cambio de canal o modelo", "Comercio",   "La terminal T-10009 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10009", date(2025, 9, 8),  "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10009 tras proceso de mantenimiento."),
        ("T-10010", date(2025, 1, 26), "Cambio de estado",         "Comercio",   "Actualización de estado operativo de la terminal T-10010 tras proceso de mantenimiento."),
        ("T-10011", date(2025, 2, 7),  "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10011 a un nuevo comercio o ubicación."),
        ("T-10011", date(2025, 4, 21), "Cambio de canal o modelo", "Comercio",   "La terminal T-10011 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10012", date(2025, 8, 5),  "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10012 tras proceso de mantenimiento."),
        ("T-10012", date(2025, 4, 24), "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10012 a un nuevo comercio o ubicación."),
        ("T-10012", date(2025, 7, 19), "Cambio de canal o modelo", "Comercio",   "La terminal T-10012 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10013", date(2025, 3, 17), "Cambio de canal o modelo", "Credibanco", "La terminal T-10013 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10014", date(2025, 2, 5),  "Baja de terminal",         "Comercio",   "La terminal T-10014 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10015", date(2025, 2, 13), "Cambio de canal o modelo", "Comercio",   "La terminal T-10015 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10015", date(2025, 9, 9),  "Reasignación comercial",   "Credibanco", "Reasignación de la terminal T-10015 a un nuevo comercio o ubicación."),
        ("T-10015", date(2025, 2, 22), "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10015 a un nuevo comercio o ubicación."),
        ("T-10016", date(2025, 6, 4),  "Cambio de estado",         "Comercio",   "Actualización de estado operativo de la terminal T-10016 tras proceso de mantenimiento."),
        ("T-10016", date(2025, 3, 15), "Alta de terminal",         "Comercio",   "Se registró la instalación de la terminal T-10016 en un nuevo punto de venta."),
        ("T-10016", date(2025, 9, 25), "Baja de terminal",         "Credibanco", "La terminal T-10016 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10017", date(2025, 5, 27), "Reasignación comercial",   "Credibanco", "Reasignación de la terminal T-10017 a un nuevo comercio o ubicación."),
        ("T-10017", date(2025, 3, 12), "Baja de terminal",         "Credibanco", "La terminal T-10017 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10017", date(2025, 6, 16), "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10017 en un nuevo punto de venta."),
        ("T-10018", date(2025, 5, 8),  "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10018 en un nuevo punto de venta."),
        ("T-10018", date(2025, 2, 3),  "Cambio de canal o modelo", "Credibanco", "La terminal T-10018 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10019", date(2025, 3, 5),  "Cambio de canal o modelo", "Credibanco", "La terminal T-10019 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10019", date(2025, 5, 17), "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10019 a un nuevo comercio o ubicación."),
        ("T-10019", date(2025, 4, 18), "Baja de terminal",         "Comercio",   "La terminal T-10019 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10020", date(2025, 6, 15), "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10020 a un nuevo comercio o ubicación."),
        ("T-10020", date(2025, 2, 8),  "Baja de terminal",         "Credibanco", "La terminal T-10020 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10021", date(2025, 1, 19), "Reasignación comercial",   "Credibanco", "Reasignación de la terminal T-10021 a un nuevo comercio o ubicación."),
        ("T-10021", date(2025, 4, 1),  "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10021 en un nuevo punto de venta."),
        ("T-10022", date(2025, 2, 2),  "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10022 tras proceso de mantenimiento."),
        ("T-10023", date(2025, 4, 9),  "Cambio de canal o modelo", "Credibanco", "La terminal T-10023 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10023", date(2025, 9, 5),  "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10023 a un nuevo comercio o ubicación."),
        ("T-10023", date(2025, 4, 26), "Cambio de canal o modelo", "Comercio",   "La terminal T-10023 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10024", date(2025, 2, 4),  "Cambio de canal o modelo", "Comercio",   "La terminal T-10024 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10025", date(2025, 7, 15), "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10025 en un nuevo punto de venta."),
        ("T-10025", date(2025, 1, 13), "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10025 tras proceso de mantenimiento."),
        ("T-10026", date(2025, 4, 7),  "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10026 a un nuevo comercio o ubicación."),
        ("T-10027", date(2025, 7, 6),  "Cambio de estado",         "Comercio",   "Actualización de estado operativo de la terminal T-10027 tras proceso de mantenimiento."),
        ("T-10028", date(2025, 2, 15), "Reasignación comercial",   "Credibanco", "Reasignación de la terminal T-10028 a un nuevo comercio o ubicación."),
        ("T-10029", date(2025, 9, 27), "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10029 en un nuevo punto de venta."),
        ("T-10030", date(2025, 3, 14), "Cambio de canal o modelo", "Comercio",   "La terminal T-10030 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10031", date(2025, 7, 2),  "Baja de terminal",         "Comercio",   "La terminal T-10031 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10032", date(2025, 7, 9),  "Cambio de canal o modelo", "Comercio",   "La terminal T-10032 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10033", date(2025, 9, 22), "Cambio de canal o modelo", "Credibanco", "La terminal T-10033 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10033", date(2025, 4, 10), "Baja de terminal",         "Credibanco", "La terminal T-10033 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10034", date(2025, 9, 2),  "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10034 tras proceso de mantenimiento."),
        ("T-10034", date(2025, 1, 19), "Cambio de canal o modelo", "Credibanco", "La terminal T-10034 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10034", date(2025, 1, 17), "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10034 en un nuevo punto de venta."),
        ("T-10035", date(2025, 2, 22), "Baja de terminal",         "Comercio",   "La terminal T-10035 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10036", date(2025, 4, 19), "Reasignación comercial",   "Credibanco", "Reasignación de la terminal T-10036 a un nuevo comercio o ubicación."),
        ("T-10037", date(2025, 2, 14), "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10037 a un nuevo comercio o ubicación."),
        ("T-10037", date(2025, 5, 7),  "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10037 tras proceso de mantenimiento."),
        ("T-10037", date(2025, 5, 13), "Baja de terminal",         "Comercio",   "La terminal T-10037 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10038", date(2025, 6, 25), "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10038 en un nuevo punto de venta."),
        ("T-10038", date(2025, 8, 20), "Reasignación comercial",   "Credibanco", "Reasignación de la terminal T-10038 a un nuevo comercio o ubicación."),
        ("T-10039", date(2025, 9, 7),  "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10039 a un nuevo comercio o ubicación."),
        ("T-10040", date(2025, 6, 3),  "Baja de terminal",         "Comercio",   "La terminal T-10040 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10041", date(2025, 3, 15), "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10041 a un nuevo comercio o ubicación."),
        ("T-10041", date(2025, 9, 1),  "Reasignación comercial",   "Comercio",   "Reasignación de la terminal T-10041 a un nuevo comercio o ubicación."),
        ("T-10042", date(2025, 2, 5),  "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10042 tras proceso de mantenimiento."),
        ("T-10042", date(2025, 2, 24), "Reasignación comercial",   "Credibanco", "Reasignación de la terminal T-10042 a un nuevo comercio o ubicación."),
        ("T-10042", date(2025, 5, 10), "Reasignación comercial",   "Credibanco", "Reasignación de la terminal T-10042 a un nuevo comercio o ubicación."),
        ("T-10043", date(2025, 6, 7),  "Cambio de estado",         "Comercio",   "Actualización de estado operativo de la terminal T-10043 tras proceso de mantenimiento."),
        ("T-10043", date(2025, 5, 28), "Alta de terminal",         "Credibanco", "Se registró la instalación de la terminal T-10043 en un nuevo punto de venta."),
        ("T-10043", date(2025, 7, 27), "Cambio de estado",         "Credibanco", "Actualización de estado operativo de la terminal T-10043 tras proceso de mantenimiento."),
        ("T-10044", date(2025, 6, 25), "Baja de terminal",         "Comercio",   "La terminal T-10044 fue retirada del sistema por obsolescencia o solicitud del comercio."),
        ("T-10045", date(2025, 8, 18), "Cambio de canal o modelo", "Credibanco", "La terminal T-10045 fue actualizada a un nuevo modelo o canal de operación."),
        ("T-10046", date(2025, 2, 23), "Baja de terminal",         "Credibanco", "La terminal T-10046 fue retirada del sistema por obsolescencia o solicitud del comercio."),
    ]

    inserted = 0
    try:
        terminal_id_col = _get_terminal_id_col()
        for term_code, fecha, tipo, responsable, observacion in novedades_data:
            terminal = (
                db.query(Terminal)
                  .filter(terminal_id_col == term_code)
                  .first()
            )
            if not terminal:
                # Si no existe la terminal, saltamos sin romper el seed
                continue

            exists = (
                db.query(Novedad)
                  .filter(
                      Novedad.terminal_id == terminal.id,
                      Novedad.fecha == fecha,
                      Novedad.tipo == tipo,
                  )
                  .first()
            )
            if exists:
                continue

            # Código legible e idempotente
            code_suffix = tipo.replace(" ", "")[:12]
            nov_code = f"NVD-{term_code}-{fecha.isoformat()}-{code_suffix}"

            db.add(Novedad(
                novedad_code=nov_code,
                terminal_id=terminal.id,
                fecha=fecha,
                tipo=tipo,
                responsable=responsable,
                observacion=observacion
            ))
            inserted += 1

        db.commit()
        print(f"✅ Novedades iniciales creadas correctamente. Registros nuevos: {inserted}")
    finally:
        db.close()