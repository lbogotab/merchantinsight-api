# MerchantInsight API

## Descripción General
MerchantInsight API es una aplicación desarrollada en **FastAPI** y **SQLAlchemy** que permite la gestión, análisis y consulta integral de información comercial. Está diseñada para ofrecer trazabilidad completa de comercios, terminales, contratos, conciliaciones, facturas, incidentes y observaciones. Su objetivo principal es centralizar datos relevantes del ecosistema de comercios y facilitar la integración con herramientas de inteligencia de negocio.

## Ejecución Local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/lbogotab/merchantinsight-api.git
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

## Comercios prueba
Los comercios de prueba van del 1 al 25

  ```bash
    C-0001
  ```

  ```bash
    C-0025
  ```

## Ejemplo de Respuesta (Detalle Completo)

```json
{
  "comercio": {
    "codigo": "C-0001",
    "nombre": "Panadería La 85 S.A.S.",
    "segmento": "Microempresa",
    "estado": "Activo",
    "canal_principal": "POS Físico",
    "direccion": "Cra 85 # 15-20",
    "ciudad": "Bogotá",
    "departamento": "Cundinamarca",
    "correo_contacto": "contacto@panaderiala85.com",
    "telefono_contacto": "+5712345678",
    "nivel_riesgo": "Bajo",
    "facturacion_promedio": 2500000,
    "productos_principales": "Pan, pasteles y productos de panadería"
  },
  "terminales": [
    {
      "codigo_terminal": "T-10001",
      "ciudad": "Bogotá",
      "modelo": "SmartPOS Clover Flex",
      "estado": "En mantenimiento",
      "canal": "POS Físico",
      "franquicias": "Mastercard,American Express",
      "asignado_por": "Credibanco",
      "ultima_actualizacion": "2025-11-06T20:43:16",
      "resumen_transacciones": {
        "total_transacciones": 774,
        "volumen_total": 34885207,
        "ciudad": "Bogotá",
        "canal": "POS Físico"
      },
      "novedades": [
        {
          "codigo": "NVD-T-10001-2025-02-01-Cambiodeesta",
          "fecha": "2025-02-01",
          "tipo": "Cambio de estado",
          "responsable": "Credibanco",
          "observacion": "Actualización de estado operativo de la terminal T-10001 tras proceso de mantenimiento."
        },
        {
          "codigo": "NVD-T-10001-2025-04-05-Altadetermin",
          "fecha": "2025-04-05",
          "tipo": "Alta de terminal",
          "responsable": "Credibanco",
          "observacion": "Se registró la instalación de la terminal T-10001 en un nuevo punto de venta."
        },
        {
          "codigo": "NVD-T-10001-2025-07-02-Altadetermin",
          "fecha": "2025-07-02",
          "tipo": "Alta de terminal",
          "responsable": "Credibanco",
          "observacion": "Se registró la instalación de la terminal T-10001 en un nuevo punto de venta."
        }
      ]
    },
    {
      "codigo_terminal": "T-10002",
      "ciudad": "Bogotá",
      "modelo": "Verifone VX520",
      "estado": "Activo",
      "canal": "POS Físico",
      "franquicias": "Mastercard,American Express",
      "asignado_por": "Credibanco",
      "ultima_actualizacion": "2025-11-06T20:43:16",
      "resumen_transacciones": {
        "total_transacciones": 145,
        "volumen_total": 204058447,
        "ciudad": "Bogotá",
        "canal": "POS Físico"
      },
      "novedades": [
        {
          "codigo": "NVD-T-10002-2025-04-17-Reasignación",
          "fecha": "2025-04-17",
          "tipo": "Reasignación comercial",
          "responsable": "Credibanco",
          "observacion": "Reasignación de la terminal T-10002 a un nuevo comercio o ubicación."
        }
      ]
    },
    {
      "codigo_terminal": "T-10003",
      "ciudad": "Bogotá",
      "modelo": "Ingenico iCT250",
      "estado": "Activo",
      "canal": "POS Físico",
      "franquicias": "Mastercard",
      "asignado_por": "Credibanco",
      "ultima_actualizacion": "2025-11-06T20:43:16",
      "resumen_transacciones": {
        "total_transacciones": 401,
        "volumen_total": 70737657,
        "ciudad": "Bogotá",
        "canal": "POS Físico"
      },
      "novedades": [
        {
          "codigo": "NVD-T-10003-2025-01-25-Bajadetermin",
          "fecha": "2025-01-25",
          "tipo": "Baja de terminal",
          "responsable": "Comercio",
          "observacion": "La terminal T-10003 fue retirada del sistema por obsolescencia o solicitud del comercio."
        },
        {
          "codigo": "NVD-T-10003-2025-04-15-Reasignación",
          "fecha": "2025-04-15",
          "tipo": "Reasignación comercial",
          "responsable": "Comercio",
          "observacion": "Reasignación de la terminal T-10003 a un nuevo comercio o ubicación."
        },
        {
          "codigo": "NVD-T-10003-2025-04-23-Reasignación",
          "fecha": "2025-04-23",
          "tipo": "Reasignación comercial",
          "responsable": "Comercio",
          "observacion": "Reasignación de la terminal T-10003 a un nuevo comercio o ubicación."
        }
      ]
    }
  ],
  "contratos": [
    {
      "codigo": "CTR-2025-1001",
      "fecha_firma": "2025-07-31",
      "producto_principal": "SmartPOS",
      "duracion_meses": 24,
      "valor_total": 21573195,
      "estado": "En renovación",
      "representante": "Julián Pérez",
      "notas": "Contrato con liquidación mensual."
    }
  ],
  "facturas": [
    {
      "codigo": "FCT-2025-1001",
      "fecha_emision": "2025-05-03",
      "periodo": "mayo 2025",
      "importe_bruto": 18664766,
      "descuentos_retenciones": 671805,
      "impuestos": 3546305.54,
      "importe_neto": 17992961,
      "estado": "Pagada",
      "metodo_pago": "Débito automático",
      "recurrente": true
    },
    {
      "codigo": "FCT-2025-1002",
      "fecha_emision": "2025-06-11",
      "periodo": "junio 2025",
      "importe_bruto": 6741530,
      "descuentos_retenciones": 199412,
      "impuestos": 1280890.7,
      "importe_neto": 6542118,
      "estado": "Pendiente",
      "metodo_pago": "Transferencia",
      "recurrente": true
    }
  ],
  "incidentes": [],
  "conciliaciones": [
    {
      "codigo": "SET-C-0001-2025-01-24-0",
      "fecha": "2025-01-24",
      "transacciones": 683,
      "monto_total": 70737657,
      "tasa_comision": 2.05,
      "retenido": 1450121,
      "neto": 69287536,
      "tipo_cuenta": "Cuenta Corriente",
      "periodo": "enero 2025"
    },
    {
      "codigo": "SET-C-0001-2025-09-03-1",
      "fecha": "2025-09-03",
      "transacciones": 1329,
      "monto_total": 118258777,
      "tasa_comision": 1.83,
      "retenido": 2164135,
      "neto": 116094642,
      "tipo_cuenta": "Cuenta Corriente",
      "periodo": "septiembre 2025"
    }
  ],
  "tickets_soporte": [],
  "observaciones": [
    {
      "id": 1,
      "comentario": "Test Observation",
      "fecha": "2025-11-06T20:44:30.149216"
    }
  ]
}
```

