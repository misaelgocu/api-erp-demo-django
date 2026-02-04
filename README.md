# API ERP - Sistema de Ventas KFC

API REST desarrollada con Django y Django REST Framework para gestionar ventas de restaurantes KFC. Sistema con arquitectura limpia que administra empresas, marcas, sucursales y registros de ventas.

## 🚀 Características

- **CRUD completo** para Empresas, Marcas, Sucursales y Ventas
- **Relaciones optimizadas** con select_related para mejor rendimiento
- **Documentación automática** con Swagger UI y ReDoc  
- **CORS configurado** para integración con frontend
- **SQLite** para desarrollo y despliegue en PythonAnywhere
- **Endpoints con y sin relaciones** para flexibilidad en consultas

## 📋 Requisitos

- Python 3.10+
- pip
- virtualenv (recomendado)

## 🔧 Instalación Local

### 1. Clonar el repositorio

```bash
git clone <tu-repositorio>
cd API_erp_demo/erp
```

### 2. Crear y activar entorno virtual

```bash
# Crear entorno virtual
python -m venv ../venv

# Activar (Linux/Mac)
source ../venv/bin/activate

# Activar (Windows)
..\venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6. Iniciar servidor de desarrollo

```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/`

## 📚 Documentación de la API

Con el servidor corriendo, accede a:

- **Swagger UI**: http://127.0.0.1:8000/docs/
- **ReDoc**: http://127.0.0.1:8000/redoc/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🛣️ Endpoints Principales

### Empresas
- `GET /api/empresas/` - Listar empresas
- `POST /api/empresas/` - Crear empresa
- `GET /api/empresas/{id}/` - Obtener empresa
- `PUT /api/empresas/{id}/` - Actualizar empresa
- `DELETE /api/empresas/{id}/` - Eliminar empresa

### Marcas
- `GET /api/marcas/` - Listar marcas
- `POST /api/marcas/` - Crear marca
- `GET /api/marcas/{id}/` - Obtener marca
- `PUT /api/marcas/{id}/` - Actualizar marca
- `DELETE /api/marcas/{id}/` - Eliminar marca

### Sucursales
- `GET /api/sucursales/` - Listar sucursales
- `POST /api/sucursales/` - Crear sucursal
- `GET /api/sucursales/{id}/` - Obtener sucursal
- `PUT /api/sucursales/{id}/` - Actualizar sucursal
- `DELETE /api/sucursales/{id}/` - Eliminar sucursal

### Ventas
- `GET /api/ventas/` - Listar ventas
- `POST /api/ventas/` - Crear venta
- `GET /api/ventas/{id}/` - Obtener venta
- `PUT /api/ventas/{id}/` - Actualizar venta
- `DELETE /api/ventas/{id}/` - Eliminar venta

### Ventas con Relaciones (Solo Lectura)
- `GET /api/ventas-completas/` - Ventas con datos completos de sucursal, marca y empresa
- `GET /api/ventas-completas/{id}/` - Venta completa con todas las relaciones

## 🗂️ Estructura del Proyecto

```
erp/
├── kfc/                    # Configuración del proyecto
│   ├── settings.py        # Configuración Django
│   ├── urls.py           # Rutas principales
│   └── wsgi.py           # Punto de entrada WSGI
├── ventas/               # App de ventas
│   ├── models.py        # Modelos de datos
│   ├── admin.py         # Admin de Django
│   └── api/             # API REST
│       ├── serializers.py  # Serializadores
│       ├── views.py       # ViewSets
│       └── urls.py        # Rutas de API
├── manage.py            # CLI de Django
├── requirements.txt     # Dependencias
└── .gitignore          # Archivos ignorados
```

## 🏗️ Modelos

**Empresas** → **Marcas** → **Sucursales** → **Ventas**

- **Empresas**: Empresas del grupo corporativo
- **Marcas**: Marcas de cada empresa (1:N)
- **Sucursales**: Sucursales por marca (1:N)
- **Ventas**: Registros diarios con:
  - Ventas netas, IVA, descuentos
  - Canales: comedor, llevar, entrega, ventana
  - Reembolsos a clientes

## 🌐 Despliegue en PythonAnywhere

### Preparación

1. Sube tu código a GitHub
2. Regístrate en [PythonAnywhere](https://www.pythonanywhere.com/)

### Configuración

```bash
# En consola Bash de PythonAnywhere
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo/erp

# Crear virtualenv
mkvirtualenv --python=/usr/bin/python3.12 kfc-env

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

### Configurar Web App

En la pestaña "Web" de PythonAnywhere:

1. Crear nueva app → Manual configuration → Python 3.10
2. Configurar paths:
   - Source code: `/home/tu_usuario/tu-repo/erp`
   - Working directory: `/home/tu_usuario/tu-repo/erp`
   - Virtualenv: `/home/tu_usuario/.virtualenvs/kfc-env`

3. Editar archivo WSGI:

```python
import os
import sys

path = '/home/tu_usuario/tu-repo/erp'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'kfc.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

4. Configurar static files:
   - URL: `/static/`
   - Directory: `/home/tu_usuario/tu-repo/erp/staticfiles`

5. Actualizar `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['tu_usuario.pythonanywhere.com']

CORS_ALLOWED_ORIGINS = [
    'https://kfc-erp.netlify.app',
]

CSRF_TRUSTED_ORIGINS = [
    'https://tu_usuario.pythonanywhere.com',
    'https://kfc-erp.netlify.app',
]
```

6. Reload la aplicación

Tu API estará en: `https://tu_usuario.pythonanywhere.com`

## 🔐 Configuración de CORS

El proyecto permite peticiones desde:
- `http://localhost:5173` (desarrollo)
- `https://kfc-erp.netlify.app` (producción)

Modifica `CORS_ALLOWED_ORIGINS` en `settings.py` según necesites.

## 🔧 Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver

# Recolectar archivos estáticos
python manage.py collectstatic

# Shell de Django
python manage.py shell
```

## 📊 Base de Datos

El proyecto usa SQLite por defecto. Si necesitas cambiar la configuración, edita `DATABASES` en `settings.py`.

## 🛡️ Seguridad para Producción

Antes de desplegar:

1. Cambia `SECRET_KEY` en `settings.py`
2. Establece `DEBUG = False`
3. Configura `ALLOWED_HOSTS` con tu dominio
4. Configura CORS y CSRF apropiadamente

## 📝 Licencia

MIT License - ver archivo LICENSE

## ✍️ Autor

Misael Gómez Cuautle

---

⭐ Si este proyecto te es útil, considera darle una estrella en GitHub
