from datetime import date
from app.db import SessionLocal
from app.models.settlement import Settlement
from app.models.commerce import Commerce

def seed_settlements():
    db = SessionLocal()
    if db.query(Settlement).count() > 0:
        print("⚠️ Settlements already seeded.")
        db.close()
        return

    settlements_data = [
        # --- C-0001 ---
# ----------------- C-0001 -----------------
        ("C-0001", date(2025, 1, 24), 683, 70737657, 2.05, 1450121, 69287536, "Cuenta Corriente", "enero 2025"),
        ("C-0001", date(2025, 9, 3), 1329, 118258777, 1.83, 2164135, 116094642, "Cuenta Corriente", "septiembre 2025"),

        # ----------------- C-0002 -----------------
        ("C-0002", date(2025, 4, 17), 1352, 12123195, 2.42, 293381, 11829814, "Cuenta de Ahorros", "abril 2025"),
        ("C-0002", date(2025, 4, 15), 1326, 79676249, 2.69, 2143291, 77532958, "Cuenta Corriente", "abril 2025"),
        ("C-0002", date(2025, 3, 23), 985, 96335303, 2.11, 2032674, 94302629, "Cuenta Corriente", "marzo 2025"),

        # ----------------- C-0003 -----------------
        ("C-0003", date(2025, 2, 3), 898, 30962105, 2.19, 678070, 30284035, "Cuenta de Ahorros", "febrero 2025"),
        ("C-0003", date(2025, 5, 26), 208, 200885885, 2.31, 4640463, 196245422, "Cuenta Corriente", "mayo 2025"),
        ("C-0003", date(2025, 7, 3), 1250, 83699444, 2.71, 2268254, 81431190, "Cuenta de Ahorros", "julio 2025"),
        ("C-0003", date(2025, 4, 23), 262, 17300889, 2.53, 437712, 16863177, "Cuenta de Ahorros", "abril 2025"),

        # ----------------- C-0004 -----------------
        ("C-0004", date(2025, 4, 28), 326, 107039357, 2.11, 2258530, 104780827, "Cuenta de Ahorros", "abril 2025"),
        ("C-0004", date(2025, 3, 12), 847, 61239114, 2.54, 1555473, 59683641, "Cuenta Corriente", "marzo 2025"),

        # ----------------- C-0005 -----------------
        ("C-0005", date(2025, 3, 18), 621, 48863022, 2.31, 1128735, 47734287, "Cuenta de Ahorros", "marzo 2025"),
        ("C-0005", date(2025, 9, 8), 784, 231251338, 2.65, 6128160, 225123178, "Cuenta Corriente", "septiembre 2025"),
        ("C-0005", date(2025, 4, 27), 185, 221102836, 2.15, 4753710, 216349126, "Cuenta de Ahorros", "abril 2025"),
        ("C-0005", date(2025, 2, 7), 1281, 240248142, 2.59, 6222426, 234025716, "Cuenta Corriente", "febrero 2025"),
        ("C-0005", date(2025, 8, 13), 1436, 128172106, 1.96, 2512173, 125659933, "Cuenta Corriente", "agosto 2025"),
        ("C-0005", date(2025, 4, 24), 1269, 149680614, 2.09, 3128324, 146552290, "Cuenta de Ahorros", "abril 2025"),

        # ----------------- C-0006 -----------------
        ("C-0006", date(2025, 7, 12), 569, 42133144, 2.36, 994342, 41138802, "Cuenta Corriente", "julio 2025"),
        ("C-0006", date(2025, 1, 28), 344, 46028029, 2.49, 1146097, 44881932, "Cuenta de Ahorros", "enero 2025"),
        ("C-0006", date(2025, 2, 13), 901, 164957580, 2.9, 4783769, 160173811, "Cuenta de Ahorros", "febrero 2025"),
        ("C-0006", date(2025, 9, 28), 143, 187612186, 2.59, 4859155, 182753031, "Cuenta de Ahorros", "septiembre 2025"),
        ("C-0006", date(2025, 6, 4), 721, 121706409, 1.97, 2397616, 119308793, "Cuenta Corriente", "junio 2025"),
        ("C-0006", date(2025, 5, 17), 485, 141279761, 2.8, 3955833, 137323928, "Cuenta de Ahorros", "mayo 2025"),

        # ----------------- C-0007 -----------------
        ("C-0007", date(2025, 4, 5), 885, 209684934, 1.98, 4151761, 205533173, "Cuenta Corriente", "abril 2025"),
        ("C-0007", date(2025, 6, 16), 159, 35029263, 2.82, 987825, 34041438, "Cuenta de Ahorros", "junio 2025"),
        ("C-0007", date(2025, 4, 2), 613, 240688907, 2.42, 5824671, 234864236, "Cuenta Corriente", "abril 2025"),
        ("C-0007", date(2025, 2, 24), 1115, 224049574, 1.88, 4212131, 219837443, "Cuenta Corriente", "febrero 2025"),
        ("C-0007", date(2025, 3, 22), 1093, 152586779, 1.98, 3021218, 149565561, "Cuenta de Ahorros", "marzo 2025"),
        ("C-0007", date(2025, 4, 18), 531, 196380782, 2.14, 4202548, 192178234, "Cuenta de Ahorros", "abril 2025"),

        # ----------------- C-0008 -----------------
        ("C-0008", date(2025, 9, 15), 367, 71546657, 2.05, 1466706, 70079951, "Cuenta de Ahorros", "septiembre 2025"),
        ("C-0008", date(2025, 1, 19), 1254, 66770953, 2.45, 1635888, 65135065, "Cuenta Corriente", "enero 2025"),
        ("C-0008", date(2025, 2, 23), 1412, 20803806, 2.05, 426478, 20377328, "Cuenta Corriente", "febrero 2025"),
        ("C-0008", date(2025, 6, 3), 1172, 68888882, 2.11, 1453555, 67435327, "Cuenta de Ahorros", "junio 2025"),
        ("C-0008", date(2025, 4, 18), 390, 199173474, 2.83, 5636609, 193536865, "Cuenta de Ahorros", "abril 2025"),

        # ----------------- C-0009 -----------------
        ("C-0009", date(2025, 8, 26), 953, 56112773, 1.9, 1066142, 55046631, "Cuenta de Ahorros", "agosto 2025"),
        ("C-0009", date(2025, 6, 14), 961, 130365979, 2.75, 3585064, 126780915, "Cuenta Corriente", "junio 2025"),
        ("C-0009", date(2025, 2, 2), 944, 200478346, 2.17, 4350380, 196127966, "Cuenta Corriente", "febrero 2025"),

        # ----------------- C-0010 -----------------
        ("C-0010", date(2025, 4, 7), 1218, 125423783, 1.95, 2445763, 122978020, "Cuenta Corriente", "abril 2025"),
        ("C-0010", date(2025, 5, 15), 631, 239743035, 2.82, 6760753, 232982282, "Cuenta de Ahorros", "mayo 2025"),
        ("C-0010", date(2025, 9, 4), 223, 180058811, 2.9, 5221705, 174837106, "Cuenta Corriente", "septiembre 2025"),

        # ----------------- C-0011 -----------------
        ("C-0011", date(2025, 4, 6), 952, 135363297, 2.33, 3153964, 132209333, "Cuenta de Ahorros", "abril 2025"),
        ("C-0011", date(2025, 1, 6), 896, 5578578, 2.88, 160663, 5417915, "Cuenta de Ahorros", "enero 2025"),

        # ----------------- C-0012 -----------------
        ("C-0012", date(2025, 5, 14), 1258, 182669726, 2.59, 4731145, 177938581, "Cuenta Corriente", "mayo 2025"),
        ("C-0012", date(2025, 4, 10), 565, 20698989, 2.44, 505055, 20193934, "Cuenta Corriente", "abril 2025"),
        ("C-0012", date(2025, 6, 2), 222, 161813979, 2.32, 3754084, 158059895, "Cuenta Corriente", "junio 2025"),
        ("C-0012", date(2025, 1, 17), 284, 233530525, 2.0, 4670610, 228859915, "Cuenta Corriente", "enero 2025"),
        ("C-0012", date(2025, 4, 13), 365, 243984681, 2.43, 5928827, 238055854, "Cuenta Corriente", "abril 2025"),

        # ----------------- C-0013 -----------------
        ("C-0013", date(2025, 2, 14), 1466, 161678336, 2.42, 3912615, 157765721, "Cuenta de Ahorros", "febrero 2025"),
        ("C-0013", date(2025, 5, 7), 1491, 197251272, 2.15, 4240902, 193010370, "Cuenta de Ahorros", "mayo 2025"),
        ("C-0013", date(2025, 7, 5), 1495, 178275298, 2.13, 3797263, 174478035, "Cuenta de Ahorros", "julio 2025"),
        ("C-0013", date(2025, 2, 1), 1058, 171741166, 2.9, 4980493, 166760673, "Cuenta Corriente", "febrero 2025"),
        ("C-0013", date(2025, 2, 18), 556, 140797388, 2.09, 2942665, 137854723, "Cuenta de Ahorros", "febrero 2025"),
        ("C-0013", date(2025, 2, 8), 876, 81500721, 1.97, 1605564, 79895157, "Cuenta de Ahorros", "febrero 2025"),

        # ----------------- C-0014 -----------------
        ("C-0014", date(2025, 9, 1), 1487, 224339721, 2.41, 5406587, 218933134, "Cuenta Corriente", "septiembre 2025"),
        ("C-0014", date(2025, 3, 9), 356, 243830437, 1.92, 4681544, 239148893, "Cuenta Corriente", "marzo 2025"),
        ("C-0014", date(2025, 5, 10), 1358, 61540466, 2.59, 1593898, 59946568, "Cuenta Corriente", "mayo 2025"),
        ("C-0014", date(2025, 5, 17), 1120, 72409847, 2.8, 2027475, 70382372, "Cuenta Corriente", "mayo 2025"),
        ("C-0014", date(2025, 2, 21), 987, 227626433, 2.1, 4780155, 222846278, "Cuenta Corriente", "febrero 2025"),
        ("C-0014", date(2025, 6, 25), 387, 176023819, 2.88, 5069485, 170954334, "Cuenta Corriente", "junio 2025"),

        # ----------------- C-0015 -----------------
        ("C-0015", date(2025, 9, 23), 995, 155567291, 1.81, 2815767, 152751524, "Cuenta Corriente", "septiembre 2025"),
        ("C-0015", date(2025, 3, 18), 193, 229034894, 2.21, 5061671, 223973223, "Cuenta Corriente", "marzo 2025"),
        ("C-0015", date(2025, 7, 5), 205, 87747470, 2.2, 1930444, 85817026, "Cuenta Corriente", "julio 2025"),
        ("C-0015", date(2025, 6, 7), 631, 184028575, 1.91, 3514945, 180513630, "Cuenta de Ahorros", "junio 2025"),
        ("C-0015", date(2025, 3, 8), 452, 219718038, 2.69, 5910415, 213807623, "Cuenta de Ahorros", "marzo 2025"),

        # ----------------- C-0016 -----------------
        ("C-0016", date(2025, 3, 24), 800, 215020274, 2.82, 6063571, 208956703, "Cuenta Corriente", "marzo 2025"),
        ("C-0016", date(2025, 5, 6), 341, 107687761, 2.76, 2972182, 104715579, "Cuenta de Ahorros", "mayo 2025"),

        # ----------------- C-0017 -----------------
        ("C-0017", date(2025, 4, 27), 1062, 98860718, 2.14, 2115619, 96745099, "Cuenta Corriente", "abril 2025"),
        ("C-0017", date(2025, 4, 1), 1471, 56842883, 2.24, 1273280, 55569603, "Cuenta de Ahorros", "abril 2025"),
        ("C-0017", date(2025, 2, 25), 691, 99260071, 2.51, 2491427, 96768644, "Cuenta de Ahorros", "febrero 2025"),

        # ----------------- C-0018 -----------------
        ("C-0018", date(2025, 6, 1), 356, 240428205, 2.87, 6900289, 233527916, "Cuenta Corriente", "junio 2025"),
        ("C-0018", date(2025, 5, 2), 342, 165140876, 2.28, 3765211, 161375665, "Cuenta de Ahorros", "mayo 2025"),
        ("C-0018", date(2025, 7, 20), 1167, 36043429, 2.22, 800164, 35243265, "Cuenta Corriente", "julio 2025"),
        ("C-0018", date(2025, 5, 2), 1013, 5453998, 2.37, 129259, 5324739, "Cuenta Corriente", "mayo 2025"),
        ("C-0018", date(2025, 6, 14), 263, 183304945, 2.81, 5150868, 178154077, "Cuenta de Ahorros", "junio 2025"),
        ("C-0018", date(2025, 2, 24), 735, 141129661, 2.14, 3020174, 138109487, "Cuenta de Ahorros", "febrero 2025"),

        # ----------------- C-0019 -----------------
        ("C-0019", date(2025, 7, 23), 725, 153823967, 1.94, 2984184, 150839783, "Cuenta de Ahorros", "julio 2025"),
        ("C-0019", date(2025, 7, 22), 476, 170226026, 2.43, 4136492, 166089534, "Cuenta de Ahorros", "julio 2025"),
        ("C-0019", date(2025, 9, 27), 120, 86570811, 2.12, 1835301, 84735510, "Cuenta de Ahorros", "septiembre 2025"),
        ("C-0019", date(2025, 6, 15), 1024, 123691366, 2.54, 3141760, 120549606, "Cuenta de Ahorros", "junio 2025"),

        # ----------------- C-0020 -----------------
        ("C-0020", date(2025, 2, 10), 1175, 183201907, 2.5, 4580047, 178621860, "Cuenta de Ahorros", "febrero 2025"),
        ("C-0020", date(2025, 2, 27), 601, 185602212, 2.14, 3971887, 181630325, "Cuenta Corriente", "febrero 2025"),
        ("C-0020", date(2025, 3, 1), 214, 70724419, 2.88, 2036863, 68687556, "Cuenta Corriente", "marzo 2025"),

        # ----------------- C-0021 -----------------
        ("C-0021", date(2025, 7, 21), 1298, 57193310, 2.59, 1481306, 55712004, "Cuenta de Ahorros", "julio 2025"),
        ("C-0021", date(2025, 8, 13), 619, 44613380, 2.52, 1124257, 43489123, "Cuenta Corriente", "agosto 2025"),
        ("C-0021", date(2025, 2, 25), 990, 63744720, 1.99, 1268519, 62476201, "Cuenta de Ahorros", "febrero 2025"),
        ("C-0021", date(2025, 1, 18), 630, 232723554, 1.93, 4491564, 228231990, "Cuenta Corriente", "enero 2025"),
        ("C-0021", date(2025, 8, 22), 1207, 155035365, 2.45, 3798366, 151236999, "Cuenta de Ahorros", "agosto 2025"),

        # ----------------- C-0022 -----------------
        ("C-0022", date(2025, 9, 14), 1242, 124699022, 2.79, 3479102, 121219920, "Cuenta de Ahorros", "septiembre 2025"),
        ("C-0022", date(2025, 8, 9), 626, 230448976, 2.5, 5761224, 224687752, "Cuenta de Ahorros", "agosto 2025"),
        ("C-0022", date(2025, 4, 9), 1020, 25799279, 2.58, 665621, 25133658, "Cuenta Corriente", "abril 2025"),
        ("C-0022", date(2025, 5, 11), 774, 244720065, 2.39, 5848809, 238871256, "Cuenta Corriente", "mayo 2025"),
        ("C-0022", date(2025, 3, 8), 904, 191280735, 1.97, 3768230, 187512505, "Cuenta Corriente", "marzo 2025"),
        ("C-0022", date(2025, 2, 14), 954, 93820296, 2.4, 2251687, 91568609, "Cuenta de Ahorros", "febrero 2025"),

        # ----------------- C-0023 -----------------
        ("C-0023", date(2025, 4, 27), 980, 109549384, 2.8, 3067382, 106482002, "Cuenta Corriente", "abril 2025"),
        ("C-0023", date(2025, 7, 16), 132, 99424535, 2.13, 2117742, 97306793, "Cuenta de Ahorros", "julio 2025"),

        # ----------------- C-0024 -----------------
        ("C-0024", date(2025, 9, 24), 1238, 219712976, 2.46, 5404939, 214308037, "Cuenta Corriente", "septiembre 2025"),
        ("C-0024", date(2025, 8, 8), 678, 121993829, 2.33, 2842456, 119151373, "Cuenta de Ahorros", "agosto 2025"),
        ("C-0024", date(2025, 6, 22), 948, 199395959, 1.98, 3948039, 195447920, "Cuenta de Ahorros", "junio 2025"),
        ("C-0024", date(2025, 3, 20), 1213, 12238751, 2.8, 342685, 11896066, "Cuenta Corriente", "marzo 2025"),
        ("C-0024", date(2025, 2, 21), 997, 41426552, 2.75, 1139230, 40287322, "Cuenta Corriente", "febrero 2025"),

        # ----------------- C-0025 -----------------
        ("C-0025", date(2025, 5, 13), 790, 61817125, 2.3, 1421793, 60395332, "Cuenta de Ahorros", "mayo 2025"),
        ("C-0025", date(2025, 7, 9), 983, 72718622, 2.72, 1977946, 70740676, "Cuenta de Ahorros", "julio 2025"),
    ]

    for i, (
        commerce_code,
        settlement_date,
        transaction_count,
        total_amount,
        commission_rate,
        retained_amount,
        net_amount,
        account_type,
        period,
    ) in enumerate(settlements_data):
        commerce = db.query(Commerce).filter(Commerce.code == commerce_code).first()
        if commerce:
            unique_code = f"SET-{commerce_code}-{settlement_date}-{i}"
            settlement = Settlement(
                settlement_code=unique_code,
                commerce_id=commerce.id,
                settlement_date=settlement_date,
                transaction_count=transaction_count,
                total_amount=total_amount,
                commission_rate=commission_rate,
                retained_amount=retained_amount,
                net_amount=net_amount,
                account_type=account_type,
                period=period,
            )
            db.add(settlement)

    db.commit()
    db.close()
    print("✅ Settlements iniciales creados correctamente.")