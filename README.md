# 🚀 Ecommerce API - Flask Powered

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?logo=jsonwebtokens&logoColor=white)
![Stripe](https://img.shields.io/badge/Payments-Stripe-008CDD?logo=stripe&logoColor=white)
![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

> *"API completa para plataforma e-commerce con autenticación JWT, procesamiento de pagos con Stripe y panel administrativo"*

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

## 🏗️ Arquitectura del Sistema

```mermaid
graph TB
    A[Client Frontend] --> B[Flask API]
    B --> C[JWT Authentication]
    B --> D[Product Management]
    B --> E[Cart & Orders]
    B --> F[Stripe Payments]
    B --> G[Admin Panel]
    
    C --> H[User Database]
    D --> I[Products Database]
    E --> J[Orders Database]
    F --> K[Stripe API]
    G --> L[Admin Dashboard]
