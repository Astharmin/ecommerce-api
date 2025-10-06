# 🚀 Ecommerce API - Flask Powered

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?logo=jsonwebtokens&logoColor=white)
![Stripe](https://img.shields.io/badge/Payments-Stripe-008CDD?logo=stripe&logoColor=white)
![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

> *"API completa para plataforma e-commerce con autenticación JWT, procesamiento de pagos con Stripe y panel administrativo"*

---

## 🌟 Características Principales

### 🔐 Sistema de Autenticación
- ✅ **Registro e inicio de sesión** con JWT tokens
- 🛡️ **Autorización por roles** (Admin/Usuario)
- 🔒 **Password hashing** con BCrypt
- 📧 **Verificación por email** (opcional)

### 🛍️ Gestión de E-commerce
- 📦 **CRUD completo** de productos y categorías
- 🛒 **Carritos de compra** persistentes por usuario
- 📋 **Sistema de órdenes** con tracking de estado
- 💰 **Procesamiento de pagos** integrado con Stripe

### 👨‍💼 Panel Administrativo
- 📊 **Dashboard analytics** con métricas de ventas
- 📈 **Gestión de inventario** en tiempo real
- 👥 **Administración de usuarios** y permisos
- 🏷️ **Categorización avanzada** de productos

---

## 🛠️ Tecnologías Usadas

- **Backend:**  
  - Python 3.8+
  - Flask
  - JWT Tokens
  - SQLAlchemy ORM

- **Base de Datos:**  
  - MySQL

- **Pagos:**  
  - Stripe API

- **Seguridad:**  
  - BCrypt
  - JWT Authentication

---

## 🗂️ Estructura del Proyecto

```
ecommerce-api/
│
├── src/
│   ├── main.py
│   ├── auth/
│   │   ├── jwt_handler.py
│   │   └── routes.py
│   ├── products/
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── admin.py
│   ├── carts/
│   │   ├── models.py
│   │   └── routes.py
│   ├── orders/
│   │   ├── models.py
│   │   └── routes.py
│   ├── payments/
│   │   ├── stripe_service.py
│   │   └── routes.py
│   ├── users/
│   │   ├── models.py
│   │   └── routes.py
│   ├── admin_panel/
│   │   └── routes.py
│   └── database/
│       └── connection.py
├── requirements.txt
└── README.md
```

---

## 🚀 Instalación Rápida

```bash
# Clonar repositorio
git clone <URL_DEL_REPOSITORIO>
cd ecommerce-api

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python src/main.py
```

---

## 📚 Endpoints Principales

### 🔐 Autenticación
```http
POST /auth/register     # Registro de usuario
POST /auth/login        # Inicio de sesión
```

### 📦 Productos
```http
GET    /products        # Listar productos
POST   /products        # Crear producto (Admin)
PUT    /products/{id}   # Actualizar producto
DELETE /products/{id}   # Eliminar producto
```

### 🛒 Carrito
```http
GET    /cart           # Ver carrito
POST   /cart/add       # Agregar producto
DELETE /cart/remove    # Eliminar item
```

### 💰 Pagos
```http
POST /payments/create-intent  # Crear intento de pago
POST /payments/confirm        # Confirmar pago
```

---

## 📄 Licencia

MIT

---

<div align="center">

**Desarrollado con ❤️ por [Astharmin](https://github.com/Astharmin)**

*Proyecto basado en [roadmap.sh/projects/ecommerce-api](https://roadmap.sh/projects/ecommerce-api)*
