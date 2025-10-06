# Ecommerce API

https://roadmap.sh/projects/ecommerce-api

Este proyecto es una API para una plataforma de comercio electrónico, construida en Python utilizando Flask. La API incluye autenticación JWT, operaciones CRUD para productos y carritos de compra, integración con Stripe para pagos, y un panel de administración para gestionar productos e inventario.

## Estructura del Proyecto

```
ecommerce-api
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── auth                   # Módulo de autenticación
│   │   ├── jwt_handler.py     # Manejo de tokens JWT
│   │   └── routes.py          # Rutas de autenticación
│   ├── products               # Módulo de productos
│   │   ├── models.py          # Modelos de datos de productos
│   │   ├── routes.py          # Rutas CRUD de productos
│   │   └── admin.py           # Rutas del panel de administración de productos
│   ├── carts                  # Módulo de carritos de compra
│   │   ├── models.py          # Modelos de datos de carritos
│   │   └── routes.py          # Rutas de carritos
│   ├── orders                 # Módulo de pedidos
│   │   ├── models.py          # Modelos de datos de pedidos
│   │   └── routes.py          # Rutas de pedidos
│   ├── payments               # Módulo de pagos
│   │   ├── stripe_service.py   # Integración con Stripe
│   │   └── routes.py          # Rutas de pagos
│   ├── users                  # Módulo de usuarios
│   │   ├── models.py          # Modelos de datos de usuarios
│   │   └── routes.py          # Rutas de usuarios
│   ├── admin_panel            # Módulo del panel de administración
│   │   └── routes.py          # Rutas del panel de administración
│   └── database               # Módulo de conexión a la base de datos
│       └── connection.py      # Manejo de la conexión a la base de datos
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd ecommerce-api
   ```

2. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Inicia la aplicación:
   ```
   python src/main.py
   ```

2. Accede a la API en `http://localhost:5000`.

## Funcionalidades

- **Autenticación**: Registro e inicio de sesión de usuarios utilizando JWT.
- **Gestión de Productos**: CRUD para productos, incluyendo un panel de administración.
- **Carritos de Compra**: Manejo de carritos de compra para usuarios.
- **Pedidos**: Creación y gestión de pedidos.
- **Pagos**: Integración con Stripe para procesar pagos.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