## Ejemplo de Respuesta (Detalle Lite)

```json
{
  "comercio": {
    "codigo": "C-0001",
    "nombre": "Panadería La 85 S.A.S.",
    "segmento": "Microempresa",
    "estado": "Activo",
    "canal_principal": "POS Físico",
    "direccion": "Cra 85 # 15-20",
    "ciudad": "Bogotá",
    "departamento": "Cundinamarca",
    "correo_contacto": "contacto@panaderiala85.com",
    "telefono_contacto": "+5712345678",
    "nivel_riesgo": "Bajo",
    "facturacion_promedio": 2500000,
    "productos_principales": "Pan, pasteles y productos de panadería"
  },
  "terminales": [
    {
      "codigo_terminal": "T-10001",
      "ciudad": "Bogotá",
      "modelo": "SmartPOS Clover Flex",
      "estado": "En mantenimiento",
      "canal": "POS Físico",
      "franquicias": "Mastercard,American Express",
      "asignado_por": "Credibanco",
      "ultima_actualizacion": "2025-11-06T20:43:16",
      "resumen_transacciones": {
        "total_transacciones": 774,
        "volumen_total": 34885207
      },
      "novedades": [
        {
          "codigo": "NVD-T-10001-2025-02-01-Cambiodeesta",
          "fecha": "2025-02-01",
          "tipo": "Cambio de estado",
          "responsable": "Credibanco",
          "observacion": "Actualización de estado operativo de la terminal T-10001 tras proceso de mantenimiento."
        },
        {
          "codigo": "NVD-T-10001-2025-04-05-Altadetermin",
          "fecha": "2025-04-05",
          "tipo": "Alta de terminal",
          "responsable": "Credibanco",
          "observacion": "Se registró la instalación de la terminal T-10001 en un nuevo punto de venta."
        },
        {
          "codigo": "NVD-T-10001-2025-07-02-Altadetermin",
          "fecha": "2025-07-02",
          "tipo": "Alta de terminal",
          "responsable": "Credibanco",
          "observacion": "Se registró la instalación de la terminal T-10001 en un nuevo punto de venta."
        }
      ]
    },
    {
      "codigo_terminal": "T-10002",
      "ciudad": "Bogotá",
      "modelo": "Verifone VX520",
      "estado": "Activo",
      "canal": "POS Físico",
      "franquicias": "Mastercard,American Express",
      "asignado_por": "Credibanco",
      "ultima_actualizacion": "2025-11-06T20:43:16",
      "resumen_transacciones": {
        "total_transacciones": 145,
        "volumen_total": 204058447
      },
      "novedades": [
        {
          "codigo": "NVD-T-10002-2025-04-17-Reasignación",
          "fecha": "2025-04-17",
          "tipo": "Reasignación comercial",
          "responsable": "Credibanco",
          "observacion": "Reasignación de la terminal T-10002 a un nuevo comercio o ubicación."
        }
      ]
    },
    {
      "codigo_terminal": "T-10003",
      "ciudad": "Bogotá",
      "modelo": "Ingenico iCT250",
      "estado": "Activo",
      "canal": "POS Físico",
      "franquicias": "Mastercard",
      "asignado_por": "Credibanco",
      "ultima_actualizacion": "2025-11-06T20:43:16",
      "resumen_transacciones": {
        "total_transacciones": 401,
        "volumen_total": 70737657
      },
      "novedades": [
        {
          "codigo": "NVD-T-10003-2025-01-25-Bajadetermin",
          "fecha": "2025-01-25",
          "tipo": "Baja de terminal",
          "responsable": "Comercio",
          "observacion": "La terminal T-10003 fue retirada del sistema por obsolescencia o solicitud del comercio."
        },
        {
          "codigo": "NVD-T-10003-2025-04-15-Reasignación",
          "fecha": "2025-04-15",
          "tipo": "Reasignación comercial",
          "responsable": "Comercio",
          "observacion": "Reasignación de la terminal T-10003 a un nuevo comercio o ubicación."
        },
        {
          "codigo": "NVD-T-10003-2025-04-23-Reasignación",
          "fecha": "2025-04-23",
          "tipo": "Reasignación comercial",
          "responsable": "Comercio",
          "observacion": "Reasignación de la terminal T-10003 a un nuevo comercio o ubicación."
        }
      ]
    }
  ],
  "facturas": [
    {
      "codigo": "FCT-2025-1001",
      "fecha_emision": "2025-05-03",
      "periodo": "mayo 2025",
      "importe_neto": 17992961,
      "estado": "Pagada"
    },
    {
      "codigo": "FCT-2025-1002",
      "fecha_emision": "2025-06-11",
      "periodo": "junio 2025",
      "importe_neto": 6542118,
      "estado": "Pendiente"
    }
  ],
  "incidentes": [],
  "observaciones": [
    {
      "id": 1,
      "comentario": "Test Observation",
      "fecha": "2025-11-06T20:44:30.149216"
    }
  ]
}
```
## Ejemplo de ingreso de novedad de un comercio
1. Ingresar código de comercio
   ```bash
   C-0001
   ```

2. Ingresar comentario en texto
   ```bash
   Observación de prueba para el comercio 1
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
