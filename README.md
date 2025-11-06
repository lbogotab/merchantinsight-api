# MerchantInsight API

## Descripción General
MerchantInsight API es una aplicación desarrollada en **FastAPI** y **SQLAlchemy** que permite la gestión, análisis y consulta integral de información comercial. Está diseñada para ofrecer trazabilidad completa de comercios, terminales, contratos, conciliaciones, facturas, incidentes y observaciones. Su objetivo principal es centralizar datos relevantes del ecosistema de comercios y facilitar la integración con herramientas de inteligencia de negocio.

## Ejecución Local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/merchantinsight-api.git
   cd merchantinsight-api
   ```

2. Crear entorno virtual e instalar dependencias:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # o .venv\Scripts\activate en Windows
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

4. Acceder a la documentación interactiva:
   ```
   http://localhost:8000/docs
   ```

> Al iniciar, la base de datos se limpia y se pobla automáticamente con datos de ejemplo (seeds).

## Ejecución con Docker

1. Construir imagen:
   ```bash
   docker build -t merchantinsight-api .
   ```

2. Ejecutar contenedor:
   ```bash
   docker run -p 8000:8000 merchantinsight-api
   ```

3. Acceso:
   ```
   http://localhost:8000
   ```

## Estructura del Proyecto

```
app/
├── main.py                # Punto de entrada de la aplicación
├── models/                # Modelos SQLAlchemy (Commerce, Terminal, Factura, etc.)
├── routers/               # Rutas organizadas por dominio (commerces, detail, observation, etc.)
├── seeds/                 # Datos iniciales cargados automáticamente
├── db.py            # Configuración y conexión a SQLite
```

## Endpoints Principales

| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| `GET` | `/commerces/detail-full/{commerce_code}` | Devuelve el detalle completo del comercio (comercio, terminales, contratos, facturas, conciliaciones, incidentes, observaciones). |
| `GET` | `/commerces/detail/{commerce_code}` | Devuelve un resumen simplificado del comercio (sin contratos, conciliaciones ni soportes). |
| `POST` | `/commerces/observation/{commerce_code}` | Permite añadir una observación asociada a un comercio. |
| `GET` | `/commerces/observation/{commerce_code}` | Obtiene las observaciones registradas para un comercio. |

## Ejemplo de Respuesta (Detalle Completo)

```json
{
  "comercio": {
    "codigo": "C-0001",
    "nombre": "Panadería La 85 S.A.S.",
    "segmento": "Microempresa",
    "estado": "Activo",
    "canal_principal": "POS Físico",
    "ciudad": "Bogotá",
    "departamento": "Cundinamarca",
    "nivel_riesgo": "Bajo"
  },
  "terminales": [
    {
      "codigo_terminal": "T-10001",
      "modelo": "SmartPOS Clover Flex",
      "estado": "En mantenimiento",
      "resumen_transacciones": {
        "total_transacciones": 774,
        "volumen_total": 34885207
      },
      "novedades": [
        {
          "codigo": "NVD-T-10001-2025-02-01-Cambio",
          "fecha": "2025-02-01",
          "tipo": "Cambio de estado",
          "responsable": "Credibanco"
        }
      ]
    }
  ],
  "contratos": [
    {
      "codigo": "CTR-2025-1001",
      "producto_principal": "SmartPOS",
      "valor_total": 21573195,
      "estado": "En renovación"
    }
  ],
  "facturas": [
    {
      "codigo": "FCT-2025-1001",
      "periodo": "mayo 2025",
      "importe_bruto": 18664766,
      "estado": "Pagada"
    }
  ],
  "conciliaciones": [
    {
      "codigo": "SET-C-0001-2025-01-24-0",
      "transacciones": 683,
      "monto_total": 70737657
    }
  ],
  "tickets_soporte": [],
  "observaciones": []
}
```

## Ejemplo de Respuesta (Detalle Lite)

```json
{
  "codigo": "C-0001",
  "nombre": "Panadería La 85 S.A.S.",
  "segmento": "Microempresa",
  "estado": "Activo",
  "ciudad": "Bogotá",
  "terminales_activas": 3,
  "facturacion_promedio": 2500000
}
```

## Tecnologías Utilizadas

- **Python 3.13**
- **FastAPI** — Framework principal de la API.
- **SQLAlchemy** — ORM para manejo de base de datos.
- **SQLite** — Base de datos embebida por defecto.
- **Uvicorn** — Servidor ASGI.
- **Docker** — Contenerización y despliegue rápido.

## Notas de Desarrollo

- El sistema carga automáticamente datos de muestra al iniciar (`seeds`).
- Cada modelo está diseñado para escalar y permitir integración con servicios externos (p. ej. Cybersource, CRM, sistemas de monitoreo).
- Se recomienda mantener los archivos de modelos y seeds separados para modularidad y pruebas unitarias.
